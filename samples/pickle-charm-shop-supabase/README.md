# Pickle Charm Shop 參考實作（Supabase 版）

這個資料夾是第 3 週實作指南四段提示詞的「參考結果」：把第 2 週的 `pickle-charm-shop` 從 Netlify Forms 與 localStorage 改成接 Supabase。

- 提示詞 1：在 `index.html` 以 CDN 載入 supabase-js，在 `script.js` 最上面用 `createClient` 建立連線。
- 提示詞 2：「註冊／登入」小視窗改用 Supabase Auth（Email 加密碼），姓名存進 `profiles`，右上角顯示「歡迎回來，〔姓名〕」與「登出」。
- 提示詞 3：購物車存在 `cart_items` 資料表，沒登入就按「加入購物車」會先打開登入小視窗。
- 提示詞 4：訂單存進 `orders` 資料表，面板顯示「訂單已送出，訂單編號 #〔id〕」，評價區下面有「我的訂單」區塊（`id="my-orders"`）。

提示詞全文見 `lectures/wk03_supabase/prompts.md`。老師可以用這份程式碼示範預期的畫面與行為；同學的版本不必和它一模一樣，但應符合提示詞中的每一項要求。

## 使用前一定要做的事

1. **建立資料表**：到 Supabase 左側 SQL Editor，貼上並執行 `lectures/wk03_supabase/supabase_setup.sql`。沒有先執行，註冊之後讀不到姓名，購物車和訂單也會寫入失敗。
2. **關閉 Email 確認**（課堂用）：Supabase → Authentication → Sign In / Providers → Email → 關閉 **Confirm email**。沒關的話，註冊後要先去信箱點確認連結才能登入，畫面會顯示「註冊成功，請到信箱確認 Email 後再登入」。
3. **換掉兩個常數**：打開 `script.js`，把最上面的
   ```js
   const SUPABASE_URL = "https://YOUR-PROJECT.supabase.co";
   const SUPABASE_ANON_KEY = "YOUR-ANON-KEY";
   ```
   換成自己專案的 Project URL 與 anon key（Supabase → Project Settings → API）。沒換就會看到 `Invalid API key` 或 `Failed to fetch`。

## 檔案

- `index.html`：頁面內容。`<head>` 多了一行 supabase-js 的 CDN；小視窗改成「登入／註冊」兩個模式；評價區下面多了「我的訂單」區塊。上週表單上的 Netlify 設定（`data-netlify`、`form-name`、`bot-field`）已全部移除。
- `script.js`：連線 Supabase、註冊／登入／登出、購物車（`cart_items`）、下單（`orders`）、我的訂單。已不再使用 localStorage 的 `pickleUser` 與 `pickleCart`。
- `styles.css`：原本的樣式，加上模式切換按鈕與訂單卡片的樣式。

## 如何部署

1. 把這三個檔案放進自己的 GitHub 儲存庫（或 fork 課程儲存庫後只取這個資料夾）。
2. 到 Netlify 新增站台，選擇該儲存庫；不需要 build 指令，publish directory 設為放這三個檔案的資料夾。
3. 這一版不再用 Netlify Forms，所以不需要開啟 form detection。
4. 本機直接開 `index.html` 也能運作（資料都是直接送到 Supabase），但建議還是用 `*.netlify.app` 網址測試。

## 安全注意事項

- **anon key 可以放在網頁裡**：它本來就是給瀏覽器用的公開金鑰，能做什麼完全由資料庫的 RLS 規則決定。
- **service_role key 絕對不能放進網頁或 GitHub**：它會略過所有 RLS 規則，拿到的人可以讀改刪整個資料庫。
- **RLS 是真正的防線**：`supabase_setup.sql` 裡的規則限制每個人只能讀寫自己的 `profiles`、`cart_items`、`orders`。程式裡每次 insert、upsert 都要帶上 `user_id`（目前登入者的 id），否則會被規則擋下，出現 `new row violates row-level security policy`。
- 會員不能改訂單狀態（沒有 update 規則）；老闆在 Supabase 後台的 Table Editor 改 `status`，前端會把 `pending` 顯示成「處理中」、`shipped` 顯示成「已出貨」。

## 其他

- 沒有金流：送出訂單只是把資料寫進 `orders`，不會收款。
- 「忘記密碼」為選做，這份參考實作沒有包含。
