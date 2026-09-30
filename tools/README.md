# 🧰 課程工具（tools/）

[← 回課程首頁](../README.md)

| 工具 | 給誰 | 用途 |
| --- | --- | --- |
| [vibe_check.html](vibe_check.html) | 同學 | 🩺 **Vibe 健檢站**：把你的 `index.html` 丟進去，看看哪些徽章亮了；每個沒過的項目都會告訴你「請跟 AI 說什麼」。主線全破可以列印 🎓 完課證書。**只在你的瀏覽器裡檢查，檔案不會上傳。** |
| [ci/vibe_check.py](ci/vibe_check.py) | 同學（進階）／老師 | 同一套檢查的 Python 版本（只用標準函式庫）：`python3 vibe_check.py index.html --level 2`，可加 `--json`、`--markdown` |
| [ci/vibe-check.yml](ci/vibe-check.yml) | 同學（支線 🤖） | GitHub Actions 範本：放進自己的 repo，每次上傳就自動健檢，拿綠色勾勾 ✅。教學見 [vibe_check_ci.md](../docs/tutorials/vibe_check_ci.md) |
| [ci/check_links.py](ci/check_links.py) | 老師 | 檢查本 repo 所有 Markdown 的內部連結與錨點（由 `.github/workflows/course-check.yml` 自動執行） |

## 🩺 健檢項目

| 等級 | 徽章 | 檢查 |
| --- | --- | --- |
| Level 1 | 🏪 開店 | 是 HTML、UTF-8、viewport（手機）、有標題、有 `<h1>`、有 CTA 按鈕、有 CSS；建議：`@media`、不引用本機圖片 |
| Level 2 | 📦 收單 | 有 `data-netlify` 表單、表單有 `name`、隱藏 `form-name` 欄位相符、每個欄位都有 `name`；建議：Email 欄位；加分：honeypot |
| Level 3 | 💾 記憶 | `localStorage.setItem`／`getItem`、`preventDefault`、`fetch`、urlencoded 格式；加分：登出 |

`vibe_check.html` 與 `vibe_check.py` 使用相同的檢查 ID，結果一致。三份 [示範作品](../samples/README.md) 的預期結果：LOW／MEDIUM 通過 Level 1，HIGH 通過 Level 1–3（由課程 CI 自動驗證）。
