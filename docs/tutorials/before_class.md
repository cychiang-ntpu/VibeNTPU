# 課前準備清單（檢核點 0）

> **完成期限**：2026/10/7 第一次上課前
> **預估時間**：約 60–75 分鐘（大部分是下載與安裝的等待時間）
> **你需要準備**：一台可以安裝軟體的筆記型電腦（Windows 10／11 或 macOS）、一支可以上網的手機、一個常用的 Email 信箱。

[← 回課程首頁](../../README.md)　｜　[教學目錄](README.md)　｜　[學習檢核點](../checkpoints.md)

---

## 這份清單要做什麼

請從步驟 1 依序做到步驟 10，一次只做一步。每一步最後都有「完成後你應該看到」，對照一下再往下走。做完之後，你的電腦就能在課堂上直接開始做網站。

請務必在上課前完成：課堂上幾十人同時下載安裝會非常慢，帳號驗證也需要時間。

**你會用到的工具，一句話說明：**

| 工具 | 一句話說明 |
| --- | --- |
| GitHub | 放你網站檔案的雲端資料夾，會記住每一次修改 |
| VS Code | 在電腦上編輯網頁的軟體 |
| Git | 裝在電腦裡、負責記錄修改的工具 |
| GitHub Copilot | VS Code 裡的 AI 助理，用中文描述需求就能幫你寫程式碼 |
| Netlify | 把 GitHub 上的檔案變成大家都能打開的網站 |

可以想成美食街：GitHub 是保存食譜的倉庫，VS Code 是廚房，Netlify 是對外營業的攤位。

**注意：** 學校電腦教室的電腦通常無法安裝軟體，Chromebook 與平板也不適用，請使用自己的筆電。

---

## 步驟 1：申請 GitHub 帳號並開啟雙重驗證（約 15 分鐘）

GitHub 帳號是整門課的通行證：Copilot 和 Netlify 都用它登入。雙重驗證（2FA）＝登入時除了密碼，還要輸入手機 App 產生的 6 位數驗證碼，GitHub 要求所有帳號開啟。

### 1-1 申請帳號

1. 打開瀏覽器，前往 <https://github.com/signup>。
2. 在 **Email** 欄位輸入你的 Email，按 **Continue**。
3. 在 **Password** 欄位設定密碼，按 **Continue**。
4. 在 **Username** 欄位輸入使用者名稱，按 **Continue**。
   - 使用者名稱會出現在網址中，例如 `github.com/amy-ntpu-2026`。
   - 建議只用英文小寫、數字和 `-`，不要用真實全名或學號。
5. 依畫面完成「我不是機器人」的驗證。
6. 打開你的信箱，找到 GitHub 寄來的驗證碼，輸入到網頁上。
7. 之後若出現問卷，可以直接按 **Skip personalization** 略過。

### 1-2 在手機安裝驗證 App

1. 在手機的 App Store 或 Google Play 搜尋 `Google Authenticator` 或 `Microsoft Authenticator`。
2. 安裝其中一個。

### 1-3 開啟雙重驗證

1. 在 GitHub 網頁右上角，點你的大頭貼圖示。
2. 在選單中點選 **Settings**。
3. 在左側選單點選 **Password and authentication**。
4. 按 **Enable two-factor authentication**。
5. 畫面會出現一個 QR Code。
6. 打開手機上的驗證 App，按 **＋**（新增），選擇 **掃描 QR 碼**，對準電腦螢幕上的 QR Code。
7. 手機 App 會出現一組 6 位數字，把它輸入到 GitHub 網頁的欄位中，按 **Continue**。

### 1-4 保存復原碼（很重要）

復原碼（recovery codes）＝手機遺失時用來登入的備用密碼。沒有它，手機掉了就可能再也登不進帳號。

1. 在 GitHub 顯示復原碼的畫面，按 **Download** 下載成檔案。
2. 把檔案存到你找得到的地方（例如雲端硬碟），或抄在紙上收好。
3. 勾選或按下 **I have saved my recovery codes**，完成設定。

**完成後你應該看到：** 登出再登入 GitHub 時，輸入密碼後會要求輸入 6 位數驗證碼；打開手機 App 輸入當下顯示的數字即可登入。

**如果不一樣：**

- 使用者名稱顯示已被使用 → 加上數字或年份，例如 `amy-ntpu-2026`。
- 驗證碼一直被拒絕 → 驗證碼每 30 秒更換一次，請輸入 App 上「目前」顯示的數字；並確認手機時間設為自動。
- 其他狀況見 [疑難排解手冊](error_guide.md) Q10，或 [GitHub 官方說明：設定雙重驗證](https://docs.github.com/zh/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)。

---

## 步驟 2：（選做，建議）申請 GitHub 學生方案（約 10 分鐘，審核需數天）

GitHub Education 學生方案通過後，可以免費使用額度較高的 Copilot Pro。沒有通過也不影響上課，免費的 Copilot Free 就夠用。

1. 前往 <https://education.github.com/pack>。
2. 按 **Start an application**（或 **Join GitHub Education**），登入 GitHub。
3. 身分選擇 **Student**。
4. 依畫面加入並選擇你的學校 Email（`@gm.ntpu.edu.tw` 等學校信箱），到信箱完成驗證。
5. 學校名稱選擇 **National Taipei University**。
6. 依畫面指示用電腦或手機鏡頭拍攝學生證正面，按 **Process my application** 送出。

**完成後你應該看到：** 畫面顯示申請已送出。審核通常需要數天，通過時會收到 Email。

**如果不一樣：** 申請被退回 → 常見原因是照片模糊或看不到有效日期，重新拍一張清楚的照片再申請。來不及通過也沒關係，直接進行下一步。

---

## 步驟 3：安裝 VS Code（約 10 分鐘）

1. 前往 <https://code.visualstudio.com/>，按藍色的 **Download** 按鈕。
2. **Windows**：打開安裝檔 → 選 **我接受合約** → 勾選 **加入 PATH** → 一路按 **下一步** → **安裝** → **完成**。
3. **macOS**：把下載的 `Visual Studio Code.app` 拖到「應用程式」資料夾 → 從「應用程式」資料夾打開它。

逐畫面的說明：[VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md) 步驟 3。

**完成後你應該看到：** VS Code 開啟，出現「歡迎使用（Welcome）」頁面。

**如果不一樣：** Windows 顯示「Windows 已保護您的電腦」→ 按 **其他資訊** → **仍要執行**。

---

## 步驟 4：安裝 Git 並確認（約 10 分鐘）

1. **Windows**：前往 <https://git-scm.com/downloads/win> 下載 → 打開安裝檔 → **所有選項都不要改，一直按 Next** → **Install** → **Finish**。
2. **macOS**：按 `⌘`＋`空白鍵`，輸入 `終端機` 按 Enter → 輸入 `git --version` 按 Enter → 跳出視窗時按 **安裝**、**同意**，等待完成。
3. **完全關閉 VS Code，再重新打開。**
4. 在 VS Code 上方選單點選 **檢視 > 終端機（View > Terminal）**，或按 `` Ctrl+` ``（Mac：`` ⌃` ``）。
5. 在畫面下方出現的終端機中輸入 `git --version`，按 Enter。

逐畫面的說明：[VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md) 步驟 4。

**完成後你應該看到：** 終端機顯示類似 `git version 2.47.1` 的文字。

**如果不一樣：** 顯示「找不到命令」→ 確認所有 VS Code 視窗都已關閉再重開；仍不行見 [疑難排解手冊](error_guide.md) Q5。

---

## 步驟 5：告訴 Git 你的名字與 Email（約 2 分鐘）

每次存檔紀錄都會寫上作者，所以要先設定。整台電腦只做一次。

1. 在 VS Code 打開終端機：**檢視 > 終端機（View > Terminal）**，或按 `` Ctrl+` ``。
2. 複製下面第一行，把 `你的名字或暱稱` 換成你的名字（引號保留），貼到終端機，按 Enter：
   ```
   git config --global user.name "你的名字或暱稱"
   ```
3. 複製下面第二行，把 `你註冊GitHub的Email` 換成你的 GitHub Email，貼到終端機，按 Enter：
   ```
   git config --global user.email "你註冊GitHub的Email"
   ```
4. 輸入 `git config --global --list`，按 Enter 檢查。

**完成後你應該看到：** 畫面列出 `user.name=...` 與 `user.email=...`，內容是你剛才輸入的資料。

**如果不一樣：** 打錯字 → 重新執行那一行即可覆蓋。

---

## 步驟 6：在 VS Code 登入 GitHub（約 3 分鐘）

1. 點 VS Code **左下角**人像形狀的圖示（**帳戶，Accounts**）。
2. 點選 **使用 GitHub 登入以使用 GitHub Copilot**（Sign in with GitHub to use GitHub Copilot）。
3. 在自動打開的瀏覽器頁面按 **Authorize Visual-Studio-Code**。
4. 瀏覽器詢問是否開啟 VS Code 時，按 **開啟**。

**完成後你應該看到：** 再點左下角帳戶圖示，會顯示你的 GitHub 帳號名稱。

**如果不一樣：** 見 [VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md) 步驟 6。

---

## 步驟 7：啟用 Copilot Free（約 3 分鐘）

1. 點 VS Code 最上方標題列（或最下方狀態列）的 Copilot 圖示（小機器人臉）。
2. 選擇 **使用 Copilot（Set up Copilot）**，方案選 **GitHub Copilot Free**。
3. 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）打開聊天面板，輸入 `你好` 並按 Enter。

**完成後你應該看到：** 側邊出現 Copilot 聊天面板，並回覆了你的訊息。

**如果不一樣：** 找不到圖示 → 用瀏覽器前往 <https://github.com/settings/copilot> 啟用 Copilot Free；其他狀況見 [疑難排解手冊](error_guide.md) Q1。

---

## 步驟 8：安裝 Live Preview（約 2 分鐘）

1. 點 VS Code 最左邊那一排中四個小方塊的圖示（**延伸模組，Extensions**）。
2. 搜尋 `Live Preview`。
3. 選擇發行者為 **Microsoft** 的那一個，按 **安裝（Install）**。

**完成後你應該看到：** 安裝按鈕變成 **解除安裝（Uninstall）** 或齒輪圖示。

**如果不一樣：** 有好幾個名稱相似的套件 → 只裝 **Microsoft** 出品的版本。

---

## 步驟 9：第一個練習 Hello NTPU（約 10 分鐘）

1. 在桌面建立資料夾 `hello-ntpu`。
2. VS Code → **檔案 > 開啟資料夾（File > Open Folder）** → 選擇 `hello-ntpu`。
3. 詢問是否信任作者時，按 **是，我信任作者**。
4. 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）打開聊天面板，模式選 **Agent**。
5. 貼上 [VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md) 步驟 9 的提示詞，按 Enter。
6. Copilot 若請你執行指令，按 **Skip**。
7. 出現 `index.html` 後，按 **保留（Keep）**。
8. 在 `index.html` 上按右鍵 → **Show Preview**。

**完成後你應該看到：** 預覽畫面中央顯示「Hello NTPU」，背景為漸層色。

**如果不一樣：** Copilot 沒有建立檔案 → 模式改選 **Agent** 再送一次（[疑難排解手冊](error_guide.md) Q2）。

---

## 步驟 10：用 GitHub 帳號申請 Netlify（約 5 分鐘）

Netlify 會在第 1 週把你的網頁變成公開網站。免費方案不需要信用卡。

1. 前往 <https://app.netlify.com/signup>。
2. 按 **Sign up with GitHub**。
3. 在 GitHub 授權頁面按 **Authorize Netlify**。
4. 若詢問用途，選擇個人或學習用途（例如 **Personal**），名稱可填你的英文名字。
5. 若出現「部署你的第一個專案」之類的畫面，可以先略過或關閉，第 1 週上課再做。

**完成後你應該看到：** 進入 Netlify 的主畫面（Projects 頁面），右上角顯示你的頭像。

**如果不一樣：** 畫面要求輸入信用卡 → 你可能點到付費方案，回到 <https://app.netlify.com/> 即可使用免費方案。

---

## 最後：想一想你的創業題目（約 10 分鐘）

第 1 週會用你的題目做一個產品首頁。請先想 1–2 個方向，並回答三個問題：**誰會用？他們現在怎麼解決？為什麼現在的方法不夠好？**

| 題目 | 誰會用 | 要解決的問題 |
| --- | --- | --- |
| 大學生租屋評價平台 | 三峽在外租屋的學生 | 房東資訊不透明，糾紛難以事先避免 |
| 二手教科書交換平台 | 修同一門課的學生 | 教科書貴、用一學期就不用了 |
| 校園周邊餐飲地圖 | 新生與交換生 | 資訊散落在社群貼文，不好依價格與距離找 |

更多題目見 [第 1 週講義](../../lectures/wk01_1007_saas-storefront/README.md)。

---

## 完成檢查表

- [ ] 步驟 1：GitHub 可以登入，已開啟雙重驗證，復原碼已保存
- [ ] 步驟 2：（選做）已送出 GitHub 學生方案申請
- [ ] 步驟 3：VS Code 可以打開
- [ ] 步驟 4：終端機輸入 `git --version` 顯示版本號
- [ ] 步驟 5：`git config --global --list` 顯示我的名字與 Email
- [ ] 步驟 6：VS Code 左下角帳戶圖示顯示我的 GitHub 帳號
- [ ] 步驟 7：Copilot 聊天面板可以打開並回覆
- [ ] 步驟 8：已安裝 Microsoft 出品的 Live Preview
- [ ] 步驟 9：已用 Copilot 做出 Hello NTPU 並看到預覽
- [ ] 步驟 10：已用 GitHub 帳號登入 Netlify
- [ ] 已想好 1–2 個創業題目

全部完成後，就達成檢核點 0。第 1 週課堂會說明如何在 [學習歷程檔案](../../templates/portfolio_README.md) 中記錄。

## 卡住了怎麼辦

1. 先看 [疑難排解手冊](error_guide.md)，Q1–Q10 涵蓋登入、Copilot、Git 的常見問題。
2. 還是不行，把錯誤畫面截圖，寫下你做到第幾步，貼到課程群組。
3. 課前沒做完很常見，上課前 10 分鐘教師與助教會協助你。

**選做：** 想先看看課程的互動教材，可以參考 [Git 與 GitHub 入門](git_intro.md) 最後的說明，把課程 repo 複製到電腦。
