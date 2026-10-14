# 第 2 週手把手實作：Pickle Charm Shop 上線、註冊、下訂單

本週以全班一起做的 [pickle-charm-shop](https://github.com/cychiang-ntpu/pickle-charm-shop)（皮克敏吊飾商店）繼續往下做。今天結束時，這個商店會：

1. 放在 Netlify 上，任何人用手機都打得開。
2. 有「註冊／登入」：訪客留下姓名與 Email，之後打開網站會顯示「歡迎回來，〔姓名〕」。
3. 有「真正的下訂單」：訪客選商品、填收件資料、按下送出，訂單會出現在你的 Netlify 後台，而且可以設定收到 Email 通知。

[提示詞](pickle_charm_prompts.md)　｜　[一頁版步驟清單](pickle_charm_steps.md)　｜　[疑難排解手冊](../../docs/tutorials/error_guide.md)　｜　[Windows 與 macOS 差異](../../docs/tutorials/windows_vs_macos.md)

---

## 先看這裡：今天的三件事在架構裡的位置

| 今天做的 | 它是什麼 | 資料存在哪裡 |
| --- | --- | --- |
| Netlify 上線 | 把 GitHub 上的檔案變成公開網站 | GitHub（檔案）、Netlify（網站） |
| 註冊／登入 | 註冊資料送到 Netlify Forms；「已登入」的狀態記在訪客自己的瀏覽器（LocalStorage） | Netlify 後台（名單）＋ 訪客瀏覽器（登入狀態） |
| 下訂單 | 訂單內容以表單送到 Netlify Forms，你在後台看得到每一筆 | Netlify 後台 |

**提醒：** 今天的「登入」是示範用的模擬登入，沒有密碼、沒有驗證。真正的會員系統需要伺服器端的帳號服務（例如 Supabase Auth），這在本課程範圍之外。訂單也沒有付款功能，收到訂單後要用其他方式收款。

| 時間 | 段落 | 完成後你會有 |
| --- | --- | --- |
| 0:00 | Part 0 準備（10 分鐘） | 自己電腦上有一份能提交、同步的 pickle-charm-shop |
| 0:10 | Part 1 Netlify 上線（15 分鐘） | 一個 `*.netlify.app` 網址，手機打得開（檢核點 3） |
| 0:25 | Part 2 註冊與登入（35 分鐘） | 後台收到註冊資料；重新整理後仍顯示「歡迎回來」（檢核點 4、5） |
| 1:00 | Part 3 真正的下訂單（40 分鐘） | 後台收到訂單，含商品、數量、金額、收件資料 |
| 1:40 | Part 4 Email 通知與自動更新（10 分鐘） | 有訂單時收到 Email；改版後網站自動更新（檢核點 6） |
| 1:50 | Part 5 收尾（10 分鐘） | 互相下單測試；寫出場券 |

**上課方式：** 兩人一組，一人操作（駕駛）、一人唸步驟（導航員），每個 Part 交換。每一步做完先對照「完成後你應該看到」。

---

## Part 0：準備（0:00–0:10）

這一段確保你的電腦上有一份自己的 pickle-charm-shop，而且之後能提交、同步到你自己的 GitHub。

### 步驟 1：把老師的 repo 複製成你自己的（Fork）（約 3 分鐘）

老師的 repo 你沒有修改權限，所以要先在你的 GitHub 帳號下複製一份。

1. 打開 <https://github.com/cychiang-ntpu/pickle-charm-shop>。
2. 按右上角的 **Fork** 按鈕。
3. 在出現的頁面中，**Owner** 選你自己的帳號，其他不用改，按綠色的 **Create fork**。

**完成後你應該看到：** 網址變成 `github.com/你的帳號/pickle-charm-shop`，左上角寫著「forked from cychiang-ntpu/pickle-charm-shop」。

**如果不一樣：** 顯示「already exists」→ 你之前已經 fork 過，直接到 `github.com/你的帳號/pickle-charm-shop` 即可。

### 步驟 2：Clone 到你的電腦（約 5 分鐘）

1. 打開 VS Code。如果已經開著其他資料夾，按 **檔案（File）→ 關閉資料夾（Close Folder）**。
2. 點左側 **原始檔控制（Source Control）** 圖示（樹枝分岔的形狀）。
3. 按 **複製存放庫（Clone Repository）** → **從 GitHub 複製（Clone from GitHub）**。
4. 在清單中點選 `你的帳號/pickle-charm-shop`（注意是你自己的，不是 cychiang-ntpu 的）。
5. 選一個資料夾存放，按 **選取為存放庫目的地**。
6. 右下角出現提示時按 **開啟（Open）**；問是否信任作者時按 **是**。

**完成後你應該看到：** 左側檔案總管有 `index.html`、`script.js`、`styles.css`、`README.md` 四個檔案。

**如果不一樣：** 清單裡找不到 → 回到 GitHub 你的 fork 頁面，按綠色 **Code** 按鈕複製網址，貼到 VS Code 上方的輸入框按 Enter。已經用電腦教室電腦 clone 過、現在在自己電腦 → 一樣重做這一步即可，檔案都在 GitHub 上。

### 步驟 3：確認 Git 身分與 Copilot（約 2 分鐘）

1. 按 **檢視（View）→ 終端機（Terminal）**，輸入 `git config --global --list`，按 Enter。
2. 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）打開 Copilot 聊天面板。

**完成後你應該看到：** 終端機列出 `user.name` 與 `user.email`；Copilot 面板打開且模式選單可選 **Agent**。

**如果不一樣：** 沒有 user.name → 照 [課前準備清單](../../docs/tutorials/before_class.md) 步驟 5 設定（電腦教室電腦每次重開都要重設）。Copilot 要求登入 → [課前準備清單](../../docs/tutorials/before_class.md) 步驟 6、7。

---

## Part 1：Netlify 上線（0:10–0:25）

### 步驟 4：在 Netlify 匯入你的 fork（約 8 分鐘）

1. 打開 <https://app.netlify.com/>，用 GitHub 帳號登入（**Log in with GitHub**）。
2. 按 **Add new project** → **Import an existing project**。
3. 選 **GitHub**。第一次會跳出授權視窗：按 **Authorize Netlify**，接著選 **Only select repositories**，勾選 `pickle-charm-shop`，按 **Install**。
4. 在清單中點選 `pickle-charm-shop`。
5. 設定頁面：**Branch to deploy** 保持 `main`；**Build command** 與 **Publish directory** 都**留空**（網站只有靜態檔案，不需要建置）。
6. **Project name** 輸入一個好記的名字，例如 `pickle-charm-你的學號末三碼`。
7. 按 **Deploy**。等待約 30 秒。

**完成後你應該看到：** 頁面顯示 **Published**，上方有 `https://pickle-charm-xxx.netlify.app` 的網址。

**如果不一樣：** 清單裡沒有 `pickle-charm-shop` → 按清單下方的 **Configure the Netlify app on GitHub**，把這個 repo 勾進去。名字已被使用 → 換一個。

### 步驟 5：用手機驗收（約 3 分鐘）

1. 點網址，在電腦上打開商店。
2. 用 LINE 把網址傳給自己，手機打開。
3. 把網址貼到課程群組。

**完成後你應該看到：** 手機上看到皮克敏吊飾商店，和老師課堂上示範的一樣。

**這一步在架構中的位置：** 你剛完成了「版本控制（GitHub）→ 雲端託管（Netlify）」這條線。檢核點 3 完成。

### 步驟 6：開啟表單偵測（約 2 分鐘，為 Part 2、3 準備）

新建立的 Netlify 專案預設**不會**收表單資料，要先打開這個開關，等一下的註冊和訂單才收得到。

1. 在 Netlify 你的專案頁面，點左側 **Forms**。
2. 按 **Enable form detection**。

**完成後你應該看到：** 頁面顯示表單偵測已啟用，並提示下次部署後生效。

---

## Part 2：註冊與登入（0:25–1:00）

這一段把右上角原本沒作用的「登入」按鈕變成真的：按下去出現註冊表單，送出後資料進 Netlify 後台，網頁顯示「歡迎回來，〔姓名〕」，重新整理也不會消失。

### 步驟 7：請 Copilot 做出「加入會員」小視窗（約 10 分鐘）

這一段分三小步，每小步貼一段提示詞，貼完先看預覽再貼下一段。

1. 打開 Copilot 聊天面板，模式選 **Agent**。
2. 打開 [提示詞](pickle_charm_prompts.md)，先複製最上面的 **「約定」** 貼上，按 Enter（只做一次）。
3. 複製 **提示詞 1**，貼上，Enter。等它改完，看一下變更，按 **保留（Keep）**。它問要不要執行指令時按 **Skip**。
4. 對 `index.html` 按右鍵 → **Show Preview**，按右上角 **登入**。

**完成後你應該看到：** 跳出「加入會員」小視窗，有姓名、Email 和送出按鈕。送出沒反應是正常的。

**如果不一樣：** Copilot 只在對話裡貼程式碼、沒改檔案 → 確認模式是 **Agent**，再送一次。

### 步驟 8：接上 Netlify、做出「歡迎回來」（約 6 分鐘）

1. 複製 **提示詞 2**（Netlify 設定，照抄即可）貼上 → Enter → **保留**。
2. 在 `index.html` 按 `Ctrl+F`（Mac：`⌘F`），搜尋 `data-netlify`。
3. 複製 **提示詞 3** 貼上 → Enter → **保留**。
4. 回到預覽，按「登入」填資料送出。

**完成後你應該看到：** 第 2 項找得到 `data-netlify`；第 4 項送出後出現「送出失敗」的字（因為還在本機，正常），表示失敗訊息也做好了。

**如果不一樣：** 找不到 `data-netlify` → 看 [提示詞](pickle_charm_prompts.md) 最下面「出問題時」第一列。

### 步驟 9：提交、同步（約 3 分鐘）

1. 點左側 **原始檔控制**。
2. 訊息框輸入 `新增註冊與登入`。
3. 按 **提交（Commit）**（問要不要全部暫存 → **是**）。
4. 按 **同步變更（Sync Changes）**。

**完成後你應該看到：** 同步按鈕消失；到 GitHub 你的 fork 頁面重新整理，最新一筆 commit 是「新增註冊與登入」。

### 步驟 10：等 Netlify 部署完成，在手機上註冊（約 5 分鐘）

1. 到 Netlify → 你的專案 → **Deploys**，等最新一筆變成 **Published**。
2. 用手機打開你的 netlify.app 網址（不要用電腦上的本機檔案）。
3. 按 **登入**，填姓名與 Email，送出。
4. 重新整理頁面。
5. 按「登出」，再重新整理。

**完成後你應該看到：** 送出後畫面顯示「歡迎回來，〔你的名字〕」；重新整理後仍顯示；登出後回到原本的「登入」按鈕。

**如果不一樣：** 送出後跳到 Netlify 的「Thank you」頁面 → 見 [疑難排解手冊](../../docs/tutorials/error_guide.md) Q16。送出失敗 → 確認用的是 netlify.app 網址，且步驟 6 已開啟表單偵測。

### 步驟 11：到後台看註冊名單（約 3 分鐘）

1. Netlify → 你的專案 → **Forms**。
2. 點 **signup**。

**完成後你應該看到：** 一筆資料，內容是你剛才填的姓名與 Email。

**這一步在架構中的位置：** 註冊資料走的是「前端 → Netlify Forms（後端即服務）」；「歡迎回來」則是存在手機瀏覽器裡的 LocalStorage。檢核點 4、5 完成。

請交換駕駛與導航員。

---

## Part 3：真正的下訂單（1:00–1:40）

這一段把「加入購物車」變成真的：按下後商品進入購物車，打開購物車可以改數量、看總金額，填收件資料後送出，訂單進 Netlify 後台。

### 步驟 12：請 Copilot 做出購物車（約 8 分鐘）

1. Copilot 聊天面板，**Agent** 模式（同一個對話繼續即可）。
2. 複製 **提示詞 4：真正的購物車** 貼上 → Enter → **保留**。
3. 預覽：對兩種商品各按一次「加入購物車」，再按右上角 **購物車**，按一次「＋」。

**完成後你應該看到：** 右上角數字變 2；面板列出兩項商品；按「＋」後數量與總金額跟著變；重新整理後購物車還在。

### 步驟 13：加上結帳表單與送出後畫面（約 9 分鐘）

1. 複製 **提示詞 5：結帳表單**（照抄即可）貼上 → Enter → **保留**。
2. `Ctrl+F` 搜尋 `data-netlify`，應該有兩處。
3. 複製 **提示詞 6：送出訂單後的畫面** 貼上 → Enter → **保留**。
4. 預覽：打開購物車，填收件姓名、電話、地址，按「送出訂單」。

**完成後你應該看到：** 面板下方有收件資料表單；本機送出會顯示「送出失敗」（正常）。購物車清空時「送出訂單」按鈕按不下去。

**如果不一樣：** 總金額不對或按鈕沒反應 → 按 `F12`（Mac：`⌥⌘I`）→ **Console**，把紅字複製貼給 Copilot，說「請修正這個錯誤」。

### 步驟 14：提交、同步、等部署（約 5 分鐘）

1. 原始檔控制 → 訊息 `新增購物車與下訂單` → **提交** → **同步變更**。
2. Netlify → **Deploys**，等 **Published**。

### 步驟 15：在手機上真正下一筆訂單（約 8 分鐘）

1. 手機打開你的 netlify.app 網址。
2. 加入兩種商品，打開購物車，調整數量。
3. 填收件資料，送出。

**完成後你應該看到：** 畫面顯示「訂單已送出」與訂單摘要（商品、數量、總金額）；購物車清空。

### 步驟 16：到後台看訂單（約 5 分鐘）

1. Netlify → **Forms** → **order**。
2. 點開那一筆。

**完成後你應該看到：** 欄位包含 `name`、`phone`、`address`、`items`（商品與數量的文字）、`total`（總金額）。如果已登入，還會有 `email`。

**這一步在架構中的位置：** 購物車內容暫存在瀏覽器（LocalStorage），送出時整筆訂單走「前端 → Netlify Forms」。社群平台的訂單系統多了付款、庫存、物流等服務，但「前端送出 → 後端收單 → 後台查看」這條線是一樣的。

請交換駕駛與導航員。

---

## Part 4：Email 通知與自動更新（1:40–1:50）

### 步驟 17：有訂單就寄信給你（約 4 分鐘）

1. Netlify → 你的專案 → 左側 **Forms**。
2. 找到 **Submission notifications**，按 **Add notification** → **Email notification**。
3. **Event to listen for** 選 **New form submission**；**Form** 選 `order`；填你的 Email；按 **Save**。
4. 用手機再下一筆測試訂單。

**完成後你應該看到：** 幾分鐘內收到一封主旨含「order」的 Email，內容是訂單欄位。

**如果不一樣：** 找不到 Submission notifications → 舊版介面在 **Project configuration → Notifications → Form submission notifications**。

### 步驟 18：改一處文字，看網站自動更新（約 6 分鐘）

1. 在 Copilot（Agent）貼上：`請把 #index.html 中「立即選購」按鈕的文字改成「馬上下單」，其他不變。` → **保留**。
2. 原始檔控制 → 訊息 `修改按鈕文字` → **提交** → **同步變更**。
3. **不要**到 Netlify 按任何東西。等約 30 秒，手機重新整理。

**完成後你應該看到：** 手機上的按鈕變成「馬上下單」。檢核點 6 完成。

---

## Part 5：收尾（1:50–2:00）

### 步驟 19：互相下單（約 5 分鐘）

1. 把網址貼到群組，到兩位同學的商店各下一筆訂單。
2. 回到自己的 Netlify → Forms → order，看收到幾筆。

### 步驟 20：出場券（約 5 分鐘）

寫在 [第 2 週學習單](worksheet.md) 第 5 部分：
1. 我的商店收到＿＿筆訂單。
2. 訂單資料存在哪裡？登入狀態存在哪裡？
3. 這個商店離「真的能營業」還缺什麼？（提示：付款、庫存、真正的帳號）

**下課前：** 瀏覽器登出 GitHub 與 Netlify；VS Code 左下角帳戶圖示 → 登出（公用電腦必做）。

---

## 課後作業（10/21 前）

**必做**
- [ ] 完成課堂未完成的步驟，確認手機能註冊、下單，後台看得到。
- [ ] 把 [學習歷程檔案範本](../../templates/portfolio_README.md) 貼進 `README.md`，填寫後提交、同步。
- [ ] 將網址貼到課程群組。

**選做**
- [ ] 請 Copilot 加一個「我的訂單」區塊：下單後把訂單摘要也存進 LocalStorage，重新整理後還看得到（提示詞見 [提示詞](pickle_charm_prompts.md) 的延伸提示詞）。
- [ ] 在 Netlify → Forms → order 匯出 CSV，用試算表算每種商品賣了幾個。
- [ ] 到 [作品牆](../../showcase/README.md) 登記。

**個資提醒：** 訂單含姓名、電話、地址，是他人的個人資料。只收必要欄位、不公開、不轉傳；課程結束後到 Netlify 後台刪除。截圖時遮住個資。

想了解表單與儲存的原理（選讀）：[表單、儲存與 CI/CD](../../docs/deep_dive/forms_storage_cicd.md)。
