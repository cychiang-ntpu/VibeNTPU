# ☁️ 組裝 SaaS 第一步：GitHub 上傳 ＋ Netlify 部署

> 這一頁帶你把電腦裡的 `index.html`，變成全世界都能打開的網址。
> 全程只需要**滑鼠拖曳 ＋ 點按鈕**，不需要打任何指令。

[← 回第 1 週](../../lectures/wk01_1007_saas-storefront/README.md)

> 📝 GitHub 與 Netlify 的介面偶爾會改版，按鈕位置可能跟下面描述略有不同。找不到按鈕時，請對照官方文件：
> [GitHub：新增檔案到儲存庫](https://docs.github.com/zh/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)｜[Netlify：從 Git 儲存庫部署](https://docs.netlify.com/start/quickstarts/deploy-from-repository/)

---

## Part A：把設計圖放進總部保險箱（GitHub）🗄️

### A1. 建立新的 Repository（儲存庫）

> **Repository（簡稱 repo）** ＝ 一個專案資料夾，GitHub 會幫你記住裡面每個檔案的每一次修改。

1. 登入 <https://github.com/>。
2. 點右上角的 **「+」** → **「New repository」**（或直接前往 <https://github.com/new>）。
3. 填寫：
   - **Repository name**：用英文小寫＋連字號，例如 `rent-radar`。
   - **Description**（選填）：一句話介紹你的產品。
   - 選 **Public（公開）**。
   - ✅ 勾選 **「Add a README file」**（這樣 repo 一建立就不是空的，比較好上傳檔案）。
4. 按綠色的 **「Create repository」**。

### A2. 拖曳上傳 `index.html`

1. 在你的 repo 頁面，點 **「Add file」** → **「Upload files」**。
2. 把桌面上的 `index.html` **直接拖曳**到網頁中間的虛線框裡。
3. 在下方「Commit changes」的欄位寫一句說明，例如 `第一版首頁`。
   > **Commit** ＝ 存檔點。就像打電動時的「存檔」，之後隨時可以回到這個版本。
4. 按綠色的 **「Commit changes」**。
5. 回到 repo 首頁，確認看到 `index.html` 出現在檔案列表中。✅

> ⚠️ 檔名一定要是 **`index.html`**。Netlify 會自動把這個檔案當作「首頁」，檔名不對就會出現 `Page not found`。

📖 延伸學習：[GitHub 官方：關於儲存庫](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories)｜[什麼是 Git？（Git 官方書，繁中）](https://git-scm.com/book/zh-tw/v2/%E9%96%8B%E5%A7%8B-%E9%97%9C%E6%96%BC%E7%89%88%E6%9C%AC%E6%8E%A7%E5%88%B6)

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
> 而且因為 GitHub 和 Netlify 已經「連線」了，下週你會看到更神奇的事：**只要更新 GitHub 上的檔案，網站就會自動更新**（這叫 CI/CD）。

---

## 🆘 常見狀況

| 狀況 | 原因與解法 |
| --- | --- |
| 網站顯示 `Page not found` | 檔名不是 `index.html`（可能是 `Index.html`、`index.html.txt`），請到 GitHub 重新命名或重新上傳 |
| Netlify 列表裡找不到我的 repo | 授權時沒勾選該 repo。點列表下方的「Configure the Netlify app on GitHub」重新勾選 |
| 中文變成亂碼 | 存檔時沒選 UTF-8，請 AI 在 `<head>` 裡確認有 `<meta charset="UTF-8">`，並重新用 UTF-8 存檔 |
| Deploy 失敗（Failed） | 檢查 Build command 和 Publish directory 是否都留空 |
| 想先試試看、不想用 GitHub | 可以用 [Netlify Drop](https://app.netlify.com/drop) 直接拖曳資料夾上線。但**這樣就沒有自動更新（CI/CD）的魔法**，所以課堂上請用 GitHub 的方式 |

更多問題 👉 [常見問題 FAQ](error_guide.md)

---

完成了嗎？回到 👉 [第 1 週步驟卡](../../lectures/wk01_1007_saas-storefront/steps.md)
