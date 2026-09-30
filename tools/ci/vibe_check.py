#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
VibeNTPU 網站自我檢核工具（命令列／GitHub Actions 版）

僅使用 Python 標準函式庫，對 index.html 進行靜態檢查（不執行其中的程式碼），
確認是否符合各檢核點的技術要求。檢查項目與網頁版 tools/vibe_check.html 相同（check ID 一致）。

檢核等級：
    Level 1 部署基本要求（檢核點 3）：HTML 結構、編碼、viewport、標題、CTA、樣式
    Level 2 表單串接（檢核點 4）：Netlify Forms 所需的屬性與欄位
    Level 3 狀態保存（檢核點 5）：LocalStorage 讀寫、AJAX（fetch）送出

用法：
    python3 vibe_check.py index.html              # 檢查 Level 1（預設）
    python3 vibe_check.py index.html --level 3    # 檢查 Level 1 至 Level 3
    python3 vibe_check.py index.html --json       # 輸出 JSON
    python3 vibe_check.py index.html --markdown   # 輸出 Markdown（給 $GITHUB_STEP_SUMMARY）

結束代碼：--level 以內的必要項目全部通過 → 0；否則 → 1；讀檔失敗 → 2。
注意：靜態檢查只能確認程式碼「具備」某些寫法，無法保證實際部署後功能正確，仍須在瀏覽器實測。
"""
import argparse
import json
import re
import sys
from html.parser import HTMLParser

REQ, WARN, BONUS = "required", "warn", "bonus"
# 各類項目的配分（僅保留於 --json 的 xp / max_xp 欄位以維持輸出結構相容，文字報告不顯示）
WEIGHT = {REQ: 10, WARN: 5, BONUS: 5}

LEVELS = {
    1: {"icon": "L1", "name": "部署基本要求", "desc": "檢核點 3：可正確顯示於桌機與手機的形象首頁"},
    2: {"icon": "L2", "name": "表單串接", "desc": "檢核點 4：以 Netlify Forms（BaaS）收集早鳥名單"},
    3: {"icon": "L3", "name": "狀態保存", "desc": "檢核點 5：以 LocalStorage 保存會員狀態，並以 fetch 非同步送出表單"},
}

# (id, level, kind, 項目名稱, 未通過時的說明與「請向 AI 說明」提示) —— 與 vibe_check.html 的 CHECKS 保持一致
CHECKS = [
    ("l1_html", 1, REQ, "檔案為 HTML 文件",
     "檔案中找不到 <html> 或 <!DOCTYPE html>，請確認選取的是 index.html。請向 AI 說明：「請提供完整的 HTML 檔案，從 <!DOCTYPE html> 開始，不要省略任何段落」"),
    ("l1_charset", 1, REQ, "宣告 UTF-8 字元編碼",
     "未宣告編碼時，瀏覽器可能以錯誤編碼解讀中文而出現亂碼。請向 AI 說明：「請在 <head> 最前面加上 <meta charset=\"UTF-8\">」"),
    ("l1_viewport", 1, REQ, "設定 viewport（響應式設計的前提）",
     "缺少 viewport 時，手機瀏覽器會以約 980px 的虛擬寬度縮小顯示整頁。請向 AI 說明：「請在 <head> 加上 <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">」"),
    ("l1_title", 1, REQ, "設定網頁標題 <title>",
     "<title> 會顯示於瀏覽器分頁與搜尋結果，也是分享連結時的預設標題。請向 AI 說明：「請在 <head> 加上 <title>，內容為產品名稱與一句價值主張」"),
    ("l1_h1", 1, REQ, "設定主標題 <h1>",
     "<h1> 是頁面最重要的標題，影響可讀性、無障礙與搜尋引擎理解。請向 AI 說明：「請在主視覺區加上一個 <h1>，以一句話說明產品為誰解決什麼問題」"),
    ("l1_cta", 1, REQ, "具備行動呼籲按鈕（Call to Action, CTA）",
     "形象首頁的目的是引導訪客採取下一步行動。請向 AI 說明：「請在主視覺區加上一個明顯的行動按鈕（例如『加入早鳥名單』），使用 <a href> 或 <button>」"),
    ("l1_style", 1, REQ, "具備 CSS 樣式",
     "未套用樣式的頁面僅有瀏覽器預設排版，難以傳達產品定位。請向 AI 說明：「請以 <style> 為整個頁面設定配色、字體與版面，全部寫在同一個 index.html 中」"),
    ("l1_media", 1, WARN, "具備 @media 行動版樣式",
     "媒體查詢（media query）可依螢幕寬度調整版面。請向 AI 說明：「請加入 @media (max-width: 640px) 的行動版樣式，讓多欄版面在手機上改為單欄」"),
    ("l1_img", 1, WARN, "未引用可能不存在的本地圖片",
     "偵測到相對路徑的圖片（例如 photo.jpg）；若 repo 中沒有該檔案，部署後會顯示為破圖。請向 AI 說明：「請將圖片改為內嵌 SVG 或純 CSS 圖形，不要引用 repo 中不存在的圖片檔」"),
    ("l2_form", 2, REQ, "具備 Netlify 表單（data-netlify=\"true\"）",
     "Netlify 在部署時會掃描 HTML，只有帶此屬性的表單才會被註冊並接收資料。請向 AI 說明：「請加入早鳥名單表單，<form> 需包含 data-netlify=\"true\" 與 method=\"POST\"」"),
    ("l2_form_name", 2, REQ, "表單具有 name 屬性",
     "表單的 name 即 Netlify 後台 Forms 頁面中的表單名稱。請向 AI 說明：「請為 <form> 加上 name=\"waitlist\"」"),
    ("l2_hidden_form_name", 2, REQ, "具有隱藏欄位 form-name，且值與表單名稱相同",
     "Netlify 依據送出資料中的 form-name 判斷資料屬於哪一個表單；以 JavaScript 送出時尤其必要。請向 AI 說明：「請在 <form> 內加上 <input type=\"hidden\" name=\"form-name\" value=\"（與表單 name 相同）\">」"),
    ("l2_field_names", 2, REQ, "每個輸入欄位皆具有 name 屬性",
     "瀏覽器送出表單時只會包含具有 name 的欄位，缺少 name 的欄位資料不會傳到 Netlify。請向 AI 說明：「請確認表單中每個 input、select、textarea 都有 name 屬性」"),
    ("l2_email", 2, WARN, "具備 Email 欄位（type=\"email\"）",
     "type=\"email\" 可讓瀏覽器在送出前檢查格式，並在手機上顯示適合的鍵盤。請向 AI 說明：「請在表單加上 <input type=\"email\" name=\"email\" required>」"),
    ("l2_honeypot", 2, BONUS, "具備防垃圾訊息誘捕欄位（honeypot）",
     "誘捕欄位對一般使用者隱藏，自動程式若填寫即被判定為垃圾訊息。請向 AI 說明：「請在 <form> 加上 netlify-honeypot=\"bot-field\"，並加入一個隱藏的 <input name=\"bot-field\">」"),
    ("l3_set", 3, REQ, "使用 localStorage.setItem 寫入資料",
     "請向 AI 說明：「表單送出成功後，請以 localStorage.setItem 將使用者名稱儲存於瀏覽器」"),
    ("l3_get", 3, REQ, "使用 localStorage.getItem 讀取資料",
     "請向 AI 說明：「頁面載入時，請以 localStorage.getItem 檢查是否已有儲存的名稱；若有，顯示會員歡迎畫面並隱藏表單」"),
    ("l3_prevent", 3, REQ, "使用 preventDefault 取消預設送出行為",
     "表單預設送出會讓瀏覽器導向新頁面，導致無法在同一頁更新畫面。請向 AI 說明：「表單送出時，請先呼叫 event.preventDefault()，改由 JavaScript 處理」"),
    ("l3_fetch", 3, REQ, "使用 fetch() 以非同步方式（AJAX）送出表單",
     "請向 AI 說明：「請以 fetch('/', { method: 'POST', ... }) 在背景將表單資料送至 Netlify，成功後再更新畫面」"),
    ("l3_urlencoded", 3, REQ, "送出格式為 application/x-www-form-urlencoded",
     "Netlify Forms 接收的是一般表單編碼格式，而非 JSON。請向 AI 說明：「fetch 的 headers 請設定 'Content-Type': 'application/x-www-form-urlencoded'，body 使用 new URLSearchParams(new FormData(form)).toString()」"),
    ("l3_logout", 3, BONUS, "具備登出功能（removeItem 或 clear）",
     "請向 AI 說明：「請在會員畫面加入登出按鈕，按下後以 localStorage.removeItem 刪除已儲存的資料並重新顯示表單」"),
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

    # Level 2：優先找 Netlify 表單，沒有的話看第一個 form
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
        max_xp += WEIGHT[kind]
        xp += WEIGHT[kind] if ok else 0
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
        return "[通過]"
    return {REQ: "[未通過]", WARN: "[建議]", BONUS: "[加分]"}[c["kind"]]


KIND_LABEL = {REQ: "", WARN: "（建議項目）", BONUS: "（加分項目）"}


def _req_summary(rep):
    req = [c for c in rep["checks"] if c["kind"] == REQ and c["level"] <= rep["level"]]
    return sum(c["pass"] for c in req), len(req)


def format_text(rep, path):
    passed, total = _req_summary(rep)
    out = ["", "VibeNTPU 網站自我檢核報告", f"檔案：{path}",
           f"檢核範圍：Level 1 至 Level {rep['level']}", ""]
    for lv in range(1, 4):
        info = rep["levels"][str(lv)]
        tag = "" if lv <= rep["level"] else "（預覽，不影響結果）"
        status = "全部通過" if info["badge"] else "尚未完成"
        out.append(f"== Level {lv} {info['name']}{tag}  必要項目 {info['required_passed']}/{info['required_total']} 通過，{status}")
        for c in rep["checks"]:
            if c["level"] != lv:
                continue
            m = _mark(c)
            pad = " " * (9 - len(m) - sum(1 for ch in m if ord(ch) > 0x2E80))  # 以顯示寬度對齊
            out.append(f"  {m}{pad}{c['id']:<20} {c['title']}{KIND_LABEL[c['kind']]}")
            if not c["pass"] and lv <= rep["level"]:
                out.append(f"           提示：{c['hint']}")
        out.append("")
    out.append(f"必要項目 {passed}/{total} 通過（Level 1 至 Level {rep['level']}）")
    if rep["ok"]:
        out.append(f"結果：Level {rep['level']} 以內的必要項目全部通過。")
    else:
        out.append("結果：尚有必要項目未通過。請依各項「提示」修改 index.html，Commit 並 Sync 後重新檢核。")
    return "\n".join(out)


def _md_escape(s):
    return (s or "").replace("|", "\\|").replace("<", "&lt;").replace(">", "&gt;")


def format_markdown(rep, path):
    passed, total = _req_summary(rep)
    out = ["## VibeNTPU 網站自我檢核報告", "",
           f"- 檔案：`{path}`", f"- 檢核範圍：Level 1 至 Level **{rep['level']}**",
           f"- 必要項目：**{passed}/{total}** 通過", ""]
    out.append(("**結果：必要項目全部通過。**" if rep["ok"]
                else "**結果：尚有必要項目未通過。** 請依下表說明修改後重新 Commit 並 Sync。"))
    out.append("")
    for lv in range(1, 4):
        info = rep["levels"][str(lv)]
        tag = "" if lv <= rep["level"] else "（預覽，不影響結果）"
        status = "全部通過" if info["badge"] else f" {info['required_passed']}/{info['required_total']} 通過"
        out += [f"### Level {lv} {info['name']}：必要項目{status} {tag}".rstrip(), "",
                "| 狀態 | 項目 | 說明 |", "| :-: | --- | --- |"]
        for c in rep["checks"]:
            if c["level"] != lv:
                continue
            hint = "" if c["pass"] else _md_escape(c["hint"])
            out.append(f"| {_mark(c)} | {_md_escape(c['title'])}{KIND_LABEL[c['kind']]} `{c['id']}` | {hint} |")
        out.append("")
    return "\n".join(out)


def main(argv=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except Exception:
            pass
    ap = argparse.ArgumentParser(description="VibeNTPU 網站自我檢核工具：靜態檢查 index.html")
    ap.add_argument("file", help="要檢查的 HTML 檔，例如 index.html")
    ap.add_argument("--level", type=int, choices=[1, 2, 3], default=1, help="檢核至第幾個 Level（預設 1）")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--json", action="store_true", help="輸出 JSON")
    g.add_argument("--markdown", action="store_true", help="輸出 Markdown（給 GitHub Step Summary）")
    args = ap.parse_args(argv)
    try:
        with open(args.file, "r", encoding="utf-8-sig", errors="replace") as f:
            text = f.read()
    except OSError as e:
        print(f"[錯誤] 無法讀取檔案：{args.file}（{e.strerror}）。請確認 index.html 位於 repo 根目錄。", file=sys.stderr)
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
