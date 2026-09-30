# 課程工具（tools/）

[← 回課程首頁](../README.md)

本資料夾收錄學生自我檢核與課程 repo 維護所用的工具。所有程式均只使用瀏覽器原生功能或 Python 標準函式庫，不需安裝額外套件。

## 1. 工具一覽

| 工具 | 使用者 | 用途 |
| --- | --- | --- |
| [vibe_check.html](vibe_check.html) | 學生 | **網站自我檢核工具**（瀏覽器版）：載入 `index.html` 後逐項檢查 Level 1–3 的技術要求，並對未通過項目提供修改建議；完成後可產生完課證明。檔案只在本機瀏覽器中分析，不會上傳。 |
| [ci/vibe_check.py](ci/vibe_check.py) | 教師、進階學生 | 自我檢核的命令列版本，檢查項目與瀏覽器版相同，可輸出文字、JSON 或 Markdown，適合批次檢核與 CI |
| [ci/vibe-check.yml](ci/vibe-check.yml) | 學生（延伸任務） | GitHub Actions 工作流程範本，放入學生自己的 repo 後，每次推送即自動執行自我檢核；教學見 [vibe_check_ci.md](../docs/tutorials/vibe_check_ci.md) |
| [ci/check_links.py](ci/check_links.py) | 教材維護者 | 檢查 repo 內所有 Markdown 檔的相對連結與標題錨點是否存在 |
| [ci/check_emoji.py](ci/check_emoji.py) | 教材維護者 | 檢查教材（`.md`、`.html`、`.yml`、`.yaml`、`.py`）是否含有 emoji |

`check_links.py` 與 `check_emoji.py` 由課程 CI（[.github/workflows/course-check.yml](../.github/workflows/course-check.yml)）於每次推送時自動執行；該工作流程同時以 `vibe_check.py` 驗證三份示範作品的檢核結果是否符合預期。

## 2. 網站自我檢核工具

### 2.1 檢核等級與項目

每個項目分為三類：**必要**（未通過即該等級未完成）、**建議**（不影響結果，但會影響品質）、**加分**（進階做法）。

| 等級 | 名稱 | 對應檢核點 | 必要項目 | 建議與加分項目 |
| --- | --- | --- | --- | --- |
| Level 1 | 部署基本要求 | 檢核點 3 | HTML 文件結構、`<meta charset="UTF-8">`、viewport 設定、`<title>`、`<h1>`、行動呼籲（CTA）按鈕或連結、CSS 樣式 | 建議：`@media` 行動版樣式；未引用 repo 中不存在的本機圖片 |
| Level 2 | 表單串接 | 檢核點 4 | 含 `data-netlify="true"` 的表單、表單 `name` 屬性、隱藏欄位 `form-name` 且值與表單名稱一致、每個輸入欄位都有 `name` | 建議：`type="email"` 欄位；加分：honeypot 防機器人欄位 |
| Level 3 | 狀態保存 | 檢核點 5 | `localStorage.setItem` 與 `getItem`、`preventDefault()`、以 `fetch()` 非同步送出、`application/x-www-form-urlencoded` 格式 | 加分：登出功能（`removeItem` 或 `clear`） |

瀏覽器版與命令列版使用相同的檢查 ID（例如 `l1_viewport`、`l2_hidden_form_name`、`l3_fetch`），結果一致。

### 2.2 運作方式與限制

檢核工具以**靜態分析**解析 HTML 結構並以規則比對 JavaScript 寫法，不會執行網頁程式碼，也不會連線到 Netlify。因此：

- 通過檢核代表程式碼「具備」必要的寫法，**不代表**網站已部署、表單已收件或功能在瀏覽器中正確運作。檢核點 3–6 仍須以公開網址與平台紀錄驗證。
- 以不同寫法達成相同功能時（例如以其他方式送出表單），可能被判定為未通過；此時應以實際運作為準。
- 工具不評估內容品質、設計或可及性，這些由 [評分規準](../docs/course_plan.md#4-分析式評分規準) 人工評閱。

## 3. 命令列版本（vibe_check.py）

### 3.1 用法

```bash
python3 tools/ci/vibe_check.py index.html              # 檢查 Level 1（預設）
python3 tools/ci/vibe_check.py index.html --level 3    # 檢查 Level 1 至 Level 3
python3 tools/ci/vibe_check.py index.html --json       # 輸出 JSON（批次處理用）
python3 tools/ci/vibe_check.py index.html --markdown   # 輸出 Markdown（寫入 GitHub Actions Summary 用）
```

### 3.2 輸出

- **文字報告**：每一項以文字標記顯示狀態：`[通過]`、`[未通過]`（必要項目）、`[建議]`、`[加分]`，未通過項目附修改提示，最後彙總必要項目通過數。
- **JSON**：包含 `level`、`ok`、各等級摘要 `levels`，以及每一項的 `id`、`level`、`kind`、`pass` 等欄位。其中 `xp`、`max_xp` 欄位僅為相容舊版輸出結構而保留，課程中不使用。
- **結束代碼**：指定等級以內的必要項目全部通過為 `0`；有未通過項目為 `1`；讀檔失敗為 `2`。CI 以此判斷成功或失敗。

教師批次檢核全班作業的方式見 [教師備課指南](../docs/teacher_guide.md#52-批次自我檢核)。

## 4. GitHub Actions 範本（vibe-check.yml）

學生將 [ci/vibe-check.yml](ci/vibe-check.yml) 放入自己 repo 的 `.github/workflows/` 後，每次推送會在 GitHub 提供的虛擬機上：

1. 取得 repo 內容（`actions/checkout`）；
2. 安裝 Python；
3. 從課程 repo 下載最新版 `vibe_check.py`；
4. 將 Markdown 報告寫入 Actions 的 Summary 頁面；
5. 以檔案開頭的 `LEVEL` 變數指定的等級執行檢核，未通過時該次執行標示為失敗。

此範本是持續整合（Continuous Integration, CI）的最小示例：每次修改都由自動化程序檢查，而非依賴人工記得檢查。工作流程僅要求 `contents: read` 權限。安裝步驟見 [vibe_check_ci.md](../docs/tutorials/vibe_check_ci.md)。

## 5. 教材維護工具

### 5.1 check_links.py

```bash
python3 tools/ci/check_links.py
```

走訪 repo 內所有 `.md` 檔，檢查相對連結的目標檔案是否存在；若連結帶有 `#錨點` 且目標為 Markdown，依 GitHub 的標題錨點產生規則檢查該錨點是否存在。外部網址（`https://` 等）不檢查。有壞連結時結束代碼為 `1`。

維護建議：改寫標題會改變錨點。連到他人維護的檔案時，宜只連到檔案本身，避免錨點因標題改寫而失效。

### 5.2 check_emoji.py

```bash
python3 tools/ci/check_emoji.py                 # 檢查整個 repo
python3 tools/ci/check_emoji.py README.md docs/ # 檢查指定檔案或資料夾
```

檢查 `.md`、`.html`、`.yml`、`.yaml`、`.py` 檔案中是否含有 emoji，列出檔案與行號；發現時結束代碼為 `1`。方向箭頭（← → ↑ ↓）與 macOS 按鍵符號（⌘ ⌥ ⌃ ⇧）不視為 emoji。此檢查用於維持教材的正式書寫風格。

## 6. 示範作品的預期結果

| 示範作品 | 預期結果 |
| --- | --- |
| [samples/LOW](../samples/LOW/index.html) | 通過 Level 1 |
| [samples/MEDIUM](../samples/MEDIUM/index.html) | 通過 Level 1，不通過 Level 2 |
| [samples/HIGH](../samples/HIGH/index.html) | 通過 Level 1–3 |

以上由課程 CI 自動驗證，可用於確認檢核工具修改後仍能正確區分三個等級。示範作品的評語見 [samples/README.md](../samples/README.md)。
