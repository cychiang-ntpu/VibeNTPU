#!/usr/bin/env python3
"""檢查 repo 內所有 Markdown 的相對連結與 #錨點是否存在（GitHub 錨點規則）。

用法：python3 tools/ci/check_links.py [repo 根目錄]
有壞連結時 exit 1。只用 Python 標準函式庫。
"""
import os
import re
import sys
import unicodedata
from urllib.parse import unquote

ROOT = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(__file__), "..", ".."))


def slugify(heading):
    """模仿 GitHub 產生標題錨點：小寫、保留文字數字與 - _，空白變 -。"""
    text = re.sub(r"<[^>]+>", "", heading.strip())
    text = re.sub(r"[`*]", "", text).lower()
    out = []
    for ch in text:
        if ch == " ":
            out.append("-")
        elif ch in "-_" or unicodedata.category(ch)[0] in "LN":
            out.append(ch)
    return "".join(out)


def anchors_of(path):
    slugs, counts = set(), {}
    in_code = False
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.lstrip().startswith("```"):
                in_code = not in_code
                continue
            m = None if in_code else re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", line)
            if m:
                s = slugify(m.group(2))
                n = counts.get(s, 0)
                slugs.add(s if n == 0 else f"{s}-{n}")
                counts[s] = n + 1
    return slugs


def main():
    md_files = []
    for d, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in (".git", "node_modules")]
        md_files += [os.path.join(d, f) for f in files if f.endswith(".md")]

    cache, bad = {}, 0
    for f in sorted(md_files):
        text = open(f, encoding="utf-8").read()
        text = re.sub(r"```.*?```", "", text, flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for link in re.findall(r"\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)", text):
            if re.match(r"^[a-z]+:", link):
                continue
            path, _, anchor = link.partition("#")
            target = os.path.normpath(os.path.join(os.path.dirname(f), unquote(path))) if path else f
            rel = os.path.relpath(f, ROOT)
            if not os.path.exists(target):
                print(f"❌ {rel}: 找不到檔案 {link}")
                bad += 1
                continue
            if anchor and target.endswith(".md"):
                if target not in cache:
                    cache[target] = anchors_of(target)
                if unquote(anchor) not in cache[target]:
                    print(f"❌ {rel}: 找不到錨點 {link}")
                    bad += 1
    print(f"檢查 {len(md_files)} 個 Markdown 檔，{'全部連結正常 ✅' if not bad else f'{bad} 個壞連結'}")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main())
