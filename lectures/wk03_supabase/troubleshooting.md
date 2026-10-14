# 第 3 週疑難排解：Supabase

先按 `F12`（Mac：`⌥⌘I`）→ **Console**，看紅字寫什麼，再對照下表。

[回實作指南](README.md)

| 你看到的 | 原因 | 怎麼做 |
| --- | --- | --- |
| `supabase is not defined` | 載入 supabase-js 的 `<script>` 不在 `script.js` 之前，或沒加 | 打開 `index.html`，確認 `<head>` 裡有 `<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>`，而且在 `<script src="script.js">` 之前。沒有就重貼提示詞 1 |
| `Invalid API key` | anon key 貼錯、貼到一半，或貼成 service_role | Supabase → Project Settings → API，重新複製 **anon / public** 那一把，重貼提示詞 1 |
| `Failed to fetch`、`net::ERR_NAME_NOT_RESOLVED` | Project URL 打錯，或專案被暫停 | 確認網址是 `https://xxxx.supabase.co`；到儀表板看專案是否 **Paused**，是就按 **Restore** |
| `Email not confirmed` | 沒關閉 Email 確認 | Authentication → Sign In / Providers → Email → 關 **Confirm email** → Save。已註冊的帳號到 Users 頁面點該使用者 → **Confirm email** |
| `Password should be at least 6 characters` | 密碼太短 | 用 6 個字以上 |
| `User already registered` | 這個 Email 註冊過了 | 改用「登入」，或換一個 Email |
| `Invalid login credentials` | Email 或密碼打錯；或帳號在別人的專案註冊的 | 每位同學的商店各自有一套帳號，到同學的商店要重新註冊 |
| `new row violates row-level security policy` | 寫入資料時沒帶 `user_id`，或沒登入 | 先確認已登入；還是不行，貼 [提示詞](prompts.md)「出問題時」表格的 RLS 修正句 |
| `relation "public.cart_items" does not exist` | 步驟 4 的 SQL 沒執行成功 | 回 SQL Editor 重貼整份 [supabase_setup.sql](supabase_setup.sql) → Run，確認 Table Editor 有三張表 |
| 畫面正常，但 Table Editor 沒資料 | 還在用 localStorage | 貼 [提示詞](prompts.md)「出問題時」表格的 localStorage 修正句 |
| 註冊成功，但 `profiles` 沒有姓名 | 註冊時沒把姓名放在 `options.data.name` | 貼：`註冊時請把姓名放在 db.auth.signUp 的 options.data.name，其他不動。`；已註冊的帳號可在 Table Editor 手動補 |
| 手機可以登入，但「我的訂單」是空的 | 訂單是別的帳號下的 | 確認手機和電腦登入的是同一個 Email |
| Netlify 部署後報錯，本機正常 | 通常是 Redirect URL 沒加 | Authentication → URL Configuration 加入 netlify 網址 |
| 想從頭來過 | — | Table Editor 各表可 **Delete all rows**；Authentication → Users 可刪使用者；SQL 可重跑 |

**上週的 Netlify 表單還要留嗎？** 不用。這週表單都改送 Supabase，Netlify 的 `data-netlify` 設定可以拿掉（提示詞已要求）。Netlify 仍然負責放網站與自動更新。

**安全提醒：** `service_role` 鑰匙與資料庫密碼只能留在你的筆記，不要貼進提示詞、GitHub 或群組。anon key 放在網頁裡是正常的，安全靠 RLS。
