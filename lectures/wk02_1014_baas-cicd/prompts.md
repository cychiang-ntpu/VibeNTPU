# 第 2 週提示詞集：串接 BaaS 與模擬會員狀態

[← 回第 2 週講義](README.md)

---

## 1. 使用方式

1. 在 VS Code 開啟**上週 clone 的 repo 資料夾**（資料夾內應有 `index.html`）。
2. 開啟 Copilot Chat，將模式切換為 **Agent**。
3. 貼上提示詞並送出。提示詞中的 `#index.html` 會把該檔案加入對話脈絡，Agent 模式會直接修改檔案，不需要手動複製貼上程式碼。
4. 檢視 Copilot 呈現的差異（diff），確認無誤後按 **Keep**；不滿意可按 **Undo** 並修改提示詞重試。
5. 依第 4 節的驗證清單檢查，再到原始檔控制面板 **Commit＋Sync**。

需要依自己的產品填入內容時，可使用 [提示詞產生器](../wk01_1007_saas-storefront/slides/prompt_builder.html)，切換至「第 2 週」模式。

## 2. 撰寫提示詞的原則

有效的提示詞會明確寫出**角色、目標、限制條件與驗收標準**。本週的提示詞刻意把技術要求逐條列出，原因是生成式 AI 在沒有明確限制時，常會產生「看起來正確、但不符合特定平台規則」的程式碼（例如忘記 `name` 屬性，或以 JavaScript 動態產生表單）。這類錯誤不會出現錯誤訊息，只會表現為「後台收不到資料」，因此比明顯的錯誤更難排查。

---

## 3. 提示詞

### 3.1 提示詞 1：加入早鳥候補名單表單

模式：**Agent**

```text
你是一位資深前端工程師。請直接修改工作區中的 #index.html，
在網頁上新增一個「加入早鳥候補名單（Waitlist）」的區塊，要求如下：

【表單欄位】
1. 姓名（必填）
2. Email（必填，要檢查格式）
3. 身分（下拉選單：大學生 / 研究生 / 上班族 / 其他）
4. 你最期待的功能（選填，多行文字）

【Netlify Forms 串接（必須遵守）】
1. <form> 標籤必須加上 name="waitlist"、method="POST" 以及 data-netlify="true" 屬性。
2. 在表單內加入 <input type="hidden" name="form-name" value="waitlist" />。
3. 每個輸入欄位都要有 name 屬性。
4. 加入防機器人的 honeypot 欄位：在 <form> 加上 netlify-honeypot="bot-field"，
   並在表單內加入一個隱藏的 <input name="bot-field" />。
5. <form> 必須直接寫在 HTML 裡，不要用 JavaScript 動態產生。

【個資告知】
在表單下方加一段簡短說明：收集的資料僅用於產品上線通知，不會提供給第三方。

【其他要求】
- 導覽列和主視覺的 CTA 按鈕，點擊後要平滑捲動到這個表單。
- 風格要和原本的網頁一致，並支援手機版。
- 其他部分保持不變。
- 改完後請不要幫我執行 git 指令，我會自己用 VS Code 的原始檔控制存檔。
```

**各項技術要求的理由：**

| 要求 | 理由 |
| --- | --- |
| `name="waitlist"` | Netlify 以表單名稱建立後台中的表單項目；沒有名稱時，後台難以辨識，多個表單也無法區分 |
| `method="POST"` | 表單資料放在 HTTP 請求本文（body）中送出。若使用預設的 GET，資料會附加在網址上，既不會被 Netlify 接收，也可能留在瀏覽紀錄與伺服器日誌中 |
| `data-netlify="true"` | Netlify 在部署時解析 HTML，只有帶這個屬性（或 `netlify` 屬性）的表單會被登記並建立接收端點 |
| 隱藏欄位 `form-name` | Netlify 依據請求中的 `form-name` 值判斷資料屬於哪個表單。一般 HTML 送出時，Netlify 會在部署處理中自動補上此欄位；但提示詞 2 改以 JavaScript（AJAX）送出，必須由我們自行帶上，否則資料會被忽略 |
| 每個欄位都有 `name` | 瀏覽器只會送出有 `name` 的欄位，並以 `name=值` 的形式編碼；沒有 `name` 的欄位不會出現在後台 |
| honeypot 欄位 | 一個真人看不到、但自動化程式常會填寫的陷阱欄位；有值的送出會被視為垃圾訊息而過濾 |
| 表單直接寫在 HTML | Netlify 的偵測發生在部署時、讀取的是靜態 HTML 檔，不會執行 JavaScript；由 JavaScript 產生的表單不會被偵測到 |
| 個資告知 | 依個人資料保護法的精神，向當事人直接蒐集資料時應告知蒐集目的等事項（見 [Netlify Forms 講義](../../docs/tutorials/netlify_forms.md)） |
| 不要執行 git | 保留由學生自己在原始檔控制面板檢視差異、撰寫 Commit 訊息的步驟，確保你知道提交了什麼；Agent 模式可以執行終端機指令，若它自行 commit 或 push，你將失去這個檢查點 |

官方說明：[Netlify Forms setup](https://docs.netlify.com/manage/forms/setup/)

### 3.2 提示詞 2：送出後原地切換為會員儀表板

模式：**Agent**（在提示詞 1 的同一個對話中接續）

```text
請直接修改 #index.html，打造「模擬登入」的體驗：

1. 使用者按下送出後，網頁「不要跳轉到其他頁面」（攔截表單預設的送出行為）。
2. 請用 JavaScript 的 fetch()，以 AJAX 方式把表單資料送給 Netlify：
   - 送到 "/"，方法是 POST
   - Content-Type 為 "application/x-www-form-urlencoded"
   - 內容用 new URLSearchParams(new FormData(form)).toString() 產生
3. 只有在伺服器回應成功（response.ok）後，才把使用者輸入的「姓名」存進瀏覽器的 localStorage。
   不要把 Email 或其他個人資料存進 localStorage。
4. 表單區塊原地變成一個「會員儀表板」畫面，顯示：
   「歡迎回來，[剛剛輸入的名字]！這是您的會員儀表板，建置中。」
   並放上 3 張「即將推出」的功能卡片（依照我的產品功能設計）。
   顯示名字時請用 textContent，不要用 innerHTML。
5. 使用者重新整理網頁時，如果 localStorage 裡已經有名字，就直接顯示會員儀表板。
6. 儀表板上加一個「登出」按鈕，按下後清除 localStorage 並回到表單。
7. 如果送出失敗，要顯示清楚的錯誤訊息，並保留使用者已填寫的內容。

其他部分保持不變，並在 JavaScript 加上中文註解。
改完後請不要幫我執行 git 指令。
```

**各項技術要求的理由：**

| 要求 | 理由 |
| --- | --- |
| 攔截預設送出（`event.preventDefault()`） | 瀏覽器預設會以整頁導向的方式送出表單並載入新頁面；攔截後才能留在原頁、原地更新畫面 |
| 使用 `fetch()` 以 POST 送到 `/` | `fetch()` 在背景發出 HTTP 請求，這種不重新載入頁面的通訊方式通稱 AJAX。Netlify 會攔截送到網站路徑的表單 POST，送到 `/` 即可 |
| `application/x-www-form-urlencoded` | 這是 HTML 表單的標準編碼格式（`name=%E5%B0%8F%E6%98%8E&email=...`），也是 Netlify Forms 接受的格式；若改送 JSON，Netlify 無法解析 |
| `URLSearchParams(new FormData(form))` | `FormData` 讀取表單中所有具 `name` 的欄位（包含隱藏的 `form-name`），`URLSearchParams` 將其轉為 urlencoded 字串 |
| 成功後才寫入 localStorage | 避免送出失敗時，畫面卻顯示「已加入」，造成使用者與後台資料不一致 |
| 不在 localStorage 存 Email | LocalStorage 未加密，可被頁面上任何腳本讀取；依資料最小化原則，只存顯示所需的名字 |
| 使用 `textContent` | 若以 `innerHTML` 插入使用者輸入，輸入內容若含 HTML 或腳本會被瀏覽器執行，形成跨站腳本攻擊（Cross-Site Scripting, XSS）的風險 |
| 錯誤處理 | 網路中斷或伺服器錯誤時仍需給使用者明確回饋 |

原理說明：[LocalStorage 講義](../../docs/tutorials/localstorage.md)｜官方說明：[Netlify Forms setup](https://docs.netlify.com/manage/forms/setup/)（其中說明以 AJAX 送出表單的方式）

### 3.3 提示詞 3：快速改版以觀察持續部署

選擇一項**在手機上一眼可辨識**的修改，以便驗證是否自動更新：

```text
請把 #index.html 主視覺的 CTA 按鈕顏色改成【亮橘色】，文字改成【立即免費加入】。
其他部分保持不變。
```

```text
請在 #index.html 最上方加一條公告橫幅：「早鳥名單開放中：上線時優先通知」。
其他部分保持不變。
```

完成後 Keep → Commit → Sync，並依 [CI/CD 講義](../../docs/tutorials/cicd.md) 觀察自動部署。修改要「小而明顯」，是持續部署的基本精神：每次變更越小，出錯時越容易定位與回復。

### 3.4 提示詞 4（選做）：提升 MVP 的說服力

```text
請在 #index.html 加入一個「社會認同（Social Proof）」區塊：
- 顯示一個數字計數器動畫，數字從 0 增加到【目前實際報名人數】
- 下方放 3 則使用者回饋卡片，以姓名縮寫作為頭像
- 若內容為示意用途，請在區塊下方以小字標示「示意內容」
其他部分保持不變。
```

```text
請檢查 #index.html 在手機版（寬度 375px）的使用體驗，列出 5 項可改善之處，說明理由後直接修改。
```

**誠信原則**：社會認同會影響使用者判斷。課堂展示時使用示意內容須明確標示；對外公開時應使用真實數據與經同意的真實回饋，捏造人數或推薦語屬於誤導行為，也會污染你自己的驗證數據。

### 3.5 疑難排解提示詞

```text
（Ask 模式）我的 Netlify 後台 Forms 頁面看不到任何表單。
請檢查 #index.html 的表單是否符合 Netlify Forms 的規定：
<form> 的 name、method="POST"、data-netlify="true"、隱藏的 form-name 欄位、
每個欄位的 name 屬性，以及表單是否直接寫在 HTML 中。只列出問題，先不要修改。
```

```text
我按下送出後，畫面沒有變成會員儀表板。瀏覽器 Console 顯示下列錯誤：【貼上錯誤訊息】
請說明錯誤原因，並直接修正 #index.html。
```

開啟 Console 的方式：在網頁上按 `F12`（Mac：`⌘⌥I`）→ 選擇「Console」分頁，紅色文字為錯誤訊息。參考：[Chrome DevTools 概覽](https://developer.chrome.com/docs/devtools/overview)。其他常見狀況見 [疑難排解手冊](../../docs/tutorials/error_guide.md)。

---

## 4. Copilot 產出後的驗證清單

AI 產生的程式碼可能在語法上正確，卻不符合平台規則或存在安全問題。每次按 Keep 前後，請逐項確認：

**表單結構（提示詞 1 之後）**

- [ ] `<form>` 同時具有 `name="waitlist"`、`method="POST"`、`data-netlify="true"`。
- [ ] 表單內有 `<input type="hidden" name="form-name" value="waitlist">`，且 `value` 與 `<form>` 的 `name` 完全相同。
- [ ] 每個輸入欄位（含下拉選單、多行文字）都有 `name` 屬性。
- [ ] 有 `netlify-honeypot="bot-field"`，且對應的 `bot-field` 欄位在畫面上看不到。
- [ ] `<form>` 是直接寫在 HTML 中，而非由 JavaScript 產生（搜尋 `createElement('form')` 或 `innerHTML` 中含 `<form`）。
- [ ] 表單附近有個資蒐集目的的說明。
- [ ] 其他區塊沒有被意外刪改（在原始檔控制面板檢視差異）。

**AJAX 與 LocalStorage（提示詞 2 之後）**

- [ ] 有 `event.preventDefault()`。
- [ ] `fetch` 的 `method` 為 `POST`，`Content-Type` 為 `application/x-www-form-urlencoded`，本文由 `URLSearchParams` 產生，而非 `JSON.stringify`。
- [ ] 只有在 `response.ok` 為真時才寫入 localStorage 並切換畫面。
- [ ] localStorage 中只存名字，沒有 Email 或其他個資（在開發者工具 Application → Local storage 檢查）。
- [ ] 顯示名字使用 `textContent`，而非 `innerHTML`。
- [ ] 重新整理後儀表板仍在；按「登出」後回到表單，且 localStorage 對應項目已刪除。

**部署後（在 Netlify 網址上測試）**

- [ ] 使用 `https://…netlify.app` 網址測試，而非本機 `file:///` 開啟的檔案。
- [ ] Netlify **Forms** 頁面出現 `waitlist`，送出的測試資料可在其中看到。
- [ ] [網站自我檢核工具](../../tools/vibe_check.html) 對應等級通過（提示詞 1 後為 Level 2，提示詞 2 後為 Level 3）。
- [ ] 在原始檔控制面板確認 Copilot 沒有自行執行 git 指令（沒有你未撰寫的 Commit）。
