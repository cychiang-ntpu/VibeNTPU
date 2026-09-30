# 🆘 卡關急救手冊（打怪攻略）

> 💪 **卡關 = 經驗值。** 每個工程師每天都在卡關，差別只是他們知道去哪裡找答案。
> 你現在遇到的問題，幾乎每一屆同學都遇過，所以才會寫在這裡。**你一點都不笨，你只是還沒遇過這隻怪。**

### 🧭 卡關時的四個步驟

1. **深呼吸** 😮‍💨：錯誤訊息不是在罵你，是在給你線索。
2. **在這頁找找看**：按 `Ctrl+F`（Mac：`⌘+F`）搜尋你看到的關鍵字，例如「Page not found」「亂碼」。
3. **問 AI**：把錯誤畫面截圖貼給 AI，說「我是新手，看到這個畫面，請一步一步教我怎麼解決」。
4. **15 分鐘還沒解決 → 求救**：貼紅色便利貼、問隔壁組、課程群組發問，或開一張 [🆘 求救單](https://github.com/cychiang-ntpu/VibeNTPU/issues/new?template=help_request.yml)。

> 🏆 解決過的問題，記得寫進冒險護照的反思裡，「卡過又解決」就是你升級最多的地方。

[← 回課程首頁](../../README.md)

---

## 💻 VS Code ／ Git ／ Copilot

<details>
<summary><b>Q1. Copilot Chat 打不開、叫我登入，或說「已達使用上限」？</b></summary>

- **叫我登入**：點 VS Code 左下角人像圖示 → 用 GitHub 登入（[VS Code ＋ Copilot 入門步驟 3、4](vscode_copilot_starter.md#步驟-3在-vs-code-登入-github-)）。
- **已達上限（免費版每月次數用完）**：
  1. 先改用咒語產生器，一次把需求講清楚，節省次數。
  2. 申請 [GitHub Education](https://education.github.com/) 學生方案，通過後可免費使用 Copilot Pro。
  3. 緊急備案：改用網頁版 AI（[Claude](https://claude.ai/)／[ChatGPT](https://chatgpt.com/)／[Gemini](https://gemini.google.com/)），把回傳的程式碼貼進 VS Code 的 `index.html` 並存檔（`Ctrl+S`），一樣可以 Commit ＋ Sync。咒語產生器可以切換成這些 AI 的版本。
</details>

<details>
<summary><b>Q2. Copilot 只在聊天視窗給我一段程式碼，沒有真的建立／修改檔案？</b></summary>

- 確認聊天輸入框上方的模式是 **Agent**（或 Edit），不是 **Ask**。Ask 模式只會回答，不會改檔案。
- 在訊息裡加上：「請**直接建立／修改**工作區中的 `index.html` 檔案」，或用 `#index.html` 指定檔案。
- 確認 VS Code 有**開啟資料夾**（左側檔案總管不是空的）。沒開資料夾時，Copilot 不知道要把檔案放哪裡。
</details>

<details>
<summary><b>Q3. Copilot 說要「執行指令」，叫我按 Continue／Allow？</b></summary>

這門課**不需要**讓 Copilot 執行任何終端機指令。看不懂它要做什麼時，按 **Skip／Cancel**，並跟它說：
「請不要執行任何指令，也不要幫我執行 git，只要修改檔案就好。」
存檔上傳我們自己用 **原始檔控制** 面板按按鈕完成。
</details>

<details>
<summary><b>Q4. Copilot 改壞了，我想回到剛剛的樣子？</b></summary>

- **還沒按 Keep**：直接按 **Undo（復原）**。
- **已經 Keep、但還沒 Commit**：原始檔控制 → 在 `index.html` 旁按 **↶ 捨棄變更**，回到上一個存檔點。
- **已經 Commit 了**：見 [Git 入門：時光機](git_intro.md#-時光機查看歷史救回改壞的版本)。
</details>

<details>
<summary><b>Q5. 終端機說找不到 git，或原始檔控制面板要我「下載 Git」？</b></summary>

Git 沒裝好。Windows 到 <https://git-scm.com/downloads/win> 下載安裝（全部預設）；macOS 在終端機輸入 `git --version` 並依提示安裝。
**裝完一定要把 VS Code 完全關掉再打開。**
</details>

<details>
<summary><b>Q6. 按 Commit 時說「請設定 user.name 和 user.email」（Make sure you configure your user.name and user.email）？</b></summary>

在 VS Code 終端機（`` Ctrl+` ``）貼上這兩行，換成你的資料後再 Commit 一次：

```
git config --global user.name "你的名字"
git config --global user.email "你的GitHub Email"
```
</details>

<details>
<summary><b>Q7. 找不到「同步變更（Sync Changes）」按鈕？</b></summary>

- **還沒 Commit**：要先 Commit，Sync 按鈕才會出現（上面會顯示 ↑1）。
- **只看到「發佈分支（Publish Branch）」**：你的資料夾不是從 GitHub clone 下來的。可以按「發佈分支」→ 選 **Public** 把它變成新的 GitHub repo；或重新照 [Git 入門步驟 1、2](git_intro.md#步驟-1在-github-建立你的-repo-) clone 一次，再把 `index.html` 複製進去。
- **面板說「目前開啟的資料夾沒有 Git 存放庫」**：你開錯資料夾了。檔案 → 開啟資料夾，選 clone 下來的那一個。
</details>

<details>
<summary><b>Q8. Sync 失敗：「rejected」、「驗證失敗」或一直要我登入？</b></summary>

- **rejected**：GitHub 上有你電腦沒有的修改（例如在網頁上改過 README）。再按一次 **同步變更**（它會先下載再上傳）。跳出「合併衝突」就舉手找助教。
- **驗證失敗**：VS Code 左下角人像 → 確認登入的是**同一個** GitHub 帳號；照瀏覽器指示重新授權。
</details>

<details>
<summary><b>Q9. 預覽畫面一片空白、中文變亂碼，或做出來的跟我想的不一樣？</b></summary>

- **空白**：`index.html` 可能還沒存檔（分頁標題旁有白色圓點＝未存檔），按 `Ctrl+S`／`⌘S`；或請 Copilot 檢查「為什麼預覽是空白的」。
- **亂碼**：請 Copilot 確認 `<head>` 裡有 `<meta charset="UTF-8">`；VS Code 右下角應顯示 `UTF-8`。
- **跟想的不一樣**：這很正常！Vibe Coding 就是「看結果 → 給回饋 → 再修改」。回饋越具體越好：
  - ❌「不好看，重做」
  - ✅「標題字太小，請放大到兩倍；背景改成淺米色；三張功能卡片在手機上要改成上下排列」
</details>

<details>
<summary><b>Q10. GitHub 要求輸入雙重驗證碼，但我沒設定？</b></summary>

依照畫面指示，用手機的驗證 App 掃描 QR Code 設定即可，並**保存好復原碼**。
📖 [GitHub：設定雙重驗證](https://docs.github.com/zh/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)
</details>

---

## ☁️ Netlify 部署

<details>
<summary><b>Q11. 網站顯示「Page not found」？</b></summary>

- 99% 是檔名問題：必須是全小寫的 `index.html`，而且要放在 repo 的**最外層**（不是在資料夾裡）。
- 檢查 Netlify 部署設定的 **Publish directory 是否為空白**。
</details>

<details>
<summary><b>Q12. 在 Netlify 找不到我的 GitHub repo？</b></summary>

授權時只勾選了部分 repo。在 Netlify 選 repo 的畫面下方，點 **「Configure the Netlify app on GitHub」**，把新的 repo 勾選進去。
</details>

<details>
<summary><b>Q13. 我更新了 GitHub，但網站沒有變？</b></summary>

1. 到 Netlify → **Deploys**，看最新一筆是不是 **Published**（如果是 Failed，點進去看原因）。
2. 如果根本沒有新的部署紀錄：你的專案可能是用 **Netlify Drop 拖曳**建立的，沒有跟 GitHub 連線。請重新用「Import from Git」建立。
3. 你是不是只按了 **Commit**、沒按 **同步變更（Sync）**？到 GitHub 網頁看看最新的 commit 有沒有出現。
4. 手機瀏覽器快取：下拉重新整理，或用無痕模式開啟。
</details>

---

## 📦 Netlify Forms

<details>
<summary><b>Q14. Netlify 後台的 Forms 頁面是空的，看不到我的表單？</b></summary>

依序檢查：
1. **有沒有開啟 Form detection？** 新專案預設是關閉的！到 Forms 頁面按 **Enable form detection**。
2. **開啟後有沒有重新部署？** Netlify 只在部署時掃描表單。到 Deploys → **Trigger deploy** 重新部署。
3. **`<form>` 有沒有 `data-netlify="true"` 和 `name` 屬性？**
4. **表單是不是由 JavaScript 動態產生的？** 如果 AI 用 JavaScript「畫出」表單，Netlify 掃描 HTML 時會看不到。請 AI 把 `<form>` 直接寫在 HTML 裡。

📖 [Netlify：表單疑難排解](https://docs.netlify.com/manage/forms/troubleshooting-tips/)
</details>

<details>
<summary><b>Q15. 表單送出了，但後台沒有資料？</b></summary>

- 你是在 `file:///` 開頭的本機網址測試嗎？**必須在 `https://xxx.netlify.app` 上測試**。
- 你有沒有填到隱藏的 honeypot 欄位？（被當成機器人過濾掉了，可以到 Forms → **Spam submissions** 看看）
- 用 AJAX 送出時，資料裡要有 `form-name` 欄位，值要和 `<form name="...">` 一樣。
</details>

<details>
<summary><b>Q16. 送出後網頁跳到一個 Netlify 的「Thank you」頁面，沒有顯示會員儀表板？</b></summary>

表示 JavaScript 沒有攔截送出動作（沒有 `event.preventDefault()`）。請用 [第二週咒語 2](../../lectures/wk02_1014_baas-cicd/prompts.md#咒語-2送出後原地變成會員儀表板) 請 AI 改成 AJAX 送出。
</details>

---

## 💻 LocalStorage

<details>
<summary><b>Q17. 換了手機打開網站，歡迎畫面不見了？</b></summary>

這是正常的！LocalStorage 存在**每台裝置自己的瀏覽器**裡，就像集點卡在你口袋，換一個人（裝置）就沒有了。詳見 [LocalStorage 解說](localstorage.md)。
</details>

<details>
<summary><b>Q18. 我想重新測試表單，但一直顯示歡迎畫面？</b></summary>

按儀表板上的「登出」按鈕；或按 `F12` → Application → Local storage → 刪除資料；或用無痕模式開啟。
</details>
