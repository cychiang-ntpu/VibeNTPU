# 第 3 週提示詞：Supabase

每一段都是用中文告訴 Copilot 你要什麼。只有「照抄」的部分含技術字眼，照貼就好。
使用方式：VS Code 打開 `pickle-charm-shop` → Copilot 聊天面板 → **Agent** → 貼上 → Enter → 看變更 → **保留（Keep）**。要求執行指令時按 **Skip**。一次貼一段，做完檢查再貼下一段。

[回實作指南](README.md)

---

## 第一次對話前：約定（只貼一次）

```text
接下來我會請你把這個皮克敏吊飾商店接上 Supabase。請遵守：
- 直接修改工作區裡的 index.html、script.js、styles.css，不要只在對話裡貼程式碼。
- 保持現在的設計風格，手機上也要好看。
- 不要使用 emoji。
- 不要幫我執行任何指令，也不要執行 git。
- 每次只做我這一段要求的事，其他地方不要動。
- 所有和 Supabase 溝通的程式都放在 script.js，用瀏覽器可以直接載入的方式，不要用 npm、打包工具或框架。
```

---

## 提示詞 1：接上 Supabase（照抄，換掉兩個【】）

```text
請把網站接上 Supabase，完全照下面做：
1. 在 index.html 的 <head> 加一行，從 CDN 載入 supabase-js：
   <script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
   這一行要放在載入 script.js 之前。
2. 在 script.js 最上面建立連線：
   const SUPABASE_URL = "【Project URL】";
   const SUPABASE_ANON_KEY = "【anon key】";
   const db = supabase.createClient(SUPABASE_URL, SUPABASE_ANON_KEY);
3. 先不要改其他功能。
```

---

## 提示詞 2：真正的註冊與登入

```text
把「加入會員」小視窗改成真正的帳號系統，用 Supabase Auth 的 Email 加密碼：
1. 小視窗裡有兩個模式可以切換：「註冊」和「登入」。
   - 註冊：姓名、Email、密碼（至少 6 個字）、送出。
   - 登入：Email、密碼、送出。
2. 註冊用 db.auth.signUp，並把姓名放在 options.data.name 裡（資料庫會自動存成會員資料）。
3. 登入用 db.auth.signInWithPassword。
4. 註冊或登入成功後：關掉小視窗，右上角顯示「歡迎回來，〔姓名〕」加「登出」按鈕。姓名從 Supabase 的 profiles 資料表讀（欄位 name，用 id 等於目前使用者的 id 查）；讀不到就顯示 Email。
5. 「登出」用 db.auth.signOut，畫面回到「登入」按鈕。
6. 網頁打開時用 db.auth.getSession 檢查是否已登入；並用 db.auth.onAuthStateChange 在登入狀態改變時更新畫面。
7. 不要再用 localStorage 記會員資料；把上週的 localStorage "pickleUser" 相關程式移除。
8. 失敗時把 Supabase 回傳的錯誤訊息顯示在小視窗裡（例如密碼太短、帳號已存在、密碼錯誤），不要用 alert()。
9. 上週表單上的 Netlify 設定（data-netlify、form-name、bot-field）可以移除，這個表單不再送到 Netlify。
顯示姓名時用 textContent。
```

---

## 提示詞 3：購物車存進 Supabase

```text
把購物車從 localStorage 改成存在 Supabase 的 cart_items 資料表（欄位：user_id、product_name、unit_price、qty；同一個使用者加同一個商品是同一列）：
1. 沒有登入時按「加入購物車」，自動打開登入小視窗，並顯示「請先登入再加入購物車」。
2. 登入後按「加入購物車」：用 upsert 寫入 cart_items（onConflict 用 "user_id,product_name"），同一商品 qty 加一。user_id 填目前登入者的 id。
3. 購物車面板的內容從 cart_items 讀取（只會讀到自己的，資料庫規則已設定）；「＋」「－」更新 qty，減到 0 就刪除那一列。
4. 右上角數字 = 自己購物車裡 qty 的總和。登出後數字變 0、面板清空。
5. 登入或網頁打開時重新載入購物車。
6. 移除上週 localStorage "pickleCart" 的程式。
7. 讀寫失敗時在面板裡顯示「連線失敗，請稍後再試」。
```

---

## 提示詞 4：訂單存進 Supabase，加「我的訂單」

```text
把「送出訂單」改成存進 Supabase 的 orders 資料表，並加一個「我的訂單」區塊：
1. 送出訂單時，用 db.from("orders").insert 寫入一列：
   user_id（目前登入者 id）、email（登入者 Email）、name、phone、address、note（表單欄位）、
   items（一個陣列，每個元素是 { name, price, qty }，從購物車來）、total（總金額）。
   status 不用填，資料庫會預設為 pending。
   用 .select().single() 拿回新增的那一列，取得訂單編號 id。
2. 成功後：清空購物車（如果購物車還是上週的 localStorage 版本就清 localStorage；如果已改成 Supabase 的 cart_items 就刪除自己的所有列）、面板換成「訂單已送出，訂單編號 #〔id〕」和商品摘要、右上角數字變 0。
3. 失敗時在面板裡顯示錯誤訊息，不要用 alert()。
4. 上週訂單表單上的 Netlify 設定（data-netlify、form-name、bot-field）移除；不再送到 Netlify。
5. 在評價區下面新增「我的訂單」區塊（有 id="my-orders"）：登入後從 orders 讀自己的訂單（按 created_at 由新到舊），每筆顯示訂單編號、日期、商品摘要、總金額、狀態（pending 顯示「處理中」、shipped 顯示「已出貨」、其他原樣顯示）。沒登入時顯示「登入後可查看訂單」。下單成功後重新載入這個區塊。
```

---

## 出問題時

| 狀況 | 貼給 Copilot 的話 |
| --- | --- |
| 顯示 `Invalid API key` 或 `Failed to fetch` | 不用問 Copilot：回 Supabase 重新複製 Project URL 與 anon key，再貼一次提示詞 1 |
| `Email not confirmed` | 不用問 Copilot：Supabase → Authentication → Sign In / Providers → Email → 關閉 Confirm email |
| 畫面還在用 localStorage，`cart_items` 沒資料 | `購物車還是存在 localStorage。請把購物車的讀寫全部改成 Supabase 的 cart_items 資料表，移除 localStorage "pickleCart"，其他不動。` |
| `new row violates row-level security policy` | `寫入 Supabase 時沒有帶 user_id。請在 insert 和 upsert 時把 user_id 設成目前登入者的 id（db.auth.getUser 或 getSession 取得），其他不動。` |
| Console 有紅字 | `我看到這個錯誤：〔紅字〕，請修好，其他不動。` |
| Copilot 改到不該改的 | 按 **Undo**，再貼：`只做我剛才那一段要求的事，其他地方不要動。` |
| 老師的完成版可以對照 | [samples/pickle-charm-shop-supabase](../../samples/pickle-charm-shop-supabase/) |

---

## 延伸提示詞（選做）

**忘記密碼**

```text
在登入模式下方加一個「忘記密碼」連結：按下後請使用者輸入 Email，用 db.auth.resetPasswordForEmail 寄重設信（redirectTo 設成目前網站的網址）。寄出後顯示「重設信已寄出，請到信箱查看」。
```

**訂單狀態變更時通知我（老闆）**

課堂外做法：Supabase → Database → Webhooks，或用 Supabase 的 Email 服務。本課程不要求。

---

## 提示詞裡的技術字眼是什麼？（看不看都可以）

| 字眼 | 一句話 |
| --- | --- |
| `supabase-js` 的 CDN 那一行 | 讓網頁可以跟 Supabase 說話的工具，用一行載入 |
| `createClient(URL, anon key)` | 告訴工具「我的 Supabase 在哪、我是誰」 |
| `signUp`、`signInWithPassword`、`signOut` | Supabase 內建的註冊、登入、登出 |
| `getSession`、`onAuthStateChange` | 打開網頁時問「有人登入嗎」；登入狀態變了就通知網頁 |
| `from("cart_items").upsert(...)` | 「有就更新，沒有就新增」一列資料 |
| `onConflict: "user_id,product_name"` | 判斷「同一個人、同一個商品」算同一列 |
| `insert ... .select().single()` | 新增一列，並把新增的那一列拿回來（含訂單編號） |
| RLS、`user_id` | 資料庫規則只允許你碰自己的列，所以每一列都要寫上是誰的 |
