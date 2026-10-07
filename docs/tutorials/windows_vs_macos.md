# 課堂用 Windows、回家用 macOS：操作差異對照

課堂在電腦教室的 Windows 桌機上進行；回家用 macOS 練習時，大部分步驟完全一樣，只有下面幾處不同。遇到教材寫 `Ctrl` 的地方，Mac 一律改成 `⌘`。

[回教學目錄](README.md)　｜　[課前準備清單](before_class.md)　｜　[第 1 週課後作業](../../lectures/wk01_1007_saas-storefront/homework.md)

---

## 1. 先懂一件事：你的檔案在 GitHub 上，不在電腦教室的電腦裡

電腦教室的桌機通常**重開機就會還原**，你在課堂上存在那台電腦的檔案會消失。這正是今天最後一定要「提交並同步」的原因：同步之後，`index.html` 就存在 GitHub 上，回家在任何電腦（Windows 或 Mac）都能取回來繼續做。

回家後的第一件事，不是找 USB 或檔案，而是在自己的電腦上安裝好軟體，然後把 repo 從 GitHub **clone** 下來（見第 4 節）。

---

## 2. 安裝軟體的差異

| 項目 | Windows（課堂桌機已裝好） | macOS（回家自己裝） |
| --- | --- | --- |
| VS Code | 下載安裝檔，一直按下一步 | 下載 `.zip`，解壓縮後把 **Visual Studio Code** 拖進「應用程式」資料夾。第一次打開若問「確定要打開嗎？」按 **打開** |
| Git | 下載安裝檔，全部預設值 | **不用另外下載。** 打開「終端機」（`⌘`＋`空白鍵`，輸入 `終端機`），輸入 `git --version` 按 Enter；跳出「需要命令列開發者工具」時按 **安裝**，等它完成（下載可能超過 10 分鐘） |
| 確認 Git 裝好 | VS Code 終端機輸入 `git --version` | 相同 |
| `git config` 兩行指令 | 貼到 VS Code 終端機 | 相同，貼到 VS Code 終端機或 macOS 終端機都可以 |
| 瀏覽器 | Edge 或 Chrome | Safari 或 Chrome 都可以；授權 GitHub 時若瀏覽器問「要打開 Visual Studio Code 嗎？」按 **允許** |

詳細步驟見 [課前準備清單](before_class.md) 步驟 3–5，裡面 Windows 與 macOS 已分開寫。

---

## 3. 快捷鍵對照

| 動作 | Windows | macOS |
| --- | --- | --- |
| 存檔 | `Ctrl+S` | `⌘S` |
| 複製、貼上、全選 | `Ctrl+C`、`Ctrl+V`、`Ctrl+A` | `⌘C`、`⌘V`、`⌘A` |
| 在檔案中搜尋（例如找 `data-netlify`） | `Ctrl+F` | `⌘F` |
| 打開原始檔控制 | `Ctrl+Shift+G` | `⌃⇧G`（Control＋Shift＋G，不是 ⌘） |
| 打開終端機 | `` Ctrl+` `` | `` ⌃` `` |
| 打開 Copilot 聊天 | `Ctrl+Alt+I` | `⌃⌘I` |
| 瀏覽器開發者工具（看 Local storage） | `F12` | `⌥⌘I` |
| 截圖（卡住時貼到群組） | `Win+Shift+S` | `⇧⌘4` |

快捷鍵記不住沒關係：所有動作都可以用滑鼠從 VS Code 的選單或左側圖示點到，教材的步驟都有寫按鈕位置。

---

## 4. 回家後怎麼接續今天的進度（約 10 分鐘，Mac 與 Windows 都適用）

前提：今天課堂上已完成「提交並同步」，GitHub 網頁上看得到你的 `index.html`。

1. 照 [課前準備清單](before_class.md) 步驟 3–7 在自己的電腦裝好 VS Code、Git，設定 `git config`，登入 GitHub，啟用 Copilot。
2. 打開 VS Code，點左側 **原始檔控制（Source Control）** 圖示。
3. 按 **複製存放庫（Clone Repository）** → **從 GitHub 複製（Clone from GitHub）**。
4. 選你的 repo（例如 `rent-radar`），選一個資料夾存放，按 **開啟（Open）**。

**完成後你應該看到：** VS Code 左側檔案總管出現 `index.html`，內容和你在課堂上做的一樣。

**如果不一樣：** 清單裡沒有你的 repo → 到 GitHub 網頁確認今天有同步成功（repo 頁面有 `index.html`）；若沒有，表示課堂上沒同步到，請從 [第 1 週課後作業](../../lectures/wk01_1007_saas-storefront/homework.md) A1 的檢查表重做。

之後每次換電腦，都是同一招：**clone**（第一次）或 **同步變更**（之後）。

---

## 5. 電腦教室桌機的兩個注意事項

1. **下課前一定要登出。** 公用電腦上的 GitHub、Netlify、VS Code 帳號登入狀態可能被下一位使用者看到。下課前：瀏覽器登出 GitHub 與 Netlify，VS Code 左下角帳戶圖示 → **登出（Sign Out）**。
2. **不要在公用電腦上保存復原碼或密碼。** 雙重驗證的復原碼請存到自己的手機或雲端硬碟。

---

## 6. macOS 使用者常見狀況

| 狀況 | 怎麼做 |
| --- | --- |
| 打開 VS Code 說「無法打開，因為來自未識別的開發者」 | 到「系統設定 → 隱私權與安全性」，往下找到該提示，按 **強制打開** |
| 終端機輸入 `git --version` 後一直沒反應 | 開發者工具還在下載，等它完成；期間可以先做 GitHub、Netlify 帳號等不需要 Git 的步驟 |
| 教材寫按 `Ctrl` 沒有反應 | 改用 `⌘`（原始檔控制與終端機的快捷鍵例外，用 `⌃`，見第 3 節） |
| 雙擊 `index.html` 用 Safari 打開，畫面有點不同 | 正常；最終以手機和 Netlify 網址上看到的為準。想和課堂一致可改用 Chrome |
| 檔案總管在哪 | macOS 叫 **Finder**；教材寫「檔案總管」時，Mac 就是 Finder |
