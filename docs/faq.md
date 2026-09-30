# 🆘 常見問題與錯誤排除（FAQ）

> 卡關時先照這頁檢查，90% 的問題都能在這裡解決。還是不行？把錯誤畫面截圖問 AI 或問助教！

[← 回課程首頁](../README.md)

---

## 🤖 AI 與程式碼

<details>
<summary><b>Q1. AI 只給我一段程式碼，不是完整的檔案？</b></summary>

在咒語最後加上：「**其他部分保持不變，請給我完整的 index.html 程式碼**」。
如果 AI 因為太長被截斷，可以說：「請繼續」，然後把兩段接起來（注意不要重複）。
</details>

<details>
<summary><b>Q2. 雙擊 index.html 後，畫面一片空白或只顯示程式碼文字？</b></summary>

- **顯示程式碼文字**：檔名可能是 `index.html.txt`。請開啟「顯示副檔名」檢查（見 [存檔教學](../week1/prompts.md#-如何把-ai-給的程式碼存成-indexhtml)）。
- **一片空白**：程式碼可能沒複製完整。檢查檔案最後一行是不是 `</html>`。
- 還是不行：用 [卡關急救包咒語](../week1/prompts.md#咒語-3卡關急救包-) 問 AI。
</details>

<details>
<summary><b>Q3. 中文變成亂碼（例如 `ä¸‰å³½`）？</b></summary>

1. 確認 `<head>` 裡有 `<meta charset="UTF-8">`。
2. 存檔時編碼選 **UTF-8**（Windows 記事本在「另存新檔」視窗下方可以選）。
</details>

<details>
<summary><b>Q4. AI 做出來的網頁跟我想的不一樣？</b></summary>

這很正常！Vibe Coding 就是「看結果 → 給回饋 → 再修改」的循環。回饋越具體越好：
- ❌「不好看，重做」
- ✅「標題字太小，請放大到兩倍；背景改成淺米色；三張功能卡片在手機上要改成上下排列」

也可以截圖給 AI 看，說「這個地方跑版了」。
</details>

---

## 🗄️ GitHub

<details>
<summary><b>Q5. 找不到「Upload files」按鈕？</b></summary>

- 確認你在**自己的 repo 首頁**（網址是 `github.com/你的帳號/repo名稱`）。
- 按鈕在檔案列表右上方的 **「Add file」** 下拉選單裡。
- 如果 repo 是空的（建立時沒勾 Add a README），畫面會顯示「uploading an existing file」的連結，點它即可。

📖 [GitHub：新增檔案到儲存庫](https://docs.github.com/zh/repositories/working-with-files/managing-files/adding-a-file-to-a-repository)
</details>

<details>
<summary><b>Q6. 上傳新版 index.html 後，GitHub 上變成兩個檔案？</b></summary>

新檔名跟舊檔不一樣（例如 `index (1).html`）。請確認上傳的檔名**完全是** `index.html`，並把多出來的檔案刪掉：點檔案 → 右上角「⋯」→ **Delete file**。
</details>

<details>
<summary><b>Q7. GitHub 要求輸入雙重驗證碼，但我沒設定？</b></summary>

依照畫面指示，用手機的驗證 App 掃描 QR Code 設定即可。
📖 [GitHub：設定雙重驗證](https://docs.github.com/zh/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)
</details>

---

## ☁️ Netlify 部署

<details>
<summary><b>Q8. 網站顯示「Page not found」？</b></summary>

- 99% 是檔名問題：必須是全小寫的 `index.html`，而且要放在 repo 的**最外層**（不是在資料夾裡）。
- 檢查 Netlify 部署設定的 **Publish directory 是否為空白**。
</details>

<details>
<summary><b>Q9. 在 Netlify 找不到我的 GitHub repo？</b></summary>

授權時只勾選了部分 repo。在 Netlify 選 repo 的畫面下方，點 **「Configure the Netlify app on GitHub」**，把新的 repo 勾選進去。
</details>

<details>
<summary><b>Q10. 我更新了 GitHub，但網站沒有變？</b></summary>

1. 到 Netlify → **Deploys**，看最新一筆是不是 **Published**（如果是 Failed，點進去看原因）。
2. 如果根本沒有新的部署紀錄：你的專案可能是用 **Netlify Drop 拖曳**建立的，沒有跟 GitHub 連線。請重新用「Import from Git」建立。
3. 手機瀏覽器快取：下拉重新整理，或用無痕模式開啟。
</details>

---

## 📦 Netlify Forms

<details>
<summary><b>Q11. Netlify 後台的 Forms 頁面是空的，看不到我的表單？</b></summary>

依序檢查：
1. **有沒有開啟 Form detection？** 新專案預設是關閉的！到 Forms 頁面按 **Enable form detection**。
2. **開啟後有沒有重新部署？** Netlify 只在部署時掃描表單。到 Deploys → **Trigger deploy** 重新部署。
3. **`<form>` 有沒有 `data-netlify="true"` 和 `name` 屬性？**
4. **表單是不是由 JavaScript 動態產生的？** 如果 AI 用 JavaScript「畫出」表單，Netlify 掃描 HTML 時會看不到。請 AI 把 `<form>` 直接寫在 HTML 裡。

📖 [Netlify：表單疑難排解](https://docs.netlify.com/forms/troubleshooting-tips/)
</details>

<details>
<summary><b>Q12. 表單送出了，但後台沒有資料？</b></summary>

- 你是在 `file:///` 開頭的本機網址測試嗎？**必須在 `https://xxx.netlify.app` 上測試**。
- 你有沒有填到隱藏的 honeypot 欄位？（被當成機器人過濾掉了，可以到 Forms → **Spam submissions** 看看）
- 用 AJAX 送出時，資料裡要有 `form-name` 欄位，值要和 `<form name="...">` 一樣。
</details>

<details>
<summary><b>Q13. 送出後網頁跳到一個 Netlify 的「Thank you」頁面，沒有顯示會員儀表板？</b></summary>

表示 JavaScript 沒有攔截送出動作（沒有 `event.preventDefault()`）。請用 [第二週咒語 2](../week2/prompts.md#咒語-2送出後原地變成會員儀表板) 請 AI 改成 AJAX 送出。
</details>

---

## 💻 LocalStorage

<details>
<summary><b>Q14. 換了手機打開網站，歡迎畫面不見了？</b></summary>

這是正常的！LocalStorage 存在**每台裝置自己的瀏覽器**裡，就像集點卡在你口袋，換一個人（裝置）就沒有了。詳見 [LocalStorage 解說](../week2/localstorage.md)。
</details>

<details>
<summary><b>Q15. 我想重新測試表單，但一直顯示歡迎畫面？</b></summary>

按儀表板上的「登出」按鈕；或按 `F12` → Application → Local storage → 刪除資料；或用無痕模式開啟。
</details>
