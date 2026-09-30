# 第 1 週一頁版步驟清單

上課時開著本頁，做完一項勾一項。每一步的詳細說明、畫面位置和「如果不一樣」怎麼辦，請看 [第 1 週手把手實作](README.md) 同一個步驟編號。

---

## 上課前（檢核點 0）

- [ ] VS Code 左下角帳戶圖示看得到我的 GitHub 帳號
- [ ] Copilot 已啟用，Live Preview 已安裝
- [ ] 已用 GitHub 帳號登入 Netlify
- [ ] 筆電有電、手機在身上

## Part 0：開場示範（0:00，5 分鐘）

- [ ] 步驟 1：看老師示範，用手機掃 QR Code 打開網站
- [ ] 步驟 2：在 [學習單](worksheet.md) 第 1 題寫下預測

## Part 1：認識 SaaS 架構（0:05，30 分鐘）

- [ ] 步驟 3：下載課程 ZIP，雙擊 `slides/social_saas.html`
- [ ] 步驟 4：在 **1. 分層架構圖** 點選 **手機 App**、**內容傳遞網路**、**推薦系統**、**推播服務**，再按 **對照 MVP 架構**
- [ ] 步驟 5：在 **2. 請求流程演示** 點 **按讚**，按 **下一步 →** 看完全部，共 ＿＿ 步
- [ ] 步驟 6：看懂講義中的簡單架構圖
- [ ] 步驟 7：打開 `foodcourt.html`，拖動拉桿，按 **播放資料流**
- [ ] 步驟 8：在 **3. 商業模式與測驗** 完成測驗，答對 80% 以上（檢核點 1）

## Part 2：GitHub 建 repo 並 clone（0:35，20 分鐘）

- [ ] 步驟 9：到 <https://github.com/new>，名稱輸入 `rent-radar`（或你的名稱），選 **Public**，打開 **Add README**，按 **Create repository**
- [ ] 步驟 10：VS Code 左側點 **原始檔控制（Source Control）**
- [ ] 步驟 11：按 **複製存放庫（Clone Repository）** → **從 GitHub 複製（Clone from GitHub）** → 選 repo → 選資料夾 → **選取為存放庫目的地** → **開啟（Open）**
- [ ] 步驟 12：確認檔案總管有 `README.md`
- [ ] 交換駕駛與導航員

## Part 3：用 Copilot 做網頁（0:55，35 分鐘）

- [ ] 步驟 13：決定題目：＿＿＿＿＿＿＿＿＿＿
- [ ] 步驟 14：打開 `prompt_builder.html`，選 **GitHub Copilot（VS Code）**，填到完整度 100%，按 **複製提示詞**
- [ ] 步驟 15：`Ctrl+Alt+I`（macOS：`⌃⌘I`）打開 Copilot Chat，選 **Agent**，貼上送出；要求執行指令時選 **略過（Skip）**
- [ ] 步驟 16：確認只改了 `index.html`，按 **保留（Keep）**
- [ ] 步驟 17：`index.html` 按右鍵 → **顯示預覽（Show Preview）**
- [ ] 步驟 18：用 [prompts.md](prompts.md) 的修改提示詞改一次，再按 **保留（Keep）**
- [ ] 步驟 19：用瀏覽器開發者工具（`F12`）檢查手機寬度（檢核點 2）
- [ ] 交換駕駛與導航員

## Part 4：提交、同步、Netlify 上線（1:30，25 分鐘）

- [ ] 步驟 20：**原始檔控制** → 訊息輸入 `新增第一版首頁` → **提交（Commit）** → 詢問時按 **是（Yes）**
- [ ] 步驟 21：按 **同步變更（Sync Changes）** → **確定（OK）**；到 GitHub 重新整理，看到 `index.html`
- [ ] 步驟 22：<https://app.netlify.com/> → **Add new project** → **Import an existing project** → **GitHub** → 選 repo
- [ ] 步驟 23：Build command、Publish directory 留空 → **Deploy** → 等到 **Published**
- [ ] 步驟 24（可跳過）：**Project configuration** → **General** → **Project details** → **Change project name** → **Save**
- [ ] 步驟 25：手機打開網址，貼到課程群組；[網站自我檢核工具](../../tools/vibe_check.html) Level 1 全部通過（檢核點 3）

我的網址：`https://＿＿＿＿＿＿＿＿.netlify.app`

## Part 5：收尾（1:55，5 分鐘）

- [ ] 步驟 26：看一位同學的網站，用「我喜歡／我希望／如果」回饋一則
- [ ] 步驟 27：完成 [學習單](worksheet.md) 第 5 部分
- [ ] 課後：把 [學習歷程檔案範本](../../templates/portfolio_README.md) 貼進 repo 的 `README.md`，提交並同步

---

卡住時：先查 [疑難排解手冊](../../docs/tutorials/error_guide.md)；同一個問題 15 分鐘沒進展，請舉手或貼紅色便利貼。
