# 疑難排解手冊

遇到問題時，先找到和你狀況最像的題目，照「怎麼做」一步一步試。每做完一步就重新看一次結果。

[← 回課程首頁](../../README.md)　｜　[教學目錄](README.md)

**快速找題目：** 按 `Ctrl+F`（Mac：`⌘F`），輸入畫面上的關鍵字，例如 `Page not found`、`rejected`、`亂碼`。

| 分類 | 題號 |
| --- | --- |
| [VS Code／Git／Copilot](#3-vs-codegitcopilot) | Q1–Q10 |
| [Netlify 部署](#4-netlify-部署) | Q11–Q13 |
| [Netlify Forms](#5-netlify-forms) | Q14–Q16 |
| [LocalStorage](#6-localstorage) | Q17–Q18 |

---

## 1. 卡住時怎麼辦

1. **看清楚畫面上的訊息。** 找出關鍵字（例如 `rejected`、`404`），用它在本手冊搜尋。
2. **一次只改一個地方。** 改完馬上看結果，才知道是哪一步有效。
3. **找出是哪一段出問題。** 電腦上預覽正常嗎？GitHub 網頁上有最新的檔案嗎？Netlify 的 Deploys 顯示 Published 嗎？哪一段不正常，問題就在那一段。
4. **試了 15 分鐘還不行，就求助。** 課堂上舉起紅色回饋卡、問旁邊同學、在課程群組發問，或開一張 [求助單](https://github.com/cychiang-ntpu/VibeNTPU/issues/new?template=help_request.yml)。

## 2. 求助時請附上

- 你原本想看到什麼。
- 實際看到什麼（附截圖或完整錯誤訊息）。
- 你做到哪一步、已經試過哪些方法。
- 你的 GitHub repo 網址與 Netlify 網址。

**範例：**「我預期按下『加入早鳥名單』後，Netlify 後台會出現一筆資料。實際上頁面跳到 Thank you 頁，但後台是空的。我已確認 `<form>` 有 `data-netlify="true"`，也重新部署過。網址是 https://xxx.netlify.app ，repo 是 https://github.com/xxx/xxx 。」

**小工具：** 按 `F12`（Mac：`⌘⌥I`）可打開瀏覽器的開發者工具。**Console** 分頁的紅字是錯誤訊息，整段複製給 Copilot，比只說「網頁壞了」更容易得到正確的修改。

---

## 3. VS Code／Git／Copilot

### Q1. Copilot Chat 無法開啟、要求登入，或顯示已達使用上限

**症狀：** 點 Copilot 圖示沒反應、一直要求登入，或顯示已用完本月額度。

**怎麼做：**
1. 點 VS Code 左下角的帳戶圖示，確認已用 GitHub 帳號登入；沒有的話，照 [VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md) 步驟 6 登入。
2. 點 Copilot 圖示，選 **使用 Copilot（Set up Copilot）**，確認已啟用 Copilot Free。
3. 若顯示已達上限：
   - 簡單的文字修改，直接在檔案裡手動改。
   - 用 [提示詞產生器](../../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html) 一次把需求寫清楚，減少來回次數。
   - 申請 [GitHub Education](https://education.github.com/) 學生方案，通過後可免費使用額度較高的 Copilot Pro。
   - 臨時替代：改用網頁版 AI 助理（例如 [Claude](https://claude.ai/)、[ChatGPT](https://chatgpt.com/)、[Gemini](https://gemini.google.com/)），把它產生的程式碼貼進 `index.html`，按 `Ctrl+S` 存檔，再照常提交、同步變更。不要貼入個人資料或密碼。

### Q2. Copilot 只在聊天視窗顯示程式碼，沒有建立或修改檔案

**症狀：** Copilot 回了一段程式碼，但左側沒有新檔案，`index.html` 也沒變。

**怎麼做：**
1. 在聊天輸入框下方的模式選單，改選 **Agent**。
2. 確認左側檔案總管有顯示你的專案資料夾；若是空的，點選 **檔案 > 開啟資料夾** 打開它。
3. 在提示詞中寫清楚：「請直接修改工作區中的 `index.html`」，或輸入 `#` 選擇 `index.html`。
4. 重新送出。

### Q3. Copilot 要求執行終端機指令（Continue／Allow）

**症狀：** Copilot 顯示一段指令，請你按 **Continue**、**Allow** 或 **Run**。

**怎麼做：**
1. 按 **Skip**（略過）或 **Cancel**（取消）。
2. 在輸入框回覆：「請不要執行任何指令，也不要執行 git，只修改檔案。」
3. 提交與同步變更，請自己在原始檔控制面板按按鈕完成。

### Q4. Copilot 修改後結果變差，想回到先前狀態

**症狀：** Copilot 改完後排版亂掉、功能不見，或不是你要的。

**怎麼做：**（看你目前到哪一步）
1. **還沒按保留（Keep）**：在聊天面板按 **復原（Undo）**。
2. **已按保留，還沒提交**：點左側 **原始檔控制** 圖示 → 滑鼠移到 `index.html` 上 → 按彎曲箭頭 **捨棄變更（Discard Changes）** → 按 **捨棄檔案**。檔案會回到上一次提交的樣子，此動作無法復原。
3. **已經提交**：在聊天面板輸入「請把 index.html 恢復成上一個 commit 的內容」，檢查後保留，再提交、同步變更。不確定時請求助助教。
4. 以後每完成一小步、確認沒問題，就提交一次，隨時都有可以回去的版本。

### Q5. 終端機找不到 git，或原始檔控制面板要求下載 Git

**症狀：** 輸入 `git --version` 顯示「找不到命令」或「not recognized」；原始檔控制面板出現「下載 Git」按鈕。

**怎麼做：**
1. 確認已安裝 Git：Windows 到 <https://git-scm.com/downloads/win> 下載安裝，選項全部不改；macOS 打開「終端機」App 輸入 `git --version`，依提示按 **安裝**。
2. **關閉所有 VS Code 視窗**，再重新打開 VS Code。
3. 點選 **檢視 > 終端機**，再輸入一次 `git --version`。

### Q6. Commit 時要求設定 user.name 與 user.email

**症狀：** 按提交時出現「Make sure you configure your user.name and user.email in git」。

**怎麼做：**
1. 點選 **檢視 > 終端機（View > Terminal）** 打開終端機。
2. 複製下面兩行，換成你的資料，一行一行貼上並按 Enter：
   ```
   git config --global user.name "你的名字"
   git config --global user.email "你的 GitHub Email"
   ```
3. 回到原始檔控制面板，再按一次 **提交（Commit）**。

### Q7. 找不到「同步變更（Sync Changes）」按鈕

**症狀：** 原始檔控制面板中沒有同步變更按鈕。

**怎麼做：** 先看面板上顯示什麼：

| 你看到的畫面 | 怎麼做 |
| --- | --- |
| 只有「提交」按鈕 | 還沒提交。先輸入訊息、按 **提交（Commit）**，按鈕就會變成「同步變更 ↑1」 |
| 顯示「發佈分支（Publish Branch）」 | 這個資料夾還沒連上 GitHub。按 **發佈分支**，選 **Public**；或照 [Git 與 GitHub 入門](git_intro.md) 步驟 1–2 重新建立並複製 repo，再把 `index.html` 複製進去 |
| 顯示「目前開啟的資料夾沒有 Git 存放庫」 | 開錯資料夾了。點選 **檔案 > 開啟資料夾**，選擇從 GitHub 複製下來的那個資料夾 |

### Q8. Sync 失敗：rejected、驗證失敗或反覆要求登入

**症狀：** 按同步變更後出現 `rejected`、`Authentication failed`，或一直跳出登入視窗。

**怎麼做：**
1. **出現 rejected**：通常是你在 GitHub 網頁上改過檔案。再按一次 **同步變更**，VS Code 會先下載再上傳。
2. **出現「合併衝突（Merge Conflict）」**：先不要再按任何按鈕，截圖後求助助教。
3. **驗證失敗**：點左下角帳戶圖示，確認登入的是擁有這個 repo 的 GitHub 帳號；不是的話，登出後重新登入。

### Q9. 預覽空白、中文亂碼，或結果與預期不同

**症狀：** 預覽一片空白；中文變成奇怪的符號；畫面跟你想要的不一樣。

**怎麼做：**
1. **空白**：按 `Ctrl+S`（Mac：`⌘S`）存檔（分頁標題旁有實心圓點代表還沒存）。仍空白就按 `F12` 看 Console 的紅字，整段複製給 Copilot。
2. **亂碼**：請 Copilot 確認 `<head>` 裡有 `<meta charset="UTF-8">`；並看 VS Code 右下角是否顯示 `UTF-8`。
3. **跟想要的不一樣**：給 Copilot 更具體的描述，一次一件事。
   - 不具體：「不好看，重做。」
   - 具體：「標題放大為兩倍；背景改淺米色；手機寬度下三張卡片改成上下排列。」

### Q10. GitHub 要求輸入雙重驗證碼

**症狀：** 登入 GitHub 時要求輸入 6 位數驗證碼，或要求設定雙重驗證。

**怎麼做：**
1. 打開手機上的驗證 App（Google Authenticator 或 Microsoft Authenticator），輸入目前顯示的 6 位數字。
2. 還沒設定過：照 [課前準備清單](before_class.md) 步驟 1-3 設定。
3. 務必下載並保存復原碼；手機遺失時要用它登入。
4. 官方說明：[設定雙重驗證](https://docs.github.com/zh/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

---

## 4. Netlify 部署

### Q11. 網站顯示「Page not found」

**症狀：** 打開 `https://xxx.netlify.app` 時顯示 `Page not found`。

**怎麼做：**
1. 在 GitHub 網頁確認 repo 最外層有 `index.html`，而且全部小寫（不是 `Index.html` 或 `index.htm`）。
2. 若有錯，在 VS Code 改名或把檔案移到最外層，再提交、同步變更。
3. 在 Netlify 點選 **Project configuration → Build & deploy**，確認 **Publish directory** 是空白。

### Q12. 在 Netlify 找不到我的 GitHub repo

**症狀：** Netlify 匯入專案時，清單中沒有你的 repo。

**怎麼做：**
1. 在 repo 清單下方，按 **Configure the Netlify app on GitHub**。
2. 在 GitHub 頁面把你的 repo 勾選加入，按 **Save**。
3. 回到 Netlify 重新整理清單。

### Q13. GitHub 已更新，但網站沒有變化

**症狀：** 已在 VS Code 修改並提交，但網站還是舊的。

**怎麼做：**（照順序檢查）
1. **GitHub**：打開 repo 網頁，看最新的提交訊息有沒有出現。沒有 → 你只按了提交，回 VS Code 按 **同步變更（Sync Changes）**。
2. **Netlify**：打開 **Deploys** 頁面看最新一筆。顯示 **Failed** → 點開看紀錄最後幾行；完全沒有新紀錄 → 專案可能是用 Netlify Drop 拖曳建立的，請照 [GitHub 與 Netlify 部署](github_netlify_deploy.md) 用 GitHub 重新匯入。
3. **瀏覽器**：按 `Ctrl+Shift+R`（Mac：`⌘⇧R`）強制重新整理，或用無痕視窗開啟；手機請下拉重新整理。

---

## 5. Netlify Forms

以下三題對應第 2 週的表單串接，操作步驟見 [Netlify Forms 教學](netlify_forms.md)。

### Q14. Netlify 後台的 Forms 頁面沒有顯示我的表單

**症狀：** 已部署有表單的網頁，但 Netlify 的 Forms 頁面是空的，或只有一個啟用提示。

**怎麼做：**（照順序檢查）
1. 在 Netlify 的 **Forms** 頁面，按 **Enable form detection**（新專案預設是關閉的）。
2. 啟用後重新部署：點選 **Deploys** → **Trigger deploy** → **Deploy project**。
3. 請 Copilot 確認 `<form>` 標籤有 `data-netlify="true"` 和 `name` 屬性（例如 `name="waitlist"`）。
4. 若表單是用 JavaScript 產生的，請 Copilot「把 `<form>` 直接寫在 HTML 中」，再提交、同步變更。

官方說明：[Netlify Forms 疑難排解](https://docs.netlify.com/manage/forms/troubleshooting-tips/)

### Q15. 表單送出成功，但後台沒有資料

**症狀：** 頁面顯示送出成功，但 Forms 頁面沒有新資料。

**怎麼做：**
1. 確認你是在 `https://xxx.netlify.app` 網址上測試，不是在 VS Code 預覽中測試（預覽中送出的資料不會到 Netlify）。
2. 在 Netlify 點選 **Forms** → 你的表單 → **Spam submissions**，看資料是不是被當成垃圾訊息。
3. 若表單是用 JavaScript 送出的，請 Copilot 確認送出的資料中有 `form-name` 欄位，而且值和 `<form name="...">` 完全一樣。
4. 仍不行：按 `F12` → **Network** 分頁，再送出一次，把出現的錯誤截圖求助。

### Q16. 送出後跳到 Netlify 的 Thank you 頁面，未顯示會員儀表板

**症狀：** 按送出後，跳到 Netlify 的感謝頁，而不是在原頁面顯示會員儀表板。

**怎麼做：**
1. 打開 [第 2 週提示詞集](../../lectures/wk02_1014_baas-cicd/prompts.md)，找到「送出後在原頁面切換為會員儀表板」的提示詞。
2. 把提示詞交給 Copilot（Agent 模式），檢查後按 **保留（Keep）**。
3. 提交、同步變更，等部署完成後，在 Netlify 網址上重新測試。
4. 改完後若後台收不到資料，再看 Q15 第 3 項。

---

## 6. LocalStorage

操作步驟見 [LocalStorage 教學](localstorage.md)。

### Q17. 換一台裝置或瀏覽器開啟網站，歡迎畫面消失

**症狀：** 電腦上顯示會員歡迎畫面，但用手機或其他瀏覽器打開時，又回到未加入的狀態。

**怎麼做：**
1. 這是正常的，不需要修正。LocalStorage 的資料只存在「這一台裝置的這一個瀏覽器」裡，不會同步到其他地方。
2. 若你的產品需要跨裝置保存，需要雲端資料庫與登入功能，這是課程之外的延伸內容。

### Q18. 想重新測試表單，但一直顯示歡迎畫面

**症狀：** 已送出過表單，重新打開網站時直接顯示會員儀表板，沒辦法再測一次表單。

**怎麼做：**（任選一種）
1. 按儀表板上的 **登出** 按鈕（若有做這個按鈕）。
2. 按 `F12` → **Application** 分頁 → 左側 **Local storage** → 點你的網址 → 在右側項目上按右鍵刪除。
3. 用無痕視窗打開網站；關掉無痕視窗後資料就會清除。

---

## 7. 參考資料

- [MDN：什麼是瀏覽器開發者工具](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)
- [VS Code：原始檔控制](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [Netlify Support Forums](https://answers.netlify.com/)
- 想了解問題背後的原理：[Git、Copilot 與部署機制（選讀）](../deep_dive/git_and_copilot.md)
