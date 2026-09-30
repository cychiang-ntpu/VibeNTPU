# VS Code 與 GitHub Copilot 入門

> **預估時間**：安裝約 25 分鐘，閱讀概念約 20 分鐘
> **對應檢核點**：[檢核點 0：課前準備](before_class.md)
> **完成後你將具備**：程式碼編輯器（VS Code）、版本控制系統（Git）、AI 程式設計助理（GitHub Copilot）三項工具，並能說明它們各自的功能、運作原理與限制。

[← 回教學目錄](README.md)

---

## 1. 學習目標

1. 說明編輯器與整合開發環境（Integrated Development Environment, IDE）的差異，以及 VS Code 的「工作區」概念。
2. 區分 Git（版本控制工具）與 GitHub（雲端代管平台）。
3. 以非技術語言說明 GitHub Copilot 的運作原理：大型語言模型如何根據上下文預測程式碼，以及它為何可能出錯。
4. 分辨 Copilot 的 Ask 與 Agent 模式，並能在 Agent 模式下審查變更與拒絕不必要的指令。
5. 了解 Copilot 的方案與額度、隱私風險與負責任使用原則。
6. 完成安裝，並以 Copilot 產生第一個網頁。

## 2. 核心概念

### 2.1 編輯器、IDE 與 VS Code

- **文字編輯器（text editor）**：用來開啟與修改純文字檔案的軟體，例如 Windows 記事本。網頁的原始碼（HTML、CSS、JavaScript）本質上就是純文字檔。
- **程式碼編輯器（code editor）**：專為程式碼設計的編輯器，提供語法上色、自動縮排、錯誤提示、搜尋取代等功能。
- **整合開發環境（IDE）**：將編輯器、除錯器、終端機、版本控制、建置工具整合在同一個應用程式中的開發環境。

**Visual Studio Code（VS Code）** 是 Microsoft 開發的免費、開放原始碼程式碼編輯器，本身輕量，但可透過延伸模組（extension）擴充成接近 IDE 的功能。它在多項開發者調查中長期是使用率最高的編輯器之一。本課程選用 VS Code 的原因是：(1) 免費且跨平台；(2) 內建 Git 圖形介面，不需輸入指令即可完成版本控制；(3) GitHub Copilot 以 VS Code 為主要整合環境。

課堂上可將 VS Code 比喻為「廚房工作台」：所有食材（檔案）與工具（終端機、預覽、AI 助理）都在同一個檯面上操作。

### 2.2 工作區與資料夾（Workspace／Folder）

VS Code 以「**資料夾**」為工作單位，而不是單一檔案。當你以「檔案 → 開啟資料夾」開啟一個資料夾時，該資料夾就成為目前的**工作區（workspace）**：

- 左側「檔案總管」顯示的是這個資料夾內的所有檔案。
- 「原始檔控制」面板偵測的是這個資料夾是否為 Git 儲存庫。
- Copilot 在 Agent 模式下建立或修改的檔案，會放在這個資料夾中；它能參考的專案內容，也以這個資料夾為範圍。

因此，**開錯資料夾或沒有開啟任何資料夾，是初學者最常見的問題來源**：Copilot 不知道檔案該放在哪裡，原始檔控制也找不到儲存庫。

**工作區信任（Workspace Trust）**：首次開啟資料夾時，VS Code 會詢問「是否信任此資料夾的作者」。這是安全機制：來源不明的專案可能包含會自動執行的設定或腳本。自己建立的資料夾與自己 clone 的 repo 可選擇信任；來源不明的下載檔案則應謹慎。

### 2.3 Git 與 GitHub

| | Git | GitHub |
| --- | --- | --- |
| 性質 | 版本控制系統（Version Control System, VCS），一套安裝在本機的軟體 | 以 Git 為基礎的雲端代管平台（網站與服務） |
| 開發者 | 2005 年由 Linus Torvalds 為管理 Linux 核心開發而建立，開放原始碼 | GitHub 公司，2018 年起為 Microsoft 所有 |
| 功能 | 記錄檔案的每一次修改（commit），可比較、還原、分支 | 在雲端保存儲存庫，並提供協作（Issue、Pull Request）、自動化（Actions）、網頁瀏覽等功能 |
| 是否需要網路 | 不需要，可完全離線記錄版本 | 需要 |

簡言之，Git 是工具，GitHub 是使用 Git 的服務之一（其他類似服務還有 GitLab、Bitbucket）。詳細的 Git 概念模型見 [Git 與 GitHub 入門](git_intro.md)。

### 2.4 GitHub Copilot 的運作原理

**GitHub Copilot** 是 GitHub 推出的 AI 程式設計助理，在 VS Code 中以程式碼補全與對話（Copilot Chat）兩種形式提供協助。

**運作機制（高層次）**：

1. **大型語言模型（Large Language Model, LLM）**：Copilot 背後是以大量文字與程式碼訓練的語言模型。模型的核心能力是「根據前文，預測接下來最可能出現的文字（token）」。產生程式碼時，它是在逐段預測「在這個上下文中，最合理的程式碼是什麼」。
2. **上下文（context）**：送給模型的內容不只是你輸入的一句話，還包括 Copilot 自動收集的資訊，例如目前開啟的檔案、游標附近的程式碼、你以 `#` 指定的檔案、工作區中相關的檔案，以及先前的對話內容。上下文越完整、越精確，產出通常越符合需求。
3. **提示詞（prompt）**：你以自然語言描述的需求。明確說明目標、限制與驗收條件（例如「手機寬度下三張卡片改為上下排列」），比模糊的描述（例如「弄好看一點」）更容易得到可用的結果。
4. **回應與套用**：模型產生文字回應或檔案變更，由 VS Code 顯示為差異（diff），等待你決定保留或復原。

**它為何可能出錯**：語言模型產生的是「統計上合理」的內容，而非經過驗證的正確答案。因此它可能：

- 產生語法正確但邏輯錯誤的程式碼，或與需求不符的功能。
- 引用不存在的函式、套件或設定（常稱為「幻覺」，hallucination）。
- 採用過時的寫法，或忽略安全性（例如未處理使用者輸入）。
- 在同一個需求下，每次產生的結果都不同（輸出具有隨機性）。

所以，**AI 產出的程式碼必須經過人的檢查與測試**。在本課程中，最低限度的檢查是：預覽畫面是否如預期、在手機寬度下是否正常、功能實際操作是否可用。

### 2.5 Ask 模式與 Agent 模式

Copilot Chat 的輸入框附近有模式選單。不同版本的 VS Code 名稱可能略有差異，本課程主要使用以下兩種：

| 模式 | 行為 | 適用情境 | 風險 |
| --- | --- | --- | --- |
| **Ask（詢問）** | 只在聊天面板中回答問題或提供程式碼片段，不會修改檔案 | 理解概念、詢問錯誤原因、請它解釋某段程式碼 | 低 |
| **Agent（代理）** | 自主規劃步驟，可**建立與修改多個檔案**，也可能**提議執行終端機指令** | 依需求建立或修改網頁 | 較高：可能一次改動多處，或提議執行你不了解的指令 |

部分版本另有 **Edit（編輯）** 模式，行為介於兩者之間：可修改你指定的檔案，但不會自主執行指令。

**Agent 模式的審查原則**：

1. **先看差異，再按 Keep。** Agent 完成後，VS Code 會以顏色標示新增（綠）與刪除（紅）的內容。請至少確認：改了哪些檔案、是否刪除了你原本需要的內容。確認無誤再按 **Keep（保留）**；不滿意則按 **Undo（復原）**。
2. **拒絕不必要的終端機指令。** Agent 有時會提議執行指令（例如安裝套件、執行 git），並請你按 **Continue／Allow**。本課程**不需要**讓 Copilot 執行任何指令，檔案的提交與同步由你透過原始檔控制面板完成。遇到此類請求時按 **Skip／Cancel**，並告訴它：「請不要執行任何指令，只修改檔案。」
3. **一次一個主題。** 將大需求拆成數個小步驟，每步驟確認後再進行下一步；換新主題時開新對話，避免舊對話的上下文干擾。

### 2.6 方案與使用額度

| 方案 | 費用 | 說明 |
| --- | --- | --- |
| **Copilot Free** | 免費 | 每月有程式碼補全與聊天請求的次數上限；可選用的模型較少。足以完成本課程 |
| **Copilot Pro** | 付費；**通過驗證的學生可免費使用** | 額度較高、可選模型較多。學生可透過 [GitHub Education](https://education.github.com/) 申請學生身分驗證，審核需數天 |

方案內容、額度與價格會隨時間調整，請以官方 [Copilot 方案頁面](https://github.com/features/copilot/plans) 為準。

**節省額度的方法**：一次將需求說清楚（可使用課程的 [提示詞產生器](../../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html)），比反覆要求小幅修改更有效率；單純的文字修改（例如改標題）可以直接在編輯器中手動完成。

### 2.7 隱私與資料安全

使用 Copilot 時，你的提示詞與相關的檔案內容會被傳送到雲端服務進行處理。GitHub 針對不同方案有不同的資料使用政策（例如是否保留提示詞、是否用於改進產品），個人帳號可在 GitHub 的 Copilot 設定頁面調整部分選項。無論政策如何，請遵守以下原則：

- **不要在提示詞或工作區檔案中放入個人資料**：例如自己或他人的身分證字號、電話、住址、學號與成績。
- **不要放入機密資訊（secrets）**：例如密碼、API 金鑰、存取權杖（token）。這些資訊一旦進入公開 repo 或被傳送到外部服務，就應視為已外洩。
- **測試用資料請使用虛構內容**：例如「王小明、test@example.com」。
- **留意工作區範圍**：Agent 模式可讀取工作區內的檔案。請只開啟本課程的專案資料夾，不要以整個「文件」或「桌面」資料夾作為工作區。

### 2.8 負責任使用

1. **你對提交的程式碼負責。** AI 產生的內容一旦由你 Commit，就是你的作品，你需要能說明它大致在做什麼。
2. **理解優先於產出。** 遇到看不懂的程式碼，請改用 Ask 模式請它逐段解釋，這是本課程重要的學習方式。
3. **注意授權與出處。** AI 可能產生與既有公開程式碼相似的內容；使用圖片、字型、文案時，也應確認授權。
4. **不要用於處理真實敏感資料的正式系統，除非經過專業審查。** Vibe coding 適合原型與最小可行產品（MVP）；涉及金流、個資的正式產品需要專業工程師檢視安全性。
5. **遵守課程的學術誠信規範。** 反思與心得等文字作業應反映你自己的思考。

## 3. 操作步驟

### 3.1 安裝 VS Code

1. 前往 <https://code.visualstudio.com/> 下載（網站會自動判斷作業系統）。
2. 安裝：
   - **Windows**：依安裝精靈進行。建議勾選「**將『以 Code 開啟』動作加入 Windows 檔案總管的右鍵選單**」與「**加入 PATH**」，方便日後從檔案總管與終端機開啟。
   - **macOS**：將下載的 `Visual Studio Code.app` 拖入「應用程式」資料夾。
3. 開啟 VS Code。若需要中文介面：按左側 **延伸模組**（四個方塊的圖示），搜尋 `Chinese (Traditional)`，安裝 Microsoft 出品的語言套件後依提示重新啟動。

官方說明：[VS Code 設定入門](https://code.visualstudio.com/docs/setup/setup-overview)｜[VS Code 入門影片](https://code.visualstudio.com/docs/getstarted/introvideos)

### 3.2 安裝 Git

- **Windows**：前往 <https://git-scm.com/downloads/win> 下載安裝程式，全部選項保持預設即可。
- **macOS**：開啟「終端機」App，輸入 `git --version` 後按 Enter。若系統提示需要安裝「指令列開發者工具（Command Line Tools）」，按「安裝」並等待完成。

安裝完成後**完全關閉並重新開啟 VS Code**（VS Code 在啟動時偵測 Git 的位置），按 `` Ctrl+` ``（Mac：`` ⌃` ``）開啟下方的終端機，輸入：

```
git --version
```

顯示 `git version 2.x.x` 即表示安裝成功。

### 3.3 設定 Git 使用者資訊（只需一次）

每一個 commit 都會記錄作者姓名與 Email，因此首次使用前須設定。在終端機輸入以下兩行（將引號內換成你的資料）：

```
git config --global user.name "你的名字或暱稱"
git config --global user.email "你註冊 GitHub 的 Email"
```

`--global` 表示此設定套用於這台電腦上的所有儲存庫。

**隱私選項**：commit 中的 Email 在公開 repo 中任何人都看得到。若不想公開真實 Email，可至 GitHub → **Settings → Emails**，勾選 **Keep my email addresses private**，GitHub 會提供一個 `數字+帳號@users.noreply.github.com` 形式的地址，將它填入上方的 `user.email` 即可。GitHub 仍會將這些 commit 正確歸屬到你的帳號。

官方說明：[設定 commit 的 Email 地址](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

### 3.4 在 VS Code 登入 GitHub

1. 點 VS Code **左下角的帳戶圖示（人像）** → **使用 GitHub 登入以使用 GitHub Copilot**（或 Sign in with GitHub）。
2. 瀏覽器會開啟 GitHub 授權頁面 → 按 **Authorize Visual-Studio-Code** → 瀏覽器詢問是否開啟 VS Code 時，按「開啟」。
3. 回到 VS Code，帳戶圖示中應顯示你的 GitHub 帳號名稱。

此授權採用 OAuth 流程：你在 GitHub 網站上確認授權，GitHub 發給 VS Code 一組存取權杖，VS Code 之後以此代表你存取 Copilot 與 repo，而不需要知道你的密碼。

### 3.5 啟用 GitHub Copilot

1. 點 VS Code 上方標題列或下方狀態列的 **Copilot 圖示**，選擇 **Set up Copilot／使用 Copilot**。
2. 若尚未擁有 Copilot 方案，選擇 **GitHub Copilot Free**；若已通過學生驗證，系統會自動套用 Copilot Pro。
3. 完成後按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）或點 Copilot 圖示，側邊會開啟 **Copilot Chat** 面板。

官方說明：[在 VS Code 設定 Copilot](https://code.visualstudio.com/docs/copilot/setup)

### 3.6 安裝 Live Preview 延伸模組

1. 開啟 **延伸模組** 面板（`Ctrl+Shift+X`，Mac：`⌘⇧X`）。
2. 搜尋 `Live Preview`，安裝 **Microsoft** 出品的版本（注意發行者名稱，避免安裝名稱相似的第三方套件）。
3. 之後在 `index.html` 上按右鍵 → **Show Preview**，VS Code 會在側邊顯示網頁預覽，檔案存檔後自動重新整理。

Live Preview 會在本機啟動一個小型網頁伺服器（網址類似 `http://127.0.0.1:3000`），只有你的電腦能存取。未安裝時，也可以直接在檔案總管雙擊 `index.html`，以瀏覽器開啟（網址會以 `file:///` 開頭）。

### 3.7 第一個練習：以 Copilot 產生 Hello NTPU 頁面

1. 在桌面建立新資料夾，命名為 `hello-ntpu`。
2. VS Code → **檔案 → 開啟資料夾**（File → Open Folder）→ 選擇 `hello-ntpu`。詢問是否信任作者時，選擇 **是，我信任作者**（這是你自己建立的資料夾）。
3. 開啟 Copilot Chat（`Ctrl+Alt+I`／`⌃⌘I`），將模式設為 **Agent**。若你的版本沒有 Agent，選擇 **Edit**。
4. 輸入以下提示詞並送出：
   ```text
   我是沒有程式設計經驗的大學生。請在這個資料夾建立一個 index.html：
   1. 畫面中央顯示「Hello NTPU」標題與一行自我介紹
   2. 背景使用柔和的漸層色，文字與背景要有足夠對比
   3. 在手機寬度下也能正常顯示（加入 viewport 設定）
   4. 使用 UTF-8 編碼
   只需要建立檔案，不要執行任何終端機指令。
   ```
5. Copilot 完成後，左側檔案總管會出現 `index.html`。檢視差異內容，確認後按 **Keep（保留）**。
6. 在 `index.html` 上按右鍵 → **Show Preview**，或在檔案總管中雙擊開啟。
7. **觀察與驗證**：將預覽視窗拉窄，模擬手機寬度，確認排版是否正常。接著切換到 Ask 模式，詢問：「請用非技術語言解釋這個 index.html 的 `<head>` 區塊各行的用途。」

這個練習驗證了整條本機工具鏈可以運作，也讓你體驗「描述需求 → AI 產生 → 人工審查 → 驗證」的基本循環。

## 4. Copilot Chat 操作速查表

| 目的 | 操作方式 |
| --- | --- |
| 開啟聊天面板 | `Ctrl+Alt+I`（Mac：`⌃⌘I`），或點 Copilot 圖示 |
| 讓 AI 直接建立或修改檔案 | 模式選 **Agent**（或 Edit） |
| 只詢問、不修改檔案 | 模式選 **Ask** |
| 指定要參考或修改的檔案 | 在訊息中輸入 `#` 後選擇檔案，例如 `#index.html` |
| 接受或拒絕變更 | 檢視差異後按 **Keep（保留）** 或 **Undo（復原）** |
| 拒絕 AI 提議的終端機指令 | 按 **Skip／Cancel**，並要求它只修改檔案 |
| 開始新對話 | 聊天面板上方的 **＋**（新主題建議開新對話，避免舊上下文干擾） |
| 切換 AI 模型 | 輸入框附近的模型選單（Free 方案可選模型較少） |
| 開啟終端機 | `` Ctrl+` ``（Mac：`` ⌃` ``） |
| 開啟原始檔控制面板 | `Ctrl+Shift+G`（Mac：`⌃⇧G`） |
| 存檔 | `Ctrl+S`（Mac：`⌘S`） |

## 5. 自我檢核

- [ ] VS Code 可正常開啟
- [ ] 終端機中 `git --version` 顯示版本號
- [ ] 已設定 `user.name` 與 `user.email`（如需要，已改用 noreply 地址）
- [ ] VS Code 左下角帳戶圖示顯示自己的 GitHub 帳號
- [ ] Copilot Chat 可開啟並回應
- [ ] 已安裝 Microsoft 出品的 Live Preview
- [ ] 已以 Copilot 產生 Hello NTPU 網頁並完成預覽

## 6. 討論與延伸思考

1. 同一段提示詞送出兩次，Copilot 可能產生不同的程式碼。這對「驗收」有什麼影響？你會如何確認結果符合需求？
2. Agent 模式能自主修改多個檔案並提議執行指令。便利性與可控性之間，你會如何取捨？在什麼情況下你會選擇 Ask 模式？
3. 若你的創業產品未來要處理使用者個資，哪些部分你會交給 AI 產生，哪些部分你認為必須由專業人員審查？

## 7. 參考資料

- [VS Code：Copilot 總覽](https://code.visualstudio.com/docs/copilot/overview)
- [VS Code：Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)
- [VS Code：提示詞撰寫技巧](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting)
- [VS Code：Workspace Trust](https://code.visualstudio.com/docs/editing/workspaces/workspace-trust)
- [GitHub Copilot 文件](https://docs.github.com/zh/copilot)
- [GitHub Copilot 方案](https://github.com/features/copilot/plans)
- [GitHub Education](https://education.github.com/)

遇到問題請查閱 [疑難排解手冊](error_guide.md#3-vs-codegitcopilot)。下一篇：[Git 與 GitHub 入門](git_intro.md)。
