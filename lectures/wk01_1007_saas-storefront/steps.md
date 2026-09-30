# 第 1 週｜一頁版步驟卡 📋

> 上課請開著這一頁，**做完一步就打勾（或用手指點一下）**。
> 🧭 領航員負責念步驟，🚗 駕駛負責操作。每個段落結束交換，**兩個人都要在自己電腦完成**！
> 看不懂某一步？點旁邊的 📖 連結看詳細說明。

[← 回第 1 週講義](README.md)

---

## 段落 1：看懂 SaaS 架構

- [ ] 打開 [social_saas.html](slides/social_saas.html)（社群媒體的 SaaS 架構）
- [ ] 分頁①：從上到下看一次架構圖，點 3 個你好奇的方塊
- [ ] 分頁②：播放「❤️ 在 IG 按讚」，數數看經過幾個服務：＿＿ 個
- [ ] 分頁①：打開「🔍 對照我們的 MVP」開關
- [ ] 打開 [foodcourt.html](slides/foodcourt.html)：拉月數拉桿、播放資料流
- [ ] 完成任一個小測驗，答對 4 題以上 → 🧠 **Q1 過關！**

## 段落 2：打開總部保險箱（GitHub）

### 2.1 先玩模擬器 🎮
- [ ] 打開 [git_flow.html](slides/git_flow.html)，完成一次：修改 → Stage → Commit → Sync

### 2.2 建 repo ☁️ 📖 [詳細說明](../../docs/tutorials/git_intro.md#步驟-1在-github-建立你的-repo-)
- [ ] 打開 <https://github.com/new>
- [ ] Repository name 填英文小寫，例如 `rent-radar`
- [ ] 選 **Public**
- [ ] ✅ 勾選 **Add a README file**
- [ ] 按綠色 **Create repository**

### 2.3 Clone 到電腦 💻 📖 [詳細說明](../../docs/tutorials/git_intro.md#步驟-2把-repo-複製到你的電腦clone)
- [ ] VS Code → 左側 **原始檔控制**（`Ctrl+Shift+G`／`⌃⇧G`）
- [ ] 按 **複製存放庫（Clone Repository）** → **從 GitHub 複製**
- [ ] （第一次）瀏覽器授權 GitHub
- [ ] 選 `你的帳號/rent-radar`
- [ ] 選一個資料夾存放 → 右下角按 **開啟（Open）**
- [ ] 左側檔案總管看到 `README.md` ✅
- [ ] 🔄 **交換駕駛／領航員**

## 段落 3：用 Copilot 詠唱店面

- [ ] 決定創業題目：＿＿＿＿＿＿＿＿＿＿
- [ ] 打開 [咒語產生器](slides/prompt_builder.html)，AI 選 **GitHub Copilot**，填好欄位，健康度到 100%
- [ ] 按「📋 複製咒語」
- [ ] 確認 VS Code 左側開的是**剛 clone 的 repo 資料夾**（上方看得到 repo 名稱）
- [ ] 打開 Copilot Chat（`Ctrl+Alt+I`／`⌃⌘I`）→ 模式選 **Agent**
- [ ] 貼上咒語 → 送出 → 等 Copilot 完成
- [ ] 看一下變更 → 按 **Keep（保留）**
- [ ] 左側出現 `index.html`（旁邊有綠色 **U**）
- [ ] 在 `index.html` 上按右鍵 → **Show Preview**（或雙擊用瀏覽器打開）→ 🎨 **Q2 過關！**
- [ ] 至少請 Copilot 修改一次，讓它更像你心中的樣子（記得 **Keep**）
- [ ] 🔄 **交換駕駛／領航員**

## 段落 4：存檔、上雲、開店

### 4.1 Commit ＋ Sync 💾 📖 [詳細說明](../../docs/tutorials/git_intro.md#步驟-4存檔點stage--commit)
- [ ] 打開 **原始檔控制** 面板（圖示上有數字）
- [ ] 訊息框輸入：`第一版首頁`
- [ ] 按 **✓ 提交（Commit）**（問要不要全部暫存 → 按 **是**）
- [ ] 按藍色 **同步變更（Sync Changes）↑1** → 問「推送和提取」按 **確定**
- [ ] 到 GitHub 網頁重新整理 repo，看到 `index.html` 和你的訊息 ✅

### 4.2 Netlify：租一個攤位 ☁️ 📖 [詳細說明](../../docs/tutorials/github_netlify_deploy.md#part-b到美食街擺攤位netlify)
- [ ] 打開 <https://app.netlify.com/>（用 GitHub 登入）
- [ ] 點 **Add new project** → **Import an existing project**
- [ ] 選 **GitHub** → 授權（Authorize Netlify）
- [ ] 選你的 repo
- [ ] Build command、Publish directory **都留空**
- [ ] Project name 填好記的名字，例如 `ntpu-rent-radar-123`
- [ ] 按 **Deploy**，等狀態變成 **Published** 🎉

### 4.3 驗收 🌍
- [ ] 點網址，電腦上打得開
- [ ] 用 LINE 傳給自己，**手機**也打得開
- [ ] 網址貼到課程群組
- [ ] 打開 [Vibe 健檢站](../../tools/vibe_check.html)，選你 repo 資料夾裡的 `index.html`，Level 1 全亮 → 🏪 **Q3 過關！**

## 段落 5：收尾

- [ ] 逛隔壁組網站，給一句「我喜歡／我希望／如果」
- [ ] 完成 [學習單](worksheet.md) 的出場券
- [ ] （回家也可以）把 [冒險護照](../../templates/passport_README.md) 貼進 repo 的 `README.md` → Commit ＋ Sync

---

😵 卡關了？👉 [卡關急救手冊](../../docs/tutorials/error_guide.md)　｜　⏱️ 15 分鐘沒進展就貼紅色便利貼！
