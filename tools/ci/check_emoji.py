#!/usr/bin/env python3
"""確認教材（.md / .html / .yml / .py）不含 emoji。

用法：python3 tools/ci/check_emoji.py [檔案或資料夾 ...]
發現 emoji 時 exit 1，並列出位置。方向箭頭（← → ↑ ↓）與 Mac 按鍵符號（⌘ ⌥ ⌃ ⇧）不算 emoji。
"""
import os
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
EXTS = (".md", ".html", ".yml", ".yaml", ".py")
RANGES = [
    (0x1F000, 0x1FAFF),  # 各類 emoji 與符號
    (0x2600, 0x27BF),    # 雜項符號與 dingbats
    (0x2B00, 0x2BFF),    # 星號、方塊等
    (0x23E9, 0x23FA),    # 時鐘、播放鍵等
    (0x231A, 0x231B),    # 手錶、沙漏
    (0xFE0F, 0xFE0F),    # emoji 變體選擇符
    (0x200D, 0x200D),    # ZWJ
    (0x20E3, 0x20E3),    # 鍵帽組合符
    (0x3297, 0x3299),
]


def is_emoji(ch):
    cp = ord(ch)
    return any(a <= cp <= b for a, b in RANGES)


def scan(path):
    hits = []
    with open(path, encoding="utf-8", errors="ignore") as f:
        for no, line in enumerate(f, 1):
            found = sorted({c for c in line if is_emoji(c)})
            if found:
                hits.append((no, "".join(found)))
    return hits


def main(args):
    targets = args or [ROOT]
    files = []
    for t in targets:
        if os.path.isdir(t):
            for d, dirs, fs in os.walk(t):
                dirs[:] = [x for x in dirs if x not in (".git", "node_modules")]
                files += [os.path.join(d, x) for x in fs if x.endswith(EXTS)]
        else:
            files.append(t)
    total = 0
    for f in sorted(files):
        for no, chars in scan(f):
            print(f"{os.path.relpath(f, ROOT)}:{no}: {chars}")
            total += 1
    print(f"檢查 {len(files)} 個檔案，{'未發現 emoji' if not total else f'{total} 行含有 emoji'}")
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
