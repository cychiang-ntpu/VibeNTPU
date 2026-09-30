# VS Code 與 GitHub Copilot 入門

> **預估時間**：約 45 分鐘（大部分是下載與安裝）
> **對應檢核點**：檢核點 0（課前準備），完整流程見 [課前準備清單](before_class.md)
> **做完你會得到**：一台可以寫網頁、用 AI 幫忙、並把作品存到 GitHub 的電腦。

[← 回教學目錄](README.md)　｜　[課前準備清單](before_class.md)　｜　[疑難排解手冊](error_guide.md)

---

## 開始之前

本篇是 [課前準備清單](before_class.md) 步驟 3 到步驟 9 的詳細版，步驟編號與課前準備清單相同。步驟 1、2（申請 GitHub 帳號、申請學生方案）請先在課前準備清單完成。

先認識三個名詞：

- **VS Code**：寫網頁用的軟體，像是一張工作桌，檔案、預覽和 AI 助理都在同一個畫面裡。
- **Git**：裝在電腦裡的「存檔紀錄」工具，會記住你每一次的修改。
- **GitHub Copilot**：在 VS Code 裡面的 AI 助理，你用中文描述需求，它幫你寫程式碼。

想了解原理（編輯器與 IDE 的差別、Copilot 如何運作、限制與隱私）：見 [Git、Copilot 與部署機制（選讀）](../deep_dive/git_and_copilot.md)。

---

## 步驟 3：安裝 VS Code（約 10 分鐘）

這一步要把 VS Code 裝到電腦上。做完後，你會有一個可以開啟與編輯網頁檔案的軟體。

### Windows

1. 打開瀏覽器，前往 <https://code.visualstudio.com/>。
2. 按頁面上藍色的 **Download for Windows** 按鈕。
3. 打開下載好的安裝檔（檔名類似 `VSCodeUserSetup-x64-....exe`）。
4. 選擇 **我接受合約（I accept the agreement）**，按 **下一步（Next）**。
5. 在「選擇附加的工作」畫面，勾選 **將「以 Code 開啟」動作加入 Windows 檔案總管檔案的操作功能表** 與 **加入 PATH**。
6. 按 **安裝（Install）**，等待完成。
7. 按 **完成（Finish）**，VS Code 會自動開啟。

### macOS

1. 打開瀏覽器，前往 <https://code.visualstudio.com/>。
2. 按 **Download for Mac**。
3. 打開「下載項目」資料夾，找到 `Visual Studio Code.app`（若是 `.zip` 檔，先雙擊解壓縮）。
4. 把 `Visual Studio Code.app` 拖到左側的「應用程式」資料夾。
5. 打開「應用程式」資料夾，雙擊 **Visual Studio Code**。
6. 若出現「這是從網際網路下載的 App，確定要打開嗎？」，按 **打開**。

### 換成中文介面（選做）

1. 在 VS Code 最左邊那一排圖示中，點選四個小方塊組成的圖示（**延伸模組，Extensions**）。
2. 在上方搜尋框輸入 `Chinese (Traditional)`。
3. 找到發行者為 **Microsoft** 的「中文(繁體)」語言套件，按 **Install**。
4. 右下角出現提示時，按 **Change Language and Restart**。

**完成後你應該看到：** VS Code 開啟，畫面中間是「歡迎使用（Welcome）」頁面，最左邊有一排直向的圖示。

**如果不一樣：** Windows 出現「Windows 已保護您的電腦」→ 按 **其他資訊** → **仍要執行**。其他狀況見 [VS Code 官方安裝說明](https://code.visualstudio.com/docs/setup/setup-overview)。

---

## 步驟 4：安裝 Git 並確認（約 10 分鐘）

Git 負責記錄每一次修改。VS Code 左側的「原始檔控制」功能需要 Git 才能運作。

### Windows

1. 前往 <https://git-scm.com/downloads/win>。
2. 按 **Click here to download** 下載安裝檔。
3. 打開安裝檔（檔名類似 `Git-2.xx.x-64-bit.exe`），出現權限詢問時按 **是**。
4. 之後每一個畫面都**不要改任何選項**，一直按 **Next**。
5. 最後一個畫面按 **Install**，等待完成。
6. 按 **Finish**。

### macOS

1. 按 `⌘`＋`空白鍵` 打開 Spotlight 搜尋，輸入 `終端機`（或 `Terminal`），按 Enter。
2. 在打開的視窗中輸入下面這一行，按 Enter：
   ```
   git --version
   ```
3. 若跳出「需要指令列開發者工具」的視窗，按 **安裝**，再按 **同意**。
4. 等待下載安裝完成（約 5–10 分鐘），按 **完成**。

### 確認安裝成功（Windows、macOS 都要做）

1. **完全關閉 VS Code**，再重新打開。（VS Code 只在啟動時尋找 Git。）
2. 在 VS Code 上方選單點選 **檢視 > 終端機（View > Terminal）**，或按 `` Ctrl+` ``（Mac：`` ⌃` ``，是鍵盤左上角 Esc 下方那個鍵）。
3. 畫面下方會出現一個可以打字的區域，這就是**終端機**（用打字方式下指令給電腦的地方）。
4. 在終端機輸入下面這一行，按 Enter：
   ```
   git --version
   ```

**完成後你應該看到：** 終端機顯示類似 `git version 2.47.1` 的文字（數字不同沒關係）。

**如果不一樣：** 顯示「找不到命令」或「not recognized」→ 確認已完全關閉所有 VS Code 視窗後重新打開，再試一次；仍不行請看 [疑難排解手冊](error_guide.md) Q5。

---

## 步驟 5：設定你的名字與 Email（約 2 分鐘）

每一次存檔紀錄（commit）都會寫上作者是誰，所以 Git 需要知道你的名字與 Email。這個設定整台電腦只要做一次。

1. 在 VS Code 打開終端機：**檢視 > 終端機（View > Terminal）**，或按 `` Ctrl+` ``。
2. 複製下面第一行，把 `你的名字或暱稱` 換成你的名字（英文或中文都可以，引號要保留），貼到終端機後按 Enter：
   ```
   git config --global user.name "你的名字或暱稱"
   ```
3. 複製下面第二行，把 `你註冊GitHub的Email` 換成你申請 GitHub 時用的 Email，貼到終端機後按 Enter：
   ```
   git config --global user.email "你註冊GitHub的Email"
   ```
4. 輸入下面這一行並按 Enter，檢查剛才的設定：
   ```
   git config --global --list
   ```

**完成後你應該看到：** 畫面列出 `user.name=你的名字` 與 `user.email=你的Email` 兩行。按 Enter 後沒有任何訊息是正常的，代表設定成功。

**如果不一樣：** 名字打錯 → 重新執行第 2 或第 3 項，新的設定會蓋掉舊的。不想讓 Email 公開 → 見 [Git、Copilot 與部署機制（選讀）](../deep_dive/git_and_copilot.md) 中「公開 repo 的資安責任」一節。

---

## 步驟 6：在 VS Code 登入 GitHub（約 3 分鐘）

登入後，VS Code 才能使用 Copilot，也才能把檔案上傳到你的 GitHub。

1. 在 VS Code **左下角**找到人像形狀的圖示（**帳戶，Accounts**），點一下。
2. 在跳出的選單中點選 **使用 GitHub 登入以使用 GitHub Copilot**（英文介面為 **Sign in with GitHub to use GitHub Copilot**）。
3. 瀏覽器會自動打開 GitHub 的授權頁面。若尚未登入 GitHub，先輸入帳號、密碼與驗證 App 上的 6 位數驗證碼。
4. 按綠色的 **Authorize Visual-Studio-Code** 按鈕。
5. 瀏覽器詢問「要開啟 Visual Studio Code 嗎？」時，按 **開啟**。
6. 回到 VS Code。

**完成後你應該看到：** 再點一次左下角的帳戶圖示，選單中會顯示你的 GitHub 帳號名稱。

**如果不一樣：** 瀏覽器沒有跳回 VS Code → 手動切換回 VS Code，通常已完成登入；若沒有，重做一次第 1 項。

---

## 步驟 7：啟用 GitHub Copilot Free（約 3 分鐘）

這一步讓 AI 助理開始運作。免費方案（Copilot Free）就足以完成本課程。

1. 在 VS Code 最上方標題列的中間偏右，找到 Copilot 圖示（一個小小的機器人臉）。也可以在最下方狀態列右側找到同樣的圖示。
2. 點一下圖示，選擇 **使用 Copilot（Set up Copilot）**，或按 **Sign in to use Copilot for free** 之類的按鈕（不同版本字樣略有差異）。
3. 若詢問方案，選擇 **GitHub Copilot Free**。已通過學生方案驗證的同學會自動套用 Copilot Pro，不必再選。
4. 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）打開聊天面板。
5. 在聊天面板下方的輸入框輸入 `你好`，按 Enter。

**完成後你應該看到：** 畫面側邊出現 **Copilot Chat（聊天）** 面板，Copilot 用文字回覆了你。

**如果不一樣：** 找不到圖示或一直要求登入 → 先確認步驟 6 已完成；也可以用瀏覽器前往 <https://github.com/settings/copilot> 啟用 Copilot Free，再回到 VS Code。顯示已達使用上限 → 見 [疑難排解手冊](error_guide.md) Q1。

---

## 步驟 8：安裝 Live Preview 預覽工具（約 2 分鐘）

Live Preview 讓你在 VS Code 裡直接看到網頁長什麼樣子，存檔後會自動更新。

1. 在 VS Code 最左邊那一排圖示中，點選四個小方塊組成的圖示（**延伸模組，Extensions**），或按 `Ctrl+Shift+X`（Mac：`⌘⇧X`）。
2. 在搜尋框輸入 `Live Preview`。
3. 找到發行者為 **Microsoft** 的那一個（名稱下方寫著 Microsoft，旁邊有藍色勾勾）。
4. 按 **安裝（Install）**。

**完成後你應該看到：** Live Preview 的頁面上，原本的「安裝」按鈕變成「解除安裝（Uninstall）」或齒輪圖示。

**如果不一樣：** 搜尋結果有好幾個名稱相似的套件 → 只裝發行者是 **Microsoft** 的版本。

---

## 步驟 9：第一個練習，用 Copilot 做出 Hello NTPU 網頁（約 10 分鐘）

這一步會用 AI 做出你的第一個網頁。做完代表你的電腦已經準備好上課了。

1. 在桌面上按右鍵，建立一個新資料夾，命名為 `hello-ntpu`。
2. 在 VS Code 上方選單點選 **檔案 > 開啟資料夾（File > Open Folder）**。
3. 選擇桌面上的 `hello-ntpu`，按 **選擇資料夾（Select Folder）**（Mac：**打開**）。
4. 出現「您信任此資料夾中檔案的作者嗎？」時，按 **是，我信任作者（Yes, I trust the authors）**。這是你自己建立的資料夾，可以放心信任。
5. 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）打開 Copilot 聊天面板。
6. 在輸入框下方找到模式選單（可能顯示 Ask 或 Agent），點一下，選擇 **Agent**。
7. 複製下面整段提示詞，貼到輸入框，按 Enter 送出：
   ```text
   我是沒有程式設計經驗的大學生。請在這個資料夾建立一個 index.html：
   1. 畫面中央顯示「Hello NTPU」標題與一行自我介紹
   2. 背景使用柔和的漸層色，文字與背景要有足夠對比
   3. 在手機寬度下也能正常顯示（加入 viewport 設定）
   4. 使用 UTF-8 編碼
   只需要建立檔案，不要執行任何終端機指令。
   ```
8. 等 Copilot 完成。若它請你按 **Continue** 或 **Allow** 執行指令，按 **Skip**（略過）。
9. 看到左側檔案總管出現 `index.html` 後，在聊天面板中按 **保留（Keep）**。
10. 在左側 `index.html` 上按右鍵，選擇 **Show Preview**（顯示預覽）。

**完成後你應該看到：** VS Code 右半邊出現一個預覽畫面，中央寫著「Hello NTPU」，背景是漸層色。

**如果不一樣：**

- Copilot 只在聊天視窗貼出程式碼，沒有建立檔案 → 模式選成 Ask 了，改選 **Agent** 再送一次（見 [疑難排解手冊](error_guide.md) Q2）。
- 右鍵選單沒有 Show Preview → 確認步驟 8 已安裝；或直接到桌面的 `hello-ntpu` 資料夾，雙擊 `index.html` 用瀏覽器開啟。
- 預覽空白 → 按 `Ctrl+S`（Mac：`⌘S`）存檔後再看一次。

**這一步在架構中的位置：** 你剛剛完成了「在自己電腦上做出網頁」這一段。這個網頁目前只有你看得到；第 1 週會把它放上 GitHub，再用 Netlify 變成大家都能開的網站。

---

## Copilot 聊天使用方法

這一節整理上課最常用到的聊天操作。

### 打開聊天面板

- 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`），或點標題列上的 Copilot 圖示。

### 選擇模式

輸入框下方的模式選單可以切換：

- **Ask（詢問）**：只回答問題，不會改你的檔案。想問「這段是什麼意思」「為什麼出錯」時用它。
- **Agent（代理）**：會直接建立或修改檔案。想請它「幫我做出…」「幫我改成…」時用它。

### 看完再按保留或復原

1. Copilot 修改完後，檔案中新增的部分會標成綠色，刪除的部分會標成紅色。
2. 先看一下預覽，確認結果是你要的。
3. 滿意就按 **保留（Keep）**；不滿意就按 **復原（Undo）**，檔案會回到修改前的樣子。

### 指定要改哪一個檔案

1. 在輸入框中輸入 `#`。
2. 從跳出的清單選擇檔案，例如 `index.html`。
3. 接著輸入你的需求，例如：`#index.html 請把標題改成深藍色`。

### 開始新對話

- 換一個新主題時，按聊天面板上方的 **＋（新增聊天，New Chat）**。舊對話的內容太多時，Copilot 容易混淆。

### Copilot 要求執行指令時

1. Agent 模式有時會顯示一段指令，並請你按 **Continue**、**Allow** 或 **Run**。
2. 按 **Skip**（略過）或 **Cancel**（取消）。
3. 在輸入框回覆：`請不要執行任何指令，只修改檔案。`

本課程不需要讓 Copilot 執行任何指令，上傳到 GitHub 由你自己按按鈕完成。

---

## 使用小提醒

- **一次只要求一件事。** 例如先改標題，確認好了再改顏色。
- **描述要具體。** 「標題放大一倍、背景改淺米色」比「弄好看一點」更容易得到你要的結果。
- **看不懂就問。** 切到 Ask 模式問：「請用非技術語言解釋這段程式碼在做什麼。」
- **不要放個人資料或密碼。** 提示詞與檔案內容會送到雲端處理。測試時用虛構資料，例如 `王小明`、`test@example.com`。
- **只打開課程的專案資料夾。** 不要把整個「桌面」或「文件」資料夾當成工作資料夾。
- **額度用完時**：簡單的文字修改直接在檔案裡手動改；需要一次說清楚時，可用 [提示詞產生器](../../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html)。
- **你要為提交的內容負責。** AI 寫的程式碼可能有錯，一定要自己預覽、在手機寬度下看過再保留。

---

## 常用快捷鍵

| 目的 | Windows | Mac |
| --- | --- | --- |
| 打開 Copilot 聊天 | `Ctrl+Alt+I` | `⌃⌘I` |
| 打開終端機 | `` Ctrl+` `` | `` ⌃` `` |
| 打開原始檔控制 | `Ctrl+Shift+G` | `⌃⇧G` |
| 打開延伸模組 | `Ctrl+Shift+X` | `⌘⇧X` |
| 存檔 | `Ctrl+S` | `⌘S` |

---

## 完成檢查

- [ ] VS Code 可以正常打開
- [ ] 終端機輸入 `git --version` 會顯示版本號
- [ ] `git config --global --list` 顯示我的名字與 Email
- [ ] VS Code 左下角帳戶圖示顯示我的 GitHub 帳號
- [ ] Copilot 聊天面板可以打開並回覆
- [ ] 已安裝 Microsoft 出品的 Live Preview
- [ ] 已用 Copilot 做出 Hello NTPU 網頁並看到預覽

遇到問題請看 [疑難排解手冊](error_guide.md) Q1–Q10。下一篇：[Git 與 GitHub 入門](git_intro.md)。
