# 第 2 週提示詞

[回第 2 週手把手實作](README.md)

提示詞＝你寫給 Copilot 的文字指令。本頁的提示詞可以直接複製使用；方括號【】裡的文字可以換成你自己的產品內容。

---

## 怎麼使用（每一個提示詞都一樣）

1. 在 VS Code 打開上週的 repo 資料夾（左側檔案總管要看得到 `index.html`）。
2. 打開 **Copilot Chat** 面板，在輸入框下方的模式選單選擇 **Agent**。
3. 複製下方灰色框裡的全部文字，貼到輸入框，按 `Enter` 送出。
4. 等 Copilot 改完，看一下 `index.html` 中綠色（新增）和紅色（刪除）的地方。
5. 沒問題就按 **保留（Keep）**；不滿意就按 **復原（Undo）**，改一下提示詞再送一次。
6. 按 `Ctrl+S`（Mac：`⌘S`）存檔，再到左側 **原始檔控制（Source Control）** 按 **提交（Commit）** 和 **同步變更（Sync Changes）**。

提示詞裡的 `#index.html` 是告訴 Copilot「請修改這個檔案」。想依自己的產品自動填好內容，可以用 [提示詞產生器](../wk01_1007_saas-storefront/slides/prompt_builder.html)，按上方的 **第 2 週：加入早鳥名單表單**。

---

## 提示詞 1：加入早鳥候補名單表單（Part 2）

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
- 不要使用 emoji；需要圖示時請用 inline SVG。
- 其他部分保持不變。
- 改完後請不要幫我執行 git 指令，我會自己用 VS Code 的原始檔控制存檔。
```

## 提示詞 2：送出後變成會員歡迎畫面（Part 3）

在提示詞 1 的同一個對話中接著送出即可。

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
8. 功能卡片不要使用 emoji；需要圖示時請用 inline SVG。

其他部分保持不變，並在 JavaScript 加上中文註解。
改完後請不要幫我執行 git 指令。
```

## 提示詞 3：做一個一眼看得出來的修改（Part 4）

兩個選一個就好。修改要小、但在手機上一眼看得出來，才方便確認網站有沒有自動更新。

```text
請把 #index.html 主視覺的 CTA 按鈕顏色改成【亮橘色】，文字改成【立即免費加入】。
其他部分保持不變。
```

```text
請在 #index.html 最上方加一條公告橫幅：「早鳥名單開放中：上線時優先通知」。
不要使用 emoji。其他部分保持不變。
```

## 提示詞 4（選做）：讓頁面更有說服力

```text
請在 #index.html 加入一個「社會認同（Social Proof）」區塊：
- 顯示一個數字計數器動畫，數字從 0 增加到【目前實際報名人數】
- 下方放 3 則使用者回饋卡片，以姓名縮寫作為頭像
- 若內容為示意用途，請在區塊下方以小字標示「示意內容」
- 不要使用 emoji；需要圖示時請用 inline SVG
其他部分保持不變。
```

```text
請檢查 #index.html 在手機版（寬度 375px）的使用體驗，列出 5 項可改善之處，說明理由後直接修改。
```

請誠實：示意用的人數或回饋一定要標示「示意內容」；對外公開時只能放真實數字。

## 遇到問題時可用的提示詞

後台看不到表單時（模式選 **Ask**，只檢查不修改）：

```text
我的 Netlify 後台 Forms 頁面看不到任何表單。
請檢查 #index.html 的表單是否符合 Netlify Forms 的規定：
<form> 的 name、method="POST"、data-netlify="true"、隱藏的 form-name 欄位、
每個欄位的 name 屬性，以及表單是否直接寫在 HTML 中。只列出問題，先不要修改。
```

送出後沒有出現歡迎畫面時（模式選 **Agent**）：

```text
我按下送出後，畫面沒有變成會員儀表板。瀏覽器 Console 顯示下列錯誤：【貼上錯誤訊息】
請說明錯誤原因，並直接修正 #index.html。
```

錯誤訊息在哪裡看：在網頁上按 `F12`（Mac：`⌘⌥I`），點選 **Console** 分頁，紅色的文字就是錯誤訊息。其他狀況見 [疑難排解手冊](../../docs/tutorials/error_guide.md)。

---

## 為什麼提示詞裡要寫這些

提示詞裡的技術要求看起來很瑣碎，但少寫一條，常常就會「畫面看起來正常、後台卻收不到資料」。

| 提示詞裡寫的 | 白話說明 |
| --- | --- |
| `data-netlify="true"`、`name="waitlist"` | 告訴 Netlify「這張表單要收」，並替它取名字，後台才找得到 |
| `method="POST"`、每個欄位都有 `name` | 資料才會真的被送出；沒有名字的欄位不會出現在後台 |
| 隱藏的 `form-name` 欄位 | 用程式在背景送出時，Netlify 靠它判斷資料屬於哪張表單 |
| 表單直接寫在 HTML 裡 | Netlify 只讀 HTML 檔案找表單，用程式產生的表單它看不到 |
| 只存名字、用 `textContent` | 瀏覽器裡的資料誰都看得到，所以不存 Email；`textContent` 可避免有人輸入惡意程式碼 |
| 不要執行 git 指令 | 讓你自己檢查修改、自己提交，確實知道存了什麼 |

想看每一條的完整原理：[表單、儲存與 CI/CD 深入閱讀](../../docs/deep_dive/forms_storage_cicd.md)（選讀）。

## 按下保留之後，檢查這 5 件事

- [ ] 在 `index.html` 按 `Ctrl+F`（Mac：`⌘F`）搜尋得到 `data-netlify` 和 `form-name`。
- [ ] 表單附近有一句話說明資料用途。
- [ ] 其他區塊沒有被意外刪掉（看原始檔控制面板中紅色的部分）。
- [ ] 用 `https://…netlify.app` 網址測試（不是 `file:///`），送出後 Netlify 的 **Forms → waitlist** 看得到資料。
- [ ] （提示詞 2 之後）重新整理後歡迎畫面還在，按 **登出** 會回到表單。
