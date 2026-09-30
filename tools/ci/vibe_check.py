#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VibeNTPU 健檢站（命令列 / GitHub Actions 版）

只用 Python 標準函式庫，檢查你的 index.html 有沒有達成每週的任務。
檢查項目與網頁版 tools/vibe_check.html 完全相同（check ID 一致）。

用法：
    python3 vibe_check.py index.html              # 檢查第 1 關（預設）
    python3 vibe_check.py index.html --level 3    # 檢查到第 3 關
    python3 vibe_check.py index.html --json       # 輸出 JSON
    python3 vibe_check.py index.html --markdown   # 輸出 Markdown（給 $GITHUB_STEP_SUMMARY）

結束代碼：到 --level 為止的「必要」項目全部通過 → 0；否則 → 1；讀檔失敗 → 2。
"""
import argparse
import json
import re
import sys
from html.parser import HTMLParser

REQ, WARN, BONUS = "required", "warn", "bonus"
XP = {REQ: 10, WARN: 5, BONUS: 5}

LEVELS = {
    1: {"icon": "🏪", "name": "開店徽章", "desc": "第 1 週：把店面（形象首頁）開起來"},
    2: {"icon": "📦", "name": "收單徽章", "desc": "第 2 週：用 Netlify Forms 收早鳥名單"},
    3: {"icon": "💾", "name": "記憶徽章", "desc": "第 2 週：LocalStorage 記住會員＋AJAX 送出"},
}

# (id, level, kind, 標題, 失敗時的提示) —— 與 vibe_check.html 的 CHECKS 保持一致
CHECKS = [
    ("l1_html", 1, REQ, "檔案是 HTML 格式",
     "檔案裡找不到 <html> 或 <!DOCTYPE html>。請確認你選的是 index.html；或請跟 AI 說：「請給我完整的 HTML 檔案，從 <!DOCTYPE html> 開始」"),
    ("l1_charset", 1, REQ, "設定 UTF-8 編碼（中文不亂碼）",
     "請跟 AI 說：「請在 <head> 加上 <meta charset=\"UTF-8\">」"),
    ("l1_viewport", 1, REQ, "設定 viewport（手機版 RWD）",
     "請跟 AI 說：「請在 <head> 加上 <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">」"),
    ("l1_title", 1, REQ, "有網頁標題 <title>",
     "請跟 AI 說：「請在 <head> 加上 <title>，內容是我的產品名稱＋一句話介紹」"),
    ("l1_h1", 1, REQ, "有大標題 <h1>",
     "請跟 AI 說：「請在主視覺區加上一個 <h1> 大標題，寫出產品最吸引人的一句話」"),
    ("l1_cta", 1, REQ, "有行動按鈕（CTA）",
     "請跟 AI 說：「請在主視覺區加上一個醒目的行動按鈕（例如『立即加入』），用 <a> 或 <button>」"),
    ("l1_style", 1, REQ, "有 CSS 樣式（不是陽春白底黑字）",
     "請跟 AI 說：「請用 <style> 幫整個頁面加上配色、字體與排版，全部寫在同一個 index.html 裡」"),
    ("l1_media", 1, WARN, "有 @media 手機版樣式",
     "請跟 AI 說：「請加上 @media (max-width: 640px) 的手機版樣式，讓手機上也好看」"),
    ("l1_img", 1, WARN, "沒有引用不存在的圖片檔",
     "你用了相對路徑的圖片（例如 photo.jpg），但 repo 裡可能沒有這個檔案，上線後會破圖。請跟 AI 說：「請把圖片改成 emoji 或 inline SVG，不要引用外部圖片檔」"),
    ("l2_form", 2, REQ, "有 Netlify 表單（data-netlify=\"true\"）",
     "請跟 AI 說：「請加一個早鳥名單表單，<form> 要有 data-netlify=\"true\" 和 method=\"POST\"」"),
    ("l2_form_name", 2, REQ, "表單有 name 名稱",
     "請跟 AI 說：「請幫 <form> 加上 name=\"waitlist\"，這是 Netlify 後台收件箱的名字」"),
    ("l2_hidden_form_name", 2, REQ, "有隱藏欄位 form-name 且值與表單名稱相同",
     "請跟 AI 說：「請在 <form> 裡加上 <input type=\"hidden\" name=\"form-name\" value=\"（跟表單 name 一樣）\">」"),
    ("l2_field_names", 2, REQ, "每個輸入欄位都有 name",
     "沒有 name 的欄位，Netlify 收不到資料。請跟 AI 說：「請確認表單裡每個 input、select、textarea 都有 name 屬性」"),
    ("l2_email", 2, WARN, "有 Email 欄位（type=\"email\"）",
     "請跟 AI 說：「請在表單加上 <input type=\"email\" name=\"email\" required>，讓瀏覽器幫忙檢查格式」"),
    ("l2_honeypot", 2, BONUS, "有防機器人陷阱（honeypot）",
     "加分題！請跟 AI 說：「請在 <form> 加上 netlify-honeypot=\"bot-field\"，並加一個隱藏的 <input name=\"bot-field\">」"),
    ("l3_set", 3, REQ, "用 localStorage.setItem 存資料",
     "請跟 AI 說：「送出表單成功後，請用 localStorage.setItem 把使用者名字存起來」"),
    ("l3_get", 3, REQ, "用 localStorage.getItem 讀資料",
     "請跟 AI 說：「打開網頁時，請用 localStorage.getItem 檢查有沒有存過名字，有的話顯示『歡迎回來』儀表板」"),
    ("l3_prevent", 3, REQ, "用 preventDefault 阻止頁面跳轉",
     "請跟 AI 說：「表單送出時，請先呼叫 event.preventDefault()，不要跳到別的頁面」"),
    ("l3_fetch", 3, REQ, "用 fetch() 以 AJAX 送出表單",
     "請跟 AI 說：「請用 fetch('/', { method: 'POST', ... }) 在背景把表單送給 Netlify」"),
    ("l3_urlencoded", 3, REQ, "送出格式是 application/x-www-form-urlencoded",
     "請跟 AI 說：「fetch 的 headers 請設定 'Content-Type': 'application/x-www-form-urlencoded'，body 用 new URLSearchParams(formData).toString()」"),
    ("l3_logout", 3, BONUS, "有登出功能（removeItem 或 clear）",
     "加分題！請跟 AI 說：「請在儀表板加一個登出按鈕，按下去用 localStorage.removeItem 清掉資料」"),
]

EXTERNAL_SRC = re.compile(r"^(?:[a-z][a-z0-9+.-]*:|//)", re.I)
RE_HTML = re.compile(r"<!doctype\s+html|<html[\s>]", re.I)
RE_SET = re.compile(r"localStorage\s*\.\s*setItem\s*\(")
RE_GET = re.compile(r"localStorage\s*\.\s*getItem\s*\(")
RE_PREVENT = re.compile(r"preventDefault\s*\(")
RE_FETCH = re.compile(r"\bfetch\s*\(")
RE_URLENC = re.compile(r"application/x-www-form-urlencoded", re.I)
RE_LOGOUT = re.compile(r"localStorage\s*\.\s*(?:removeItem|clear)\s*\(")
RE_MEDIA = re.compile(r"@media\b", re.I)
SKIP_INPUT_TYPES = {"submit", "button", "reset", "image"}


class _Collector(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.metas, self.links, self.imgs, self.forms = [], [], [], []
        self.title_parts, self.style_parts, self.script_parts = [], [], []
        self.h1 = 0
        self.cta = 0
        self._in = None          # "title" / "style" / "script"（目前在收集哪一段文字）
        self._script_inline = False
        self._form = None        # 目前所在的 form
        self._title_seen = False # 只看第一個 <title>

    def handle_starttag(self, tag, attrs):
        a = {k.lower(): (v if v is not None else "") for k, v in attrs}
        if tag == "meta":
            self.metas.append(a)
        elif tag == "link":
            self.links.append(a)
        elif tag == "img":
            self.imgs.append(a)
        elif tag == "h1":
            self.h1 += 1
        elif tag == "button" or (tag == "a" and "href" in a):
            self.cta += 1
        elif tag == "title" and not self._title_seen:
            self._in = "title"
            self._title_seen = True
        elif tag == "style":
            self._in = "style"
        elif tag == "script":
            self._in = "script"
            self._script_inline = "src" not in a
        elif tag == "form":
            self._form = {"attrs": a, "fields": []}
            self.forms.append(self._form)
        if tag in ("input", "select", "textarea") and self._form is not None:
            self._form["fields"].append((tag, a))

    def handle_endtag(self, tag):
        if tag in ("title", "style", "script"):
            self._in = None
        elif tag == "form":
            self._form = None

    def handle_data(self, data):
        if self._in == "title":
            self.title_parts.append(data)
        elif self._in == "style":
            self.style_parts.append(data)
        elif self._in == "script" and self._script_inline:
            self.script_parts.append(data)


def _is_netlify(form_attrs):
    return form_attrs.get("data-netlify", "").strip().lower() == "true" or "netlify" in form_attrs


def analyze(html_text):
    """回傳 {check_id: True/False}"""
    p = _Collector()
    try:
        p.feed(html_text)
        p.close()
    except Exception:  # 壞掉的 HTML 也盡量檢查
        pass
    css = "\n".join(p.style_parts)
    js = "\n".join(p.script_parts)
    r = {}

    r["l1_html"] = bool(RE_HTML.search(html_text))
    r["l1_charset"] = any(
        m.get("charset", "").strip().lower() in ("utf-8", "utf8")
        or (m.get("http-equiv", "").lower() == "content-type"
            and re.search(r"charset\s*=\s*utf-?8", m.get("content", ""), re.I))
        for m in p.metas)
    r["l1_viewport"] = any(
        m.get("name", "").strip().lower() == "viewport" and "width" in m.get("content", "").lower()
        for m in p.metas)
    r["l1_title"] = bool("".join(p.title_parts).strip())
    r["l1_h1"] = p.h1 > 0
    r["l1_cta"] = p.cta > 0
    r["l1_style"] = bool(css.strip()) or any(
        "stylesheet" in l.get("rel", "").lower().split() for l in p.links)
    r["l1_media"] = bool(RE_MEDIA.search(css))
    r["l1_img"] = not any(
        i.get("src", "").strip() and not EXTERNAL_SRC.match(i.get("src", "").strip())
        for i in p.imgs)

    # 第 2 關：優先找 Netlify 表單，沒有的話看第一個 form
    form = next((f for f in p.forms if _is_netlify(f["attrs"])), p.forms[0] if p.forms else None)
    fa = form["attrs"] if form else {}
    fields = form["fields"] if form else []
    form_name = fa.get("name", "").strip()
    r["l2_form"] = bool(form) and _is_netlify(fa)
    r["l2_form_name"] = bool(form_name)
    r["l2_hidden_form_name"] = bool(form_name) and any(
        t == "input" and a.get("type", "").lower() == "hidden"
        and a.get("name", "") == "form-name" and a.get("value", "").strip() == form_name
        for t, a in fields)
    data_fields = [
        a for t, a in fields
        if not (t == "input" and a.get("type", "").strip().lower() in SKIP_INPUT_TYPES)
        and a.get("name", "") != "form-name"
    ]
    r["l2_field_names"] = bool(data_fields) and all(a.get("name", "").strip() for a in data_fields)
    r["l2_email"] = any(t == "input" and a.get("type", "").strip().lower() == "email" for t, a in fields)
    hp = fa.get("netlify-honeypot", "").strip()
    r["l2_honeypot"] = bool(hp) and any(a.get("name", "") == hp for t, a in fields)

    r["l3_set"] = bool(RE_SET.search(js))
    r["l3_get"] = bool(RE_GET.search(js))
    r["l3_prevent"] = bool(RE_PREVENT.search(js))
    r["l3_fetch"] = bool(RE_FETCH.search(js))
    r["l3_urlencoded"] = bool(RE_URLENC.search(js))
    r["l3_logout"] = bool(RE_LOGOUT.search(js))
    return r


def build_report(html_text, level):
    res = analyze(html_text)
    checks, xp, max_xp = [], 0, 0
    for cid, lv, kind, title, hint in CHECKS:
        ok = res[cid]
        max_xp += XP[kind]
        xp += XP[kind] if ok else 0
        checks.append({"id": cid, "level": lv, "kind": kind, "pass": ok,
                       "title": title, "hint": None if ok else hint})
    levels = {}
    for lv, info in LEVELS.items():
        req = [c for c in checks if c["level"] == lv and c["kind"] == REQ]
        levels[str(lv)] = dict(info, badge=all(c["pass"] for c in req),
                               required_passed=sum(c["pass"] for c in req), required_total=len(req))
    ok = all(c["pass"] for c in checks if c["kind"] == REQ and c["level"] <= level)
    return {"tool": "VibeNTPU vibe_check", "level": level, "ok": ok,
            "xp": xp, "max_xp": max_xp, "levels": levels, "checks": checks}


def _mark(c):
    if c["pass"]:
        return "✅"
    return "❌" if c["kind"] == REQ else ("⚠️" if c["kind"] == WARN else "⬜")


KIND_LABEL = {REQ: "", WARN: "（建議）", BONUS: "（加分）"}


def format_text(rep, path):
    out = ["", "🩺 VibeNTPU 健檢報告", f"📄 檔案：{path}", f"🎯 檢查到第 {rep['level']} 關", ""]
    for lv in range(1, 4):
        info = rep["levels"][str(lv)]
        tag = "（本次檢查）" if lv <= rep["level"] else "（預習，不影響結果）"
        badge = "🏅 已點亮" if info["badge"] else f"{info['required_passed']}/{info['required_total']}"
        out.append(f"── Level {lv} {info['icon']} {info['name']} {tag}  [{badge}]")
        for c in rep["checks"]:
            if c["level"] != lv:
                continue
            out.append(f"  {_mark(c)} {c['id']:<20} {c['title']}{KIND_LABEL[c['kind']]}")
            if not c["pass"] and lv <= rep["level"]:
                out.append(f"       💡 {c['hint']}")
        out.append("")
    out.append(f"⭐ 經驗值 XP：{rep['xp']} / {rep['max_xp']}")
    if rep["ok"]:
        out.append(f"🎉 恭喜！第 {rep['level']} 關以內的必要項目全部通過！")
    else:
        out.append("💪 還差一步！沒過的項目都是升級的經驗值，照著 💡 提示跟 AI 說，再推一次就好。")
    return "\n".join(out)


def format_markdown(rep, path):
    out = ["## 🩺 VibeNTPU 健檢報告", "",
           f"- 📄 檔案：`{path}`", f"- 🎯 檢查到第 **{rep['level']}** 關",
           f"- ⭐ 經驗值：**{rep['xp']} / {rep['max_xp']} XP**", ""]
    out.append(("### 🎉 恭喜！必要項目全部通過！" if rep["ok"]
                else "### 💪 還差一步！沒過的項目都是升級的經驗值"))
    out.append("")
    for lv in range(1, 4):
        info = rep["levels"][str(lv)]
        tag = "" if lv <= rep["level"] else "（預習，不影響結果）"
        badge = "🏅 已點亮" if info["badge"] else f"{info['required_passed']}/{info['required_total']}"
        out += [f"#### Level {lv} {info['icon']} {info['name']} — {badge} {tag}", "",
                "| 結果 | 項目 | 提示 |", "| :-: | --- | --- |"]
        for c in rep["checks"]:
            if c["level"] != lv:
                continue
            hint = "" if c["pass"] else (c["hint"] or "").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")
            title = c["title"].replace("<", "&lt;").replace(">", "&gt;")
            out.append(f"| {_mark(c)} | {title}{KIND_LABEL[c['kind']]} `{c['id']}` | {hint} |")
        out.append("")
    return "\n".join(out)


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="VibeNTPU 健檢站：檢查你的 index.html")
    ap.add_argument("file", help="要檢查的 HTML 檔，例如 index.html")
    ap.add_argument("--level", type=int, choices=[1, 2, 3], default=1, help="檢查到第幾關（預設 1）")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--json", action="store_true", help="輸出 JSON")
    g.add_argument("--markdown", action="store_true", help="輸出 Markdown（給 GitHub Step Summary）")
    args = ap.parse_args(argv)
    try:
        with open(args.file, "r", encoding="utf-8-sig", errors="replace") as f:
            text = f.read()
    except OSError as e:
        print(f"❌ 讀不到檔案：{args.file}（{e.strerror}）。請確認 index.html 放在 repo 最外層。", file=sys.stderr)
        return 2
    rep = build_report(text, args.level)
    if args.json:
        print(json.dumps(dict(rep, file=args.file), ensure_ascii=False, indent=2))
    elif args.markdown:
        print(format_markdown(rep, args.file))
    else:
        print(format_text(rep, args.file))
    return 0 if rep["ok"] else 1


if __name__ == "__main__":
    sys.exit(main())
