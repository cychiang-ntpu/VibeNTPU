# ☁️ 組裝 SaaS 第一步：GitHub 存檔 ＋ Netlify 部署

> 這一頁帶你把 VS Code 裡的 `index.html`，變成全世界都能打開的網址。
> 全程只需要**點按鈕**：VS Code 的 Commit／Sync ＋ Netlify 網頁上的幾個按鈕。

[← 回第 1 週](../../lectures/wk01_1007_saas-storefront/README.md)　｜　[教學目錄](README.md)

> 📝 GitHub、VS Code 與 Netlify 的介面偶爾會改版，按鈕位置可能跟下面描述略有不同。找不到按鈕時，請對照官方文件：
> [VS Code：Git 入門](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git)｜[Netlify：從 Git 儲存庫部署](https://docs.netlify.com/start/quickstarts/deploy-from-repository/)

---

## Part A：把設計圖存進總部保險箱（GitHub）🗄️

> 詳細圖文與觀念 👉 [Git 與 GitHub 入門](git_intro.md)。這裡是濃縮版。

1. **建 repo**：到 <https://github.com/new>，名稱如 `rent-radar`，選 **Public**，✅ 勾 **Add a README file** → **Create repository**。
2. **Clone**：VS Code → 左側 **原始檔控制**（`Ctrl+Shift+G`／`⌃⇧G`）→ **複製存放庫** → **從 GitHub 複製** → 選你的 repo → 選資料夾 → **開啟**。
3. **做網頁**：請 Copilot 在這個資料夾建立 `index.html`，按 **Keep**。
4. **Commit**：原始檔控制面板 → 訊息框寫 `第一版首頁` → **✓ 提交**（問要不要全部暫存就按 **是**）。
5. **Sync**：按 **同步變更（Sync Changes）↑1**。
6. **確認**：到 GitHub 網頁重新整理 repo，看到 `index.html` ✅

> ⚠️ 檔名一定要是 **`index.html`**，而且放在 repo 的**最外層**（不是在資料夾裡）。Netlify 會自動把這個檔案當作「首頁」，檔名不對就會出現 `Page not found`。

---

## Part B：到美食街擺攤位（Netlify）☁️

### B1. 從 GitHub 匯入專案

1. 登入 <https://app.netlify.com/>（選 **Log in with GitHub**）。
2. 在首頁找到 **「Add new project」**（舊版介面叫「Add new site」）→ **「Import an existing project」**。
3. 選擇 **「GitHub」**。
4. 第一次使用時，會跳出 GitHub 授權視窗：
   - 按 **「Authorize Netlify」**。
   - 接著安裝 Netlify App：可以選 **「All repositories」**，或只選 **「Only select repositories」** 並勾選你剛建立的 repo（比較安全 👍）。
5. 在列表中點選你的 repo（例如 `rent-radar`）。

### B2. 設定並部署

1. 設定畫面的欄位 **全部維持預設/空白** 即可：
   - Branch to deploy：`main`
   - Build command：**留空**（我們只有一個 HTML 檔，不需要「建置」）
   - Publish directory：**留空**
2. 幫專案取名（Project name），這會變成你的網址，例如輸入 `ntpu-rent-radar` → 網址就是 `https://ntpu-rent-radar.netlify.app`。
   > 名字要全世界唯一，被用走了就換一個，例如加上你的學號末三碼。
3. 按下 **「Deploy」**。
4. 等待約 10～30 秒，狀態變成 **「Published」** 就完成了！🎉

### B3. （如果剛剛沒取名）更改網址

預設網址會長得像 `https://jolly-pony-123abc.netlify.app` 這種亂碼。
在專案首頁（Project overview）點 **Customize** → **Manage project name and cover image**；或到 **Project configuration** → **General** → **Project details** → **Manage project name and cover image**，改成好記的名字即可。

📖 官方說明：[Netlify：更改專案名稱](https://docs.netlify.com/manage/projects/customize-project-name-and-cover-image/)

📖 延伸學習：[Netlify：更改網站名稱／網域](https://docs.netlify.com/manage/domains/get-started-with-domains/)（想要 `.com` 自訂網域的同學可以研究）

---

## Part C：驗收 🌍

1. 點擊 Netlify 上的網址，確認網站可以打開。
2. **用手機**打開同一個網址（可以用 LINE 傳給自己）。
3. 把網址貼到課程群組，互相逛逛同學的店面！

> 🏗️ **架構呼應**：恭喜！你們剛剛 **沒有碰任何一台實體伺服器，沒有綁信用卡**，就利用 Netlify 這個「雲端託管 SaaS」把網站推向全世界了！
> 而且因為 GitHub 和 Netlify 已經「連線」了，**之後你在 VS Code 每按一次 Commit ＋ Sync，網站就會自動更新**（這叫 CI/CD，下週細講）。

---

## 🆘 常見狀況

| 狀況 | 原因與解法 |
| --- | --- |
| 網站顯示 `Page not found` | 檔名不是 `index.html`（可能是 `Index.html`），或檔案被放在子資料夾裡。在 VS Code 改名／移到最外層後，Commit ＋ Sync |
| Netlify 列表裡找不到我的 repo | 授權時沒勾選該 repo。點列表下方的「Configure the Netlify app on GitHub」重新勾選 |
| 中文變成亂碼 | 請 Copilot 確認 `<head>` 裡有 `<meta charset="UTF-8">`；VS Code 右下角狀態列應顯示 `UTF-8` |
| Deploy 失敗（Failed） | 檢查 Build command 和 Publish directory 是否都留空 |
| 網站沒更新 | 你是不是只按了 Commit、沒按 **同步變更（Sync）**？Commit 只存在你的電腦裡 |
| 想先試試看、不想用 GitHub | 可以用 [Netlify Drop](https://app.netlify.com/drop) 直接拖曳資料夾上線。但**這樣就沒有自動更新（CI/CD）的魔法**，所以課堂上請用 GitHub 的方式 |

更多問題 👉 [常見問題 FAQ](error_guide.md)

---

完成了嗎？回到 👉 [第 1 週步驟卡](../../lectures/wk01_1007_saas-storefront/steps.md)
