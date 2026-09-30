# 🧰 VS Code ＋ GitHub Copilot 入門：打造你的 AI 工作室

> ⏱️ 約 25 分鐘（多半在等下載）｜🥚 這是 [Q0 報到任務](before_class.md) 的主要內容
> 做完這一篇，你的電腦就有了：**一個專業的編輯器（VS Code）＋ 一位 AI 工程師（Copilot）＋ 一台存檔機（Git）**。

[← 回教學目錄](README.md)

---

## 🍱 先用比喻搞懂這三樣東西

| 工具 | 美食街比喻 | 它在做什麼 |
| --- | --- | --- |
| 🧰 **VS Code** | 你的**廚房工作台** | 全世界工程師最常用的免費編輯器，打開資料夾、看檔案、預覽網頁都在這裡 |
| 🤖 **GitHub Copilot** | 工作台旁的 **AI 主廚助理** | 你用中文說想要什麼，它直接幫你寫好、改好檔案 |
| 💾 **Git** | 工作台上的**存檔機＋傳真機** | 幫每一版設計圖存檔，並把它傳到 GitHub 總部 |

> 💡 **為什麼不用網頁版的 ChatGPT 就好？** 網頁版 AI 只能「給你一段程式碼」，你要自己複製、存檔、上傳。
> Copilot 住在 VS Code 裡，**看得到你的檔案、可以直接幫你改**，改完你用 VS Code 一鍵存檔上傳，這才是真實工程師的工作方式。

---

## 步驟 1：安裝 VS Code 🧰

1. 前往 <https://code.visualstudio.com/> 下載（網站會自動判斷你的作業系統）。
2. 安裝：
   - **Windows**：一路按「下一步」。建議勾選「**將『以 Code 開啟』動作加入 Windows 檔案總管的右鍵選單**」和「**加入 PATH**」。
   - **macOS**：把下載的 `Visual Studio Code.app` 拖進「應用程式」資料夾。
3. 打開 VS Code。想要中文介面？按左側的 **延伸模組**（四個方塊圖示），搜尋 `Chinese (Traditional)`，安裝後依提示重新啟動。

📖 官方說明：[VS Code 設定入門](https://code.visualstudio.com/docs/setup/setup-overview)｜[VS Code 入門影片](https://code.visualstudio.com/docs/getstarted/introvideos)

## 步驟 2：安裝 Git 💾

- **Windows**：前往 <https://git-scm.com/downloads/win> 下載安裝，**全部保持預設值一路下一步**即可。
- **macOS**：打開「終端機」App，輸入 `git --version` 按 Enter。如果跳出「需要安裝指令列開發者工具」，按「安裝」並等它完成。

裝好後**重新開啟 VS Code**，按 `` Ctrl+` ``（Mac：`` ⌃` ``）打開下方的「終端機」，輸入：

```
git --version
```

看到 `git version 2.x.x` 就成功了 🎉

### 第一次使用：跟 Git 自我介紹（只需做一次）

每個存檔點都會記錄「是誰存的」，所以要先告訴 Git 你是誰。在同一個終端機貼上這兩行（把引號裡的內容換成你的）：

```
git config --global user.name "你的名字或暱稱"
git config --global user.email "你註冊 GitHub 的 Email"
```

> 🔐 不想公開 Email？可以到 GitHub → Settings → Emails 勾選「Keep my email addresses private」，改用它給你的 `xxxx@users.noreply.github.com` 地址。
> 📖 [GitHub：設定 commit 的 Email](https://docs.github.com/zh/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-email-preferences/setting-your-commit-email-address)

## 步驟 3：在 VS Code 登入 GitHub 🔑

1. 點 VS Code **左下角的人像圖示（帳戶）** → **使用 GitHub 登入以使用 GitHub Copilot**（或 Sign in with GitHub）。
2. 瀏覽器會打開 GitHub 授權頁面 → 按 **Authorize Visual-Studio-Code** → 瀏覽器問要不要開啟 VS Code，按「開啟」。
3. 回到 VS Code，左下角人像圖示出現你的 GitHub 帳號名稱 ✅

## 步驟 4：啟用 GitHub Copilot 🤖

1. 點 VS Code 上方標題列的 **Copilot 圖示**（或左下角狀態列的 Copilot 圖示），選 **Set up Copilot／使用 Copilot**。
2. 如果你還沒有 Copilot 方案，選 **GitHub Copilot Free（免費版）** 即可。
3. 完成後，按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）或點上方的 Copilot 圖示，右側會打開 **Copilot Chat（聊天）** 面板。

| 方案 | 費用 | 適合誰 |
| --- | --- | --- |
| **Copilot Free** | 免費，每月有使用次數上限 | 這門課夠用 👍 |
| **Copilot Pro（學生免費）** | 通過 [GitHub Education](https://education.github.com/) 學生身分驗證後免費 | 想要更多次數的同學（驗證需要幾天，請提早申請） |

📖 官方說明：[在 VS Code 設定 Copilot](https://code.visualstudio.com/docs/copilot/setup)｜[Copilot 方案比較](https://github.com/features/copilot/plans)

> ⚠️ **次數省著用**：免費版每月的聊天次數有限。一次把需求說清楚（用咒語產生器！），比一直小改省很多次數。

## 步驟 5：安裝預覽工具 Live Preview 👀

1. 按左側 **延伸模組**（`Ctrl+Shift+X`，Mac：`⌘⇧X`）。
2. 搜尋 `Live Preview`，安裝 **Microsoft** 出品的那一個。
3. 之後在 `index.html` 上按右鍵 → **Show Preview**，VS Code 右邊就會出現網頁預覽，改檔案時會自動重新整理。

> 不裝也可以：在檔案總管（Finder）裡雙擊 `index.html`，用瀏覽器打開也行。

---

## 步驟 6：⭐ 你的第一次成功，請 Copilot 做一個網頁

1. 在桌面建立一個新資料夾，取名 `hello-ntpu`。
2. VS Code → **檔案 → 開啟資料夾**（File → Open Folder）→ 選 `hello-ntpu`。
   - 如果問「是否信任此資料夾的作者？」→ 選 **是，我信任作者**。
3. 打開 Copilot Chat（`Ctrl+Alt+I`／`⌃⌘I`），在輸入框上方的模式選單選 **Agent（代理）**。
   > 你的版本沒有 Agent？選 **Edit（編輯）** 也可以。
4. 貼上這段話送出：
   ```text
   你好！我是完全沒寫過程式的大學生。請在這個資料夾建立一個 index.html，
   顯示「Hello NTPU 👋」，背景是漂亮的漸層色，文字置中，要支援手機。
   ```
5. Copilot 會開始工作，並在左側出現 `index.html`。看一下它改了什麼，按 **Keep（保留）** 接受變更。
6. 在 `index.html` 上按右鍵 → **Show Preview**（或到資料夾雙擊打開）。

🎉 **看到畫面了嗎？恭喜，這是你在「真正的工程師工具」裡，用 AI 做出的第一個網頁！**

> 🧠 **為什麼要先做這一步？** 心理學研究發現，「親身成功過一次」是建立「我做得到」信心最有效的方法。

---

## 🤖 Copilot Chat 使用小抄

| 你想做什麼 | 怎麼做 |
| --- | --- |
| 打開聊天 | `Ctrl+Alt+I`（Mac：`⌃⌘I`）或點上方 Copilot 圖示 |
| 讓 AI **直接改檔案** | 模式選 **Agent**（或 Edit） |
| 只想**問問題**、不改檔案 | 模式選 **Ask** |
| 指定要改哪個檔案 | 在訊息裡打 `#` 選檔案，例如 `#index.html` |
| 接受／拒絕 AI 的修改 | 按 **Keep（保留）** 或 **Undo（復原）** |
| 開新對話 | 聊天面板上方的 **＋**（換新主題時開新對話，AI 比較不會搞混） |
| 換 AI 模型 | 輸入框下方的模型選單（免費版可選的模型較少） |

> ⚠️ **Copilot 要求「執行指令」時**：Agent 模式有時會說要在終端機執行指令並請你按 **Continue／Allow**。
> 這門課**不需要**讓它執行任何指令。看不懂它要做什麼時，按 **Skip／Cancel**，並跟它說「請不要執行指令，只要修改檔案就好」。

📖 延伸學習：[Copilot Chat 官方說明](https://code.visualstudio.com/docs/copilot/chat/copilot-chat)｜[VS Code 的 Copilot 總覽](https://code.visualstudio.com/docs/copilot/overview)

---

## ✅ 檢查清單

- [ ] VS Code 裝好並能打開
- [ ] `git --version` 看得到版本號
- [ ] 已設定 `user.name` 和 `user.email`
- [ ] VS Code 左下角看得到自己的 GitHub 帳號
- [ ] Copilot Chat 打得開
- [ ] 安裝了 Live Preview
- [ ] ⭐ Copilot 幫我做出 Hello NTPU 網頁

卡住了？👉 [卡關急救手冊](error_guide.md#-vs-code--git--copilot)　｜　下一篇 👉 [Git 與 GitHub 入門](git_intro.md)
