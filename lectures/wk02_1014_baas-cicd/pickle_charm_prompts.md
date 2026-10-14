# Pickle Charm Shop 提示詞

使用方式：VS Code 打開你的 `pickle-charm-shop` 資料夾 → Copilot 聊天面板 → 模式選 **Agent** → 複製整段提示詞貼上 → Enter → 檢視變更後按 **保留（Keep）**。Copilot 要求執行指令時按 **Skip**。

[回實作指南](pickle_charm_lab.md)

---

## 提示詞 1：註冊與登入

```text
請直接修改這個工作區的 #index.html、#script.js 和 #styles.css，為這個皮克敏吊飾商店加上「註冊／登入」功能。要求如下：

【畫面】
1. 右上角現有的「登入」按鈕（class="ghost-btn"）改為：按下後在頁面中央彈出一個「加入會員」對話框，可以關閉。
2. 對話框內是一個表單，欄位：姓名（必填）、Email（必填，type="email"）、一個「送出」按鈕。
3. 表單上方加一行說明：「我們只會用這些資料通知你新品與訂單狀態。」

【Netlify Forms 串接（請完全照做）】
4. <form> 必須是 name="signup" method="POST" data-netlify="true" netlify-honeypot="bot-field"。
5. 表單內加 <input type="hidden" name="form-name" value="signup">。
6. 加一個隱藏的 honeypot 欄位：<p hidden><input name="bot-field"></p>。
7. 每個輸入欄位都要有 name 屬性（name="name"、name="email"）。
8. <form> 必須直接寫在 HTML 裡，不要用 JavaScript 動態產生。

【送出行為（JavaScript，寫在 script.js）】
9. 送出時用 event.preventDefault() 阻止跳頁，改用 fetch() 以 POST 送到 "/"，
   headers 為 { "Content-Type": "application/x-www-form-urlencoded" }，
   body 為 new URLSearchParams(new FormData(form)).toString()。
10. 只有在 response.ok 為 true 時，才把 { name, email } 以 JSON 存進 localStorage，鍵名 "pickleUser"。
11. 存好後關閉對話框，右上角「登入」按鈕改成顯示「歡迎回來，〔姓名〕」，旁邊多一個「登出」按鈕。顯示姓名時用 textContent，不要用 innerHTML。
12. 頁面載入時，如果 localStorage 有 "pickleUser"，直接顯示歡迎狀態。
13. 「登出」會移除 localStorage 的 "pickleUser"，畫面回到原本的「登入」按鈕。
14. 送出失敗時，在對話框內顯示「送出失敗，請確認網路後再試一次」，不要用 alert()。

【其他】
15. 樣式延續現有的 styles.css 風格，手機上也要能正常使用。
16. 不要使用 emoji；需要圖示時用內嵌 SVG。
17. 其他現有內容與功能保持不變。
18. 不要幫我執行任何 git 指令，我會自己用 VS Code 的原始檔控制提交。
```

---

## 提示詞 2：購物車與下訂單

```text
請直接修改這個工作區的 #index.html、#script.js 和 #styles.css，把「加入購物車」做成真正可以下訂單的購物車。要求如下：

【商品資料】
1. 三個商品卡片（粉糖皮克敏 NT$390、夜空藍皮克敏 NT$420、陽光草莓皮克敏 NT$450）的「加入購物車」按鈕，各自加上 data-name 與 data-price 屬性。

【購物車】
2. 按「加入購物車」時，把商品加入購物車；同一商品再按一次是數量 +1。按鈕不要變成禁用，保持可重複點擊。
3. 右上角的購物車數字顯示所有商品數量的總和。
4. 按右上角「購物車」按鈕時，在頁面右側滑出購物車面板，可以關閉。
5. 面板中列出每一項商品：名稱、單價、數量（有 + 和 − 按鈕）、小計；最下方顯示總金額。數量減到 0 就從購物車移除。
6. 購物車內容存在 localStorage，鍵名 "pickleCart"；重新整理後購物車還在。

【結帳表單（在購物車面板下方）】
7. 欄位：收件人姓名（必填，name="name"）、電話（必填，name="phone"）、地址（必填，name="address"）、備註（選填，name="note"）。
8. 另外放三個隱藏欄位：name="items"（送出前由 JavaScript 填入商品清單文字，例如「粉糖皮克敏 x2, 夜空藍皮克敏 x1」）、name="total"（總金額數字）、name="email"（如果 localStorage 有 "pickleUser" 就填入其 email，否則留空）。
9. <form> 必須是 name="order" method="POST" data-netlify="true" netlify-honeypot="bot-field"，表單內有 <input type="hidden" name="form-name" value="order"> 和隱藏的 <p hidden><input name="bot-field"></p>。
10. <form> 直接寫在 HTML 裡，不要用 JavaScript 動態產生。

【送出行為】
11. 購物車是空的時候，「送出訂單」按鈕不可按，並顯示「購物車是空的」。
12. 送出時 event.preventDefault()，先把 items 與 total 隱藏欄位填好，再用 fetch() POST 到 "/"，Content-Type 為 application/x-www-form-urlencoded，body 為 new URLSearchParams(new FormData(form)).toString()。
13. response.ok 時：清空購物車（localStorage 與畫面）、把面板內容換成「訂單已送出」加上訂單摘要（商品、數量、總金額）。
14. 失敗時在面板內顯示「送出失敗，請確認網路後再試一次」，不要用 alert()。
15. 如果已登入（localStorage 有 "pickleUser"），收件人姓名欄位預設帶入其姓名。

【其他】
16. 樣式延續 styles.css 風格，手機上面板要全寬顯示。
17. 不要使用 emoji；需要圖示時用內嵌 SVG。
18. 保留提示詞 1 已完成的註冊／登入功能，其他現有內容不變。
19. 不要幫我執行任何 git 指令。
```

---

## 修正提示詞（出問題時用）

**A. Copilot 沒有加 Netlify 屬性**

```text
請檢查 #index.html 中 name="signup" 和 name="order" 的 <form>，確認每個都有 method="POST"、data-netlify="true"、netlify-honeypot="bot-field"，表單內有 <input type="hidden" name="form-name"> 且 value 與 form 的 name 相同，並且每個輸入欄位都有 name 屬性。缺少的請補上，其他不變。
```

**B. 送出後跳到 Netlify 的 Thank you 頁面**

```text
#script.js 中送出 signup 或 order 表單時沒有阻止頁面跳轉。請在 submit 事件處理函式一開始加上 event.preventDefault()，並確認是用 fetch() 送出，其他不變。
```

**C. 瀏覽器 Console 出現錯誤**

```text
我在瀏覽器 Console 看到這個錯誤：【貼上紅字】。請找出原因並直接修正相關檔案，其他不變。
```

**D. 總金額或數量算錯**

```text
購物車的【數量／總金額】顯示不正確：我加入了【描述你做的動作】，畫面顯示【實際結果】，應該是【預期結果】。請修正 #script.js，其他不變。
```

---

## 步驟 18 用：改一處文字

```text
請把 #index.html 中「立即選購」按鈕的文字改成「馬上下單」，其他不變。
```

---

## 延伸提示詞（選做）

**我的訂單**

```text
請在 #index.html 加一個「我的訂單」區塊（放在評價區之後），並修改 #script.js：每次訂單送出成功後，把 { 時間, 商品清單, 總金額 } 加進 localStorage 的 "pickleOrders" 陣列；頁面載入時列出所有歷史訂單；提供「清除紀錄」按鈕。只存這三個欄位，不要存電話與地址。不要使用 emoji。其他不變。
```

---

## 為什麼提示詞裡要寫這些

| 寫法 | 原因 |
| --- | --- |
| `data-netlify="true"`、`name="signup"` | Netlify 在部署時掃描 HTML 找到這些表單，才會建立收件箱 |
| 隱藏欄位 `form-name` | 用 JavaScript 送出時，Netlify 靠它分辨是哪一個表單 |
| 每個欄位都有 `name` | 沒有 `name` 的欄位，Netlify 不會記錄 |
| honeypot 欄位 | 機器人會亂填隱藏欄位，Netlify 據此過濾垃圾資料 |
| 表單直接寫在 HTML | Netlify 只讀靜態 HTML，JavaScript 動態產生的表單它看不到 |
| `preventDefault()` ＋ `fetch()` | 不跳頁，可以在原畫面顯示結果 |
| 只在 `response.ok` 才寫 localStorage | 送出失敗時不要假裝成功 |
| 用 `textContent` 顯示姓名 | 避免輸入的文字被當成 HTML 執行 |
| 不執行 git 指令 | 提交與同步由你自己在 VS Code 操作，這是要練習的技能 |

送出後的檢查清單：
1. `Ctrl+F` 找得到 `data-netlify`（兩處）。
2. 本機預覽能打開對話框與購物車面板，數字會變。
3. 部署後用 netlify.app 網址測試，不是本機檔案。
4. Netlify → Forms 看得到 `signup` 與 `order`。
5. 手機上重新整理後，登入狀態與購物車都還在。
