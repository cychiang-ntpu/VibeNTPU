# 第 3 週一頁版步驟清單：Supabase

做完一步就打勾。詳細說明見 [實作指南](README.md)，提示詞見 [提示詞](prompts.md)。

## Part 0 準備
- [ ] 1 VS Code 開 `pickle-charm-shop` → 同步變更 → Copilot（Agent）可開

## Part 1 建立 Supabase 專案
- [ ] 2 supabase.com/dashboard → Sign in with GitHub → 建組織（Free）
- [ ] 3 New project：名稱 `pickle-charm`、產生並記下資料庫密碼、Region Tokyo → Create
- [ ] 4 SQL Editor → New query → 貼 [supabase_setup.sql](supabase_setup.sql) → Run → Table Editor 看到 profiles、cart_items、orders
- [ ] 5 Authentication → Sign In / Providers → Email → 關 Confirm email → Save
- [ ] 6 Project Settings → API：記下 Project URL、anon key（不要抄 service_role）
- [ ] 7 Authentication → URL Configuration：Site URL 填 netlify 網址；Redirect URLs 加 netlify 網址與 `http://localhost:*`
- [ ] 交換駕駛／導航員

## Part 2 真正的註冊與登入
- [ ] 8 Copilot：貼「約定」→ 貼提示詞 1（換掉【】）→ 保留 → `Ctrl+F` 找到 `supabase-js`
- [ ] 9 貼提示詞 2 → 保留 → 預覽小視窗有密碼欄、註冊／登入切換
- [ ] 10 本機預覽：註冊 `test1@example.com` → 歡迎回來 → 重新整理仍在 → 登出 → 登入
- [ ] 11 Supabase：Authentication → Users 有 test1；Table Editor → profiles 有姓名
- [ ] 12 提交 `接上 Supabase 註冊登入` → 同步 → Published → 手機登入同一帳號
- [ ] 交換駕駛／導航員

## Part 3 購物車存進雲端
- [ ] 13 貼提示詞 3 → 保留 → 登入後加入商品、按＋ → 重新整理仍在 → Table Editor → cart_items 有列
- [ ] 14 提交 `購物車存進 Supabase` → 同步 → Published → 手機登入看到同樣購物車
- [ ] 15 無痕視窗註冊 `test2@example.com` → 購物車是空的
- [ ] 交換駕駛／導航員

## Part 4 訂單與後台
- [ ] 16 貼提示詞 4 → 保留 → 預覽下單 → 看到「訂單已送出，訂單編號」
- [ ] 17 Table Editor → orders 看到那一筆（name、phone、address、items、total、status）
- [ ] 18 把 status 改成 `shipped` → Export CSV → 網站「我的訂單」顯示已出貨
- [ ] 19 提交 `訂單存進 Supabase` → 同步 → Published → 手機下單
- [ ] 交換駕駛／導航員

## Part 5 收尾
- [ ] 20 到兩位同學的商店註冊、下單；看自己後台的 orders 與 Users
- [ ] 21 出場券
- [ ] 22 公用電腦：登出 GitHub、Netlify、Supabase、VS Code
