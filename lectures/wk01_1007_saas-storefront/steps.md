# 第 1 週操作步驟卡

上課時請開啟本頁，完成一項即勾選一項。導航員朗讀步驟並檢查畫面，駕駛負責操作；每個段落結束後交換角色，兩人都須在自己的電腦完成。各步驟的完整說明請見連結的教學文件。

[← 回第 1 週講義](README.md)

---

## 1. 段落 1：架構理解（檢核點 1）

- [ ] 開啟 [social_saas.html](slides/social_saas.html)，在架構圖分頁由上而下瀏覽，點選三個元件閱讀說明。
- [ ] 在操作流程分頁播放「按讚」，記錄經過的服務數量：＿＿ 個。
- [ ] 在架構圖分頁開啟 MVP 對照功能。
- [ ] 開啟 [foodcourt.html](slides/foodcourt.html)，拖動月數拉桿，並播放資料流。
- [ ] 完成任一份架構互動測驗，答對 80% 以上。

## 2. 段落 2：建立 repo 並複製到本機

### 2.1 模擬器

- [ ] 開啟 [git_flow.html](slides/git_flow.html)，完成一次「修改 → Stage → Commit → Sync」。

### 2.2 建立 repo（說明：[Git 與 GitHub 入門](../../docs/tutorials/git_intro.md)）

- [ ] 開啟 <https://github.com/new>。
- [ ] Repository name 使用英文小寫與連字號，例如 `rent-radar`。
- [ ] 選擇 **Public**。
- [ ] 勾選 **Add a README file**。
- [ ] 按 **Create repository**。

### 2.3 複製到本機（Clone）

- [ ] VS Code 左側開啟 **原始檔控制**（`Ctrl+Shift+G`／`⌃⇧G`）。
- [ ] 按 **複製存放庫（Clone Repository）** → **從 GitHub 複製**。
- [ ] 首次使用時，於瀏覽器完成 GitHub 授權。
- [ ] 選擇 `你的帳號/rent-radar`。
- [ ] 選擇存放資料夾，並在右下角提示中按 **開啟（Open）**。
- [ ] 確認檔案總管中出現 `README.md`。
- [ ] 交換駕駛與導航員。

## 3. 段落 3：以 Copilot 建立前端（檢核點 2）

- [ ] 決定創業題目：＿＿＿＿＿＿＿＿＿＿
- [ ] 開啟 [提示產生器](slides/prompt_builder.html)，AI 工具選擇 **GitHub Copilot**，填寫欄位至完整度 100%。
- [ ] 按複製。
- [ ] 確認 VS Code 左側開啟的是剛才 clone 的 repo 資料夾。
- [ ] 開啟 Copilot Chat（`Ctrl+Alt+I`／`⌃⌘I`），模式選擇 **Agent**。
- [ ] 貼上提示並送出，等待 Copilot 完成。
- [ ] 若 Copilot 提議執行終端機指令，選擇略過（Skip）。
- [ ] 檢視差異，確認只新增 `index.html`，按 **Keep**。
- [ ] 確認檔案總管中出現 `index.html`（旁邊標示綠色 **U**，表示尚未追蹤的新檔案）。
- [ ] 在 `index.html` 上按右鍵 → **Show Preview**（或以瀏覽器開啟）。
- [ ] 至少提出一次修改要求（參考 [提示 2](prompts.md#53-提示-2迭代修改agent-模式)），檢視差異後按 **Keep**。
- [ ] 以手機寬度檢查版面，並確認開發者工具 Console 沒有錯誤（[驗證清單](prompts.md#3-ai-輸出的驗證清單)）。
- [ ] 交換駕駛與導航員。

## 4. 段落 4：提交、同步與 Netlify 部署（檢核點 3）

### 4.1 Commit 與 Sync（說明：[Git 與 GitHub 入門](../../docs/tutorials/git_intro.md)）

- [ ] 開啟 **原始檔控制** 面板（圖示上顯示變更數量）。
- [ ] 在訊息框輸入：`新增第一版首頁`。
- [ ] 按 **提交（Commit）**；若詢問是否暫存所有變更，選擇 **是**。
- [ ] 按 **同步變更（Sync Changes）↑1**；詢問推送與提取時選擇 **確定**。
- [ ] 在 GitHub 網頁重新整理 repo，確認出現 `index.html` 與提交訊息。

### 4.2 Netlify 部署（說明：[部署教學](../../docs/tutorials/github_netlify_deploy.md)）

- [ ] 開啟 <https://app.netlify.com/>，以 GitHub 帳號登入。
- [ ] 點選 **Add new project** → **Import an existing project**。
- [ ] 選擇 **GitHub**，完成授權（Authorize Netlify）。
- [ ] 選擇你的 repo。
- [ ] Build command 與 Publish directory 皆留空。
- [ ] Project name 填入易辨識的名稱，例如 `ntpu-rent-radar-123`。
- [ ] 按 **Deploy**，等待狀態顯示 **Published**。

### 4.3 驗收

- [ ] 在電腦上開啟網址，頁面正常顯示。
- [ ] 將網址傳到自己的手機，確認手機也能開啟且版面正常。
- [ ] 將網址貼到課程群組。
- [ ] 開啟 [網站自我檢核工具](../../tools/vibe_check.html)，選擇 repo 資料夾中的 `index.html`，確認 Level 1 全部通過。

## 5. 段落 5：收尾

- [ ] 瀏覽至少一組同學的網站，以「我喜歡／我希望／如果」提供一則回饋。
- [ ] 完成 [學習單](worksheet.md) 第 5 部分（出場券）。
- [ ] 課後：將 [學習歷程檔案範本](../../templates/portfolio_README.md) 貼入 repo 的 `README.md`，Commit 並 Sync。

---

遇到問題時：先查閱 [疑難排解手冊](../../docs/tutorials/error_guide.md)；同一問題 15 分鐘無進展，請貼紅色便利貼請求協助。
