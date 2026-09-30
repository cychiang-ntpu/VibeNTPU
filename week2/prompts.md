# 🪄 第二週 AI 咒語集：串接 BaaS 與模擬會員體驗

> 使用方式：**先把你上週的 `index.html` 完整內容貼給 AI**（或上傳檔案），再貼上下面的咒語。
> 這樣 AI 才會在「你的網頁」上修改，而不是重新做一個新的。

[← 回第二週](README.md)

---

## 咒語 1：加入早鳥候補名單（Waitlist）表單

```text
你是一位資深前端工程師。以下是我目前的 index.html 程式碼：

【把你的 index.html 完整內容貼在這裡】

請幫我在網頁上新增一個「加入早鳥候補名單（Waitlist）」的區塊，要求如下：

【表單欄位】
1. 姓名（必填）
2. Email（必填，要檢查格式）
3. 身分（下拉選單：大學生 / 研究生 / 上班族 / 其他）
4. 你最期待的功能（選填，多行文字）

【Netlify Forms 串接（非常重要，請務必遵守）】
1. <form> 標籤必須加上 name="waitlist"、method="POST" 以及 data-netlify="true" 屬性。
2. 在表單內加入 <input type="hidden" name="form-name" value="waitlist" />。
3. 每個輸入欄位都要有 name 屬性。
4. 加入防機器人的 honeypot 欄位：在 <form> 加上 netlify-honeypot="bot-field"，
   並在表單內加入一個隱藏的 <input name="bot-field" />。

【其他要求】
- 導覽列和主視覺的 CTA 按鈕，點擊後要平滑捲動到這個表單。
- 風格要和原本的網頁一致，並支援手機版。
- 其他部分保持不變，請給我完整的 index.html 程式碼。
```

> 🏗️ **架構呼應**：`data-netlify="true"` 這一行字，就是把「訂單代收中心（BaaS）」接上你餐廳的關鍵！
> 📖 官方說明：[Netlify Forms：HTML 表單設定](https://docs.netlify.com/forms/setup/)

✅ **檢查 AI 有沒有做對**：用 `Ctrl + F`（Mac 用 `⌘ + F`）在程式碼裡搜尋 `data-netlify`，找得到就對了。

---

## 咒語 2：送出後原地變成「會員儀表板」

```text
很好！現在請幫我修改這個 index.html，打造「模擬登入」的體驗：

1. 使用者按下送出後，網頁「不要跳轉到其他頁面」。
2. 請用 JavaScript 的 fetch()，以 AJAX 方式把表單資料送給 Netlify：
   - 送到 "/"，方法是 POST
   - Content-Type 為 "application/x-www-form-urlencoded"
   - 內容用 new URLSearchParams(new FormData(form)).toString() 產生
3. 送出後，把使用者輸入的「姓名」存進瀏覽器的 localStorage。
4. 表單區塊原地變成一個「會員儀表板」畫面，顯示：
   「🎉 歡迎回來，[剛剛輸入的名字]！這是您的會員儀表板，建置中…」
   並放上 3 張「即將推出」的功能卡片（依照我的產品功能設計）。
5. 使用者重新整理網頁時，如果 localStorage 裡已經有名字，就直接顯示會員儀表板。
6. 儀表板上加一個「登出」按鈕，按下後清除 localStorage 並回到表單。
7. 如果送出失敗，要顯示友善的錯誤訊息。

其他部分保持不變，請給我完整的 index.html 程式碼，並在 JavaScript 加上中文註解。
```

> 🏗️ **架構呼應**：現在你的網站同時用了兩種「記住客人」的方式：
> - ☁️ **Netlify Forms**（雲端）：老闆在後台看得到名單。
> - 💻 **LocalStorage**（瀏覽器）：客人自己的瀏覽器記得「我已經加入了」。
>
> 📖 原理解說：[localstorage.md](localstorage.md)｜官方說明：[Netlify：用 AJAX 送出表單](https://docs.netlify.com/forms/setup/#submit-javascript-rendered-forms-with-ajax)

---

## 咒語 3：快速改版，體驗 CI/CD

選一個你想改的地方，越明顯越好（這樣用手機驗收時才看得出來）：

```text
請把主視覺的 CTA 按鈕顏色改成【亮橘色】，文字改成【立即免費加入 🚀】。
其他部分保持不變，請給我完整的程式碼。
```

```text
請在網頁最上方加一條公告橫幅：「🎉 早鳥限定：前 100 名加入享終身 8 折！」
其他部分保持不變，請給我完整的程式碼。
```

然後照 👉 [cicd.md](cicd.md) 的步驟上傳，見證自動更新的魔法！

---

## 咒語 4（加分題）：讓 MVP 更有說服力

```text
請在網頁上加入一個「社會認同（Social Proof）」區塊：
- 顯示「已有 128 位北大同學加入候補名單」的計數器動畫（數字從 0 跳到 128）
- 下方放 3 則虛構的使用者推薦語，搭配 Emoji 頭像
其他部分保持不變，請給我完整的程式碼。
```

```text
請幫我檢查這個網頁的「手機版」體驗，列出 5 個可以改善的地方，並直接修改好給我完整的程式碼。
```

> ⚠️ **誠信提醒**：Demo 時用虛構數字沒關係，但**正式對外上線時，請使用真實數據**，不要誤導使用者。

---

## 🚑 卡關急救包

```text
我的 Netlify 後台 Forms 頁面看不到任何表單。
以下是我的表單程式碼：【貼上 <form> ... </form> 的部分】
請幫我檢查是否符合 Netlify Forms 的規定（name 屬性、data-netlify、hidden form-name 欄位）。
```

```text
我按下送出後，畫面沒有變成會員儀表板。瀏覽器的 Console 顯示這個錯誤：【貼上錯誤訊息】
請幫我找出問題並給我修正後的完整程式碼。
```

> 💡 **怎麼看 Console 錯誤訊息？** 在網頁上按 `F12`（Mac：`⌘ + ⌥ + I`）→ 點「Console」分頁，紅色的字就是錯誤訊息。
> 📖 [Chrome 開發者工具入門](https://developer.chrome.com/docs/devtools/overview)
