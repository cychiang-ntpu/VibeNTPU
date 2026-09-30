# 疑難排解手冊

本手冊整理本課程常見的技術問題，依工具分類，每題以「症狀／可能原因／處理步驟」的格式撰寫。遇到本手冊未涵蓋的狀況時，請先依第 2 節的一般除錯方法自行診斷。

初學者在設定開發環境與第一次部署時遇到問題屬正常現象。軟體開發工作中有相當比例的時間用於診斷問題，能有系統地找出原因，本身就是重要的能力。

[← 回課程首頁](../../README.md)　｜　[教學目錄](README.md)

---

## 1. 如何使用本手冊

1. **搜尋關鍵字**：按 `Ctrl+F`（Mac：`⌘F`），輸入錯誤訊息中的關鍵字，例如 `Page not found`、`rejected`、`亂碼`。
2. **對照症狀**：確認你看到的現象與題目描述一致，再依「處理步驟」逐項檢查。每完成一步就重新測試一次。
3. **15 分鐘求助原則**：自行嘗試 15 分鐘仍無法解決時，請求助：課堂上舉起紅色回饋卡、詢問同組或鄰組同學、在課程群組發問，或開立一張 [求助單](https://github.com/cychiang-ntpu/VibeNTPU/issues/new?template=help_request.yml)。求助時請依第 2.6 節提供完整資訊。
4. **記錄與反思**：解決後，將問題、原因與解法簡要記錄在 [學習歷程檔案](../../templates/portfolio_README.md) 的反思中。

### 題號索引

| 分類 | 題號 |
| --- | --- |
| [VS Code／Git／Copilot](#3-vs-codegitcopilot) | Q1–Q10 |
| [Netlify 部署](#4-netlify-部署) | Q11–Q13 |
| [Netlify Forms](#5-netlify-forms) | Q14–Q16 |
| [LocalStorage](#6-localstorage) | Q17–Q18 |

---

## 2. 一般除錯方法

除錯（debugging）是找出並修正問題根本原因的過程。以下方法適用於本課程所有工具，也適用於日後任何技術問題。

### 2.1 重現問題（reproduce）

先確認問題能穩定出現：在什麼操作之後、在哪個環境（本機預覽或 Netlify 網址、電腦或手機、哪個瀏覽器）會發生。能穩定重現的問題才能有效診斷，也才能確認修正是否有效。

### 2.2 閱讀錯誤訊息

錯誤訊息是系統提供的線索，而非指責。請完整閱讀，特別注意：

- **錯誤類型與關鍵字**：例如 `rejected`、`404`、`permission denied`、`Uncaught TypeError`。
- **發生位置**：檔案名稱與行號，例如 `index.html:42`。
- **英文訊息可直接搜尋**：將錯誤訊息的關鍵部分貼到搜尋引擎或 AI 助理中，通常能找到相同案例。

### 2.3 隔離問題（isolate）

縮小問題範圍，判斷問題出在哪一個環節：

| 檢查點 | 若正常，代表 | 若異常，代表 |
| --- | --- | --- |
| 本機預覽是否正常 | 程式碼大致無誤，問題可能在上傳或部署 | 問題在程式碼本身 |
| GitHub 網頁上是否看得到最新 commit | 推送成功，問題在 Netlify 或瀏覽器 | 問題在 Commit 或 Sync |
| Netlify Deploys 最新一筆是否為 Published | 部署成功，問題可能在快取或程式碼 | 問題在部署設定，請閱讀部署紀錄 |
| 無痕視窗中是否正常 | 問題可能是瀏覽器快取或 LocalStorage 舊資料 | 問題在網站本身 |

### 2.4 一次只改一個地方

每次只做一項修改，並立即測試。同時修改多處時，即使問題解決，也無法得知是哪項修改生效；若情況變糟，也難以回復。請 Copilot 修改時亦同：一次只提出一個需求，並在按 Keep 之前檢視差異。

### 2.5 使用瀏覽器開發者工具（DevTools）

瀏覽器內建的開發者工具是檢查網頁問題的主要工具。按 `F12`（Mac：`⌘⌥I`）開啟：

| 分頁 | 用途 |
| --- | --- |
| **Console（主控台）** | 顯示 JavaScript 錯誤與訊息。紅色文字為錯誤，通常附有檔案名稱與行號 |
| **Elements（元素）** | 檢視網頁的 HTML 結構與套用的 CSS，可即時試改樣式 |
| **Network（網路）** | 檢視每個請求的狀態碼，例如表單送出後是否回傳 200，或圖片是否為 404 |
| **Application（應用程式）** | 檢視與刪除 LocalStorage 等瀏覽器端儲存的資料 |
| **裝置模擬（Toggle device toolbar）** | 以手機尺寸預覽網頁 |

將 Console 中的紅色錯誤訊息完整複製給 Copilot，比只描述「網頁壞了」更容易得到正確的修正建議。

### 2.6 附上上下文求助

無論是詢問 AI、同學或助教，請提供以下資訊：

1. **預期結果**：你原本希望看到什麼。
2. **實際結果**：實際發生了什麼，附上完整錯誤訊息或截圖。
3. **重現步驟**：你做了哪些操作之後出現問題。
4. **已嘗試的做法**：你已經試過哪些方法、結果如何。
5. **相關連結**：GitHub repo 網址、Netlify 網址。

範例：「我預期按下『加入早鳥名單』後，Netlify 後台會出現一筆資料。實際上頁面跳到 Thank you 頁，但後台 Forms 頁面是空的。我已確認 `<form>` 有 `data-netlify="true"`，也重新部署過。網址是 https://xxx.netlify.app ，repo 是 https://github.com/xxx/xxx 。」

---

## 3. VS Code／Git／Copilot

### Q1. Copilot Chat 無法開啟、要求登入，或顯示已達使用上限

**症狀**：點 Copilot 圖示沒有反應、要求登入，或回覆訊息顯示已達到每月使用額度。

**可能原因**：
- VS Code 尚未以 GitHub 帳號登入，或授權已過期。
- 尚未啟用 Copilot 方案。
- Copilot Free 方案的每月額度已用完。

**處理步驟**：
1. 點 VS Code 左下角帳戶圖示，確認已以 GitHub 帳號登入；未登入時依 [VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md#34-在-vs-code-登入-github) 操作。
2. 點 Copilot 圖示選擇 **Set up Copilot**，確認已啟用 Copilot Free 或 Pro。
3. 若已達額度上限：
   - 改用 [提示詞產生器](../../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html) 一次描述完整需求，減少往返次數；簡單的文字修改直接手動編輯。
   - 申請 [GitHub Education](https://education.github.com/) 學生身分驗證，通過後可免費使用 Copilot Pro。
   - 臨時替代方案：改用網頁版 AI 助理（例如 [Claude](https://claude.ai/)、[ChatGPT](https://chatgpt.com/)、[Gemini](https://gemini.google.com/)），將產生的程式碼貼入 VS Code 的 `index.html` 並存檔（`Ctrl+S`），之後一樣以 Commit＋Sync 上傳。提示詞產生器可切換為這些服務的版本。使用時同樣不要貼入個人資料或機密。

### Q2. Copilot 只在聊天視窗顯示程式碼，沒有建立或修改檔案

**症狀**：Copilot 回覆了一段程式碼，但左側檔案總管沒有新檔案，`index.html` 也沒有變化。

**可能原因**：
- 模式設為 **Ask**，此模式只回答、不修改檔案。
- VS Code 沒有開啟任何資料夾，Copilot 無處放置檔案。
- 提示詞未明確要求修改檔案。

**處理步驟**：
1. 將聊天輸入框附近的模式切換為 **Agent**（或 Edit）。
2. 確認左側檔案總管顯示你的專案資料夾；若是空的，以「檔案 → 開啟資料夾」開啟。
3. 在提示詞中明確寫出：「請直接建立（或修改）工作區中的 `index.html`」，或以 `#index.html` 指定檔案。

### Q3. Copilot 要求執行終端機指令（Continue／Allow）

**症狀**：Agent 模式顯示一段指令，並請你按 **Continue**、**Allow** 或 **Run**。

**可能原因**：Agent 模式會自主規劃步驟，有時判斷需要安裝套件、啟動伺服器或執行 git 指令。

**處理步驟**：
1. 本課程**不需要**讓 Copilot 執行任何終端機指令。按 **Skip** 或 **Cancel**。
2. 回覆：「請不要執行任何指令，也不要執行 git，只修改檔案。」
3. 提交與同步請自行透過原始檔控制面板完成，這樣你能清楚掌握哪些內容被上傳。

### Q4. Copilot 修改後結果變差，想回到先前狀態

**症狀**：Copilot 修改後網頁排版錯亂、功能消失，或不符合需求。

**可能原因**：AI 依統計推測產生程式碼，可能誤解需求或一次改動過多內容。

**處理步驟**（依目前狀態選擇）：
1. **尚未按 Keep**：在 Chat 中按 **Undo（復原）**。
2. **已按 Keep，尚未 Commit**：原始檔控制 → 在 `index.html` 旁按 **↶ 捨棄變更（Discard Changes）**，檔案會回到最後一次 commit 的內容。此操作無法復原。
3. **已 Commit**：見 [Git 與 GitHub 入門：查看歷史與還原修改](git_intro.md#5-查看歷史與還原修改)。
4. 預防：養成「每完成一個可運作的步驟就 Commit」的習慣，確保隨時有可回復的版本。

### Q5. 終端機找不到 git，或原始檔控制面板要求下載 Git

**症狀**：終端機輸入 `git --version` 顯示「找不到命令」或類似訊息；原始檔控制面板顯示「下載 Git」按鈕。

**可能原因**：Git 尚未安裝；或已安裝，但 VS Code 在安裝前就已啟動，尚未偵測到 Git。

**處理步驟**：
1. Windows：至 <https://git-scm.com/downloads/win> 下載安裝，選項全部維持預設。macOS：在「終端機」App 輸入 `git --version`，依提示安裝指令列開發者工具。
2. **完全關閉 VS Code 後重新開啟**（Windows 請確認所有 VS Code 視窗皆已關閉）。
3. 再次輸入 `git --version` 確認。

### Q6. Commit 時要求設定 user.name 與 user.email

**症狀**：按提交時出現「Make sure you configure your user.name and user.email in git」或類似訊息。

**可能原因**：尚未設定 Git 使用者資訊。每個 commit 都必須記錄作者。

**處理步驟**：
1. 在 VS Code 終端機（`` Ctrl+` ``）輸入以下兩行，換成你的資料：
   ```
   git config --global user.name "你的名字"
   git config --global user.email "你的 GitHub Email"
   ```
2. 若不想公開真實 Email，可改用 GitHub 提供的 noreply 地址，見 [VS Code 與 GitHub Copilot 入門](vscode_copilot_starter.md#33-設定-git-使用者資訊只需一次)。
3. 重新按一次提交。

### Q7. 找不到「同步變更（Sync Changes）」按鈕

**症狀**：原始檔控制面板中沒有同步變更按鈕。

**可能原因與處理步驟**：

| 你看到的畫面 | 原因 | 處理 |
| --- | --- | --- |
| 有「提交」按鈕，但沒有同步 | 尚未 Commit，本機沒有待推送的 commit | 先完成 Commit，按鈕會顯示為「同步變更 ↑1」 |
| 顯示「發佈分支（Publish Branch）」 | 資料夾是本機建立的 repo，尚未連接 GitHub | 按「發佈分支」並選擇 **Public**，建立新的 GitHub repo；或依 [Git 與 GitHub 入門：建立 repo](git_intro.md#41-在-github-建立-repo) 重新 clone，再將 `index.html` 複製進去 |
| 顯示「目前開啟的資料夾沒有 Git 存放庫」 | 開啟的不是 clone 下來的資料夾 | 以「檔案 → 開啟資料夾」選擇正確的資料夾 |

### Q8. Sync 失敗：rejected、驗證失敗或反覆要求登入

**症狀**：按同步變更後出現 `rejected`、`Authentication failed`，或不斷跳出登入視窗。

**可能原因**：
- **rejected**：GitHub 上有本機沒有的 commit（例如曾在 GitHub 網頁上編輯 README），Git 拒絕推送以避免覆蓋他人的變更。
- **驗證失敗**：VS Code 登入的 GitHub 帳號與 repo 擁有者不同，或授權已失效。

**處理步驟**：
1. rejected：再按一次 **同步變更**，VS Code 會先 pull 整合遠端變更再 push。
2. 若出現**合併衝突**，依 [Git 與 GitHub 入門](git_intro.md) 第 3.6 節處理；不確定時請求助助教，不要反覆按同步。
3. 驗證失敗：點左下角帳戶圖示，確認登入的是擁有該 repo 的帳號；必要時登出後重新授權。

### Q9. 預覽空白、中文亂碼，或結果與預期不同

**症狀**：預覽畫面空白；中文顯示為亂碼；畫面與你描述的需求不一致。

**可能原因與處理步驟**：
1. **空白**：檔案可能尚未存檔（編輯器分頁標題旁的實心圓點表示未存檔），按 `Ctrl+S`（Mac：`⌘S`）。仍空白時，按 `F12` 開啟 Console 查看是否有紅色錯誤，將錯誤訊息貼給 Copilot。
2. **亂碼**：確認 `<head>` 中有 `<meta charset="UTF-8">`，且 VS Code 右下角狀態列顯示 `UTF-8`。
3. **與預期不同**：這是 AI 輔助開發的常態，需要「檢視結果 → 具體回饋 → 再修改」的迭代。回饋越具體越有效：
   - 不具體：「不好看，重做。」
   - 具體：「標題字級放大為目前的兩倍；背景改為淺米色；三張功能卡片在寬度小於 600px 時改為上下排列。」

### Q10. GitHub 要求輸入雙重驗證碼

**症狀**：登入 GitHub 時要求輸入 6 位數驗證碼，或要求設定雙重驗證。

**可能原因**：GitHub 要求提交程式碼的帳號啟用雙重驗證（2FA）。

**處理步驟**：
1. 依畫面指示，以手機驗證 App 掃描 QR Code 完成設定。
2. **下載並妥善保存復原碼**；手機遺失時需要復原碼才能登入。
3. 官方說明：[設定雙重驗證](https://docs.github.com/zh/authentication/securing-your-account-with-two-factor-authentication-2fa/configuring-two-factor-authentication)

---

## 4. Netlify 部署

### Q11. 網站顯示「Page not found」

**症狀**：開啟 `https://xxx.netlify.app` 時顯示 Netlify 的 `Page not found` 頁面。

**可能原因**：
- 首頁檔名不是全小寫的 `index.html`（例如 `Index.html`、`index.htm`）。Netlify 的伺服器區分大小寫。
- `index.html` 位於子資料夾，而非 repo 最外層。
- Publish directory 設定為不存在或錯誤的資料夾。

**處理步驟**：
1. 在 GitHub 網頁上確認 `index.html` 的檔名與位置。
2. 若有誤，在 VS Code 中更名或移到最外層後 Commit＋Sync。
3. 在 Netlify → **Project configuration → Build & deploy** 確認 Publish directory 為空白。

### Q12. 在 Netlify 找不到我的 GitHub repo

**症狀**：Netlify 匯入專案時的 repo 清單中沒有你要的 repo。

**可能原因**：安裝 Netlify GitHub App 時選擇了 Only select repositories，但未勾選此 repo（例如 repo 是之後才建立的）。

**處理步驟**：
1. 在 repo 清單下方點 **Configure the Netlify app on GitHub**。
2. 在 GitHub 設定頁面將新的 repo 加入授權範圍並儲存。
3. 回到 Netlify 重新整理清單。

### Q13. GitHub 已更新，但網站沒有變化

**症狀**：已在 VS Code 修改並提交，但開啟網站仍是舊版。

**可能原因**：commit 未推送、Netlify 未收到通知或部署失敗、瀏覽器快取。

**處理步驟**（依資料流順序檢查）：
1. **GitHub**：開啟 repo 網頁，確認最新 commit 是否出現。若沒有，表示只按了 Commit、未按 **同步變更（Sync）**。
2. **Netlify**：至 **Deploys** 頁面查看最新一筆。若為 **Failed**，點開閱讀部署紀錄；若完全沒有新紀錄，專案可能是以 Netlify Drop 拖曳建立，未與 GitHub 連接，請改以 **Import from Git** 重新建立。
3. **瀏覽器**：強制重新整理（Windows：`Ctrl+Shift+R`；Mac：`⌘⇧R`），或以無痕視窗開啟；手機可下拉重新整理。

---

## 5. Netlify Forms

以下三題對應第 2 週的表單串接，概念說明見 [Netlify Forms 教學](netlify_forms.md)。

### Q14. Netlify 後台的 Forms 頁面沒有顯示我的表單

**症狀**：已部署含表單的網頁，但 Netlify 的 Forms 頁面是空的，或只顯示啟用提示。

**可能原因**：Netlify 是在**部署時**掃描 HTML 原始碼來偵測表單。若掃描功能未開啟、開啟後尚未重新部署，或表單不在 HTML 原始碼中，就不會被偵測到。

**處理步驟**（依序檢查）：
1. **表單偵測是否已啟用**：新專案預設關閉。至 Forms 頁面按 **Enable form detection**。
2. **啟用後是否重新部署**：至 **Deploys** → **Trigger deploy** → **Deploy project**，或推送一個新的 commit。
3. **`<form>` 標籤是否具備必要屬性**：須有 `data-netlify="true"` 與 `name` 屬性（例如 `name="waitlist"`）。
4. **表單是否由 JavaScript 動態產生**：若表單是頁面載入後才由 JavaScript 插入，部署時的 HTML 中並不存在，Netlify 無法偵測。請要求 Copilot 將 `<form>` 直接寫在 HTML 中。

官方說明：[Netlify Forms 疑難排解](https://docs.netlify.com/manage/forms/troubleshooting-tips/)

### Q15. 表單送出成功，但後台沒有資料

**症狀**：頁面顯示送出成功，但 Forms 頁面中沒有新的提交紀錄。

**可能原因**：
- 在本機（`file:///` 或 `127.0.0.1`）測試，資料沒有送到 Netlify。
- 提交被判定為垃圾訊息，例如填寫了隱藏的 honeypot 欄位。
- 以 JavaScript（AJAX）送出時，缺少 `form-name` 欄位或其值與表單名稱不符。

**處理步驟**：
1. 確認是在 `https://xxx.netlify.app` 上測試，而非本機預覽。
2. 至 Forms → 該表單 → **Spam submissions** 查看是否被歸類為垃圾訊息。
3. 以 AJAX 送出時，確認送出的資料中包含 `form-name` 欄位，且其值與 `<form name="...">` 完全相同。
4. 按 `F12` 開啟 Network 分頁，重新送出一次，確認請求的狀態碼是否為 200；若為 404 或其他錯誤，將完整資訊貼給 Copilot。

### Q16. 送出後跳到 Netlify 的 Thank you 頁面，未顯示會員儀表板

**症狀**：按下送出後，頁面跳轉到 Netlify 預設的感謝頁，而不是在原頁面切換為會員儀表板。

**可能原因**：表單以瀏覽器預設方式送出（整頁跳轉），JavaScript 沒有攔截送出事件（缺少 `event.preventDefault()`），也沒有改以 AJAX（`fetch`）送出。

**處理步驟**：
1. 使用 [第 2 週提示詞集](../../lectures/wk02_1014_baas-cicd/prompts.md) 中「送出後在原頁面切換為會員儀表板」的提示詞，請 Copilot 改為 AJAX 送出。
2. 修改後 Commit＋Sync，待部署完成後在 Netlify 網址上重新測試。
3. 確認 Q15 所述的 `form-name` 欄位仍然存在，否則改為 AJAX 後可能出現 Q15 的症狀。

---

## 6. LocalStorage

概念說明見 [LocalStorage 教學](localstorage.md)。

### Q17. 換一台裝置或瀏覽器開啟網站，歡迎畫面消失

**症狀**：在電腦上已顯示會員歡迎畫面，但用手機或其他瀏覽器開啟時，又回到未加入狀態。

**可能原因**：這是 LocalStorage 的預期行為，而非錯誤。LocalStorage 的資料儲存在**每個瀏覽器自己的空間**中，依網域分開保存，不會在裝置或瀏覽器之間同步，也不會傳送到伺服器。

**處理步驟**：
1. 無須修正。這正是 LocalStorage 的限制之一：它適合保存個人偏好等非關鍵資料，無法作為跨裝置的會員系統。
2. 若產品需要跨裝置保存狀態，需要伺服器端的資料庫與登入機制（例如後端即服務 BaaS 的身分驗證功能），此為課程延伸內容。

### Q18. 想重新測試表單，但一直顯示歡迎畫面

**症狀**：已送出過表單，重新開啟網站時直接顯示會員儀表板，無法再次測試表單流程。

**可能原因**：LocalStorage 中仍保留先前的會員資料。

**處理步驟**（任選一種）：
1. 按儀表板上的「登出」按鈕（若有實作，通常會呼叫 `localStorage.removeItem` 清除資料）。
2. 按 `F12` → **Application** → **Local storage** → 選擇你的網址 → 刪除相關項目。
3. 以無痕視窗開啟網站；無痕視窗關閉後其 LocalStorage 即被清除。

---

## 7. 參考資料

- [MDN：什麼是瀏覽器開發者工具](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools)
- [Chrome DevTools 文件](https://developer.chrome.com/docs/devtools)
- [VS Code：原始檔控制](https://code.visualstudio.com/docs/sourcecontrol/overview)
- [Netlify Support Forums](https://answers.netlify.com/)
- [GitHub Docs：關於合併衝突](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts)
