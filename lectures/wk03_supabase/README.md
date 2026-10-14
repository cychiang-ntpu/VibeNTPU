# 第 3 週手把手實作：用 Supabase 做真正的會員、購物車與訂單後台

上週的「登入」只是記在瀏覽器裡的模擬，訂單則是送進 Netlify 的表單收件匣。這週換成 **Supabase**：一個免費的「後端即服務」，提供真正的帳號系統（Email＋密碼，可登入、登出、換裝置）、資料庫（購物車和訂單存在雲端，換手機也看得到），以及一個可以直接看、改、匯出訂單的後台。

做完之後，你的 Pickle Charm Shop 會：

1. 讓訪客用 Email 與密碼**註冊、登入、登出**；換一台手機登入，還是同一個人。
2. **購物車跟著帳號走**：在電腦加入的商品，手機登入後也看得到。
3. **訂單存進雲端資料庫**，你在 Supabase 後台看到每一筆：誰、買了什麼、多少錢、什麼時候；可以改狀態、匯出 CSV。
4. 每位會員只看得到**自己的**購物車和訂單（別人看不到你的）。

[提示詞](prompts.md)　｜　[一頁版步驟清單](steps.md)　｜　[給 Supabase 貼的 SQL](supabase_setup.sql)　｜　[疑難排解](troubleshooting.md)　｜　[老師的完成版](../../samples/pickle-charm-shop-supabase/README.md)

---

## 先看這裡：Supabase 在架構中的位置

| 上週（Netlify Forms） | 這週（Supabase） |
| --- | --- |
| 登入狀態只記在這台瀏覽器 | 帳號存在雲端，任何裝置都能登入 |
| 購物車只在這台瀏覽器 | 購物車存在資料庫，跟著帳號走 |
| 訂單進表單收件匣，只能看 | 訂單是資料表，可以查、改狀態、匯出 |
| 不用設定任何東西 | 要在 Supabase 建專案、建資料表、貼一把「公開鑰匙」到網站 |

兩種都是「後端即服務」。差別是 Supabase 給你真正的資料庫和帳號系統，代價是多 20 分鐘的設定。

**兩個名詞：**
- **Project URL** 與 **anon key（公開鑰匙）**：網站用它們找到你的 Supabase 專案。anon key 本來就設計成可以放在網頁裡被看到，安全靠下面的 RLS。
- **RLS（Row Level Security，列級安全）**：資料庫的規則，決定「誰可以看、改哪些資料」。這週會貼好一套規則，讓每個人只碰得到自己的購物車和訂單。**沒有 RLS，任何人都能用你的公開鑰匙讀到所有訂單**，所以這一步不能跳過。

## 兩小時怎麼分配（實際版）

Supabase 的設定對第一次用的人要花不少時間，所以課堂只做到「真正的註冊登入＋訂單進後台」；**購物車存進雲端（Part 3）改為課後作業**，上週的瀏覽器購物車本週照用即可。

| 時間 | 段落 | 老師做什麼 | 學生完成 |
| --- | --- | --- | --- |
| 0:00–0:10 | 開場 | 投影上週的網站，示範「換一台手機就不認得你」；用一張表說明 Supabase 補上什麼（見下方）。 | 學習單第 1 題 |
| 0:10–0:35 | Part 1 建立 Supabase 專案 | **先全程示範一次（8 分鐘）**，再讓學生做；助教巡視步驟 4（貼 SQL）與步驟 6（抄鑰匙）。 | 步驟 2–7 |
| 0:35–1:05 | Part 2 真正的註冊與登入 | 示範貼約定、提示詞 1、2；提醒「這週本機就能註冊」。 | 步驟 8–12 |
| 1:05–1:40 | Part 4 訂單進資料庫與後台 | 示範提示詞 4、Table Editor 改 status、Export CSV。 | 步驟 16–19 |
| 1:40–1:55 | Part 5 互相下單 | 投影自己的 orders 表，看同學的訂單進來。 | 步驟 20–21 |
| 1:55–2:00 | 收尾 | 說明課後作業（Part 3 購物車）；公用電腦登出。 | 步驟 22 |

**先做順序提醒：** 跳過 Part 3 直接做 Part 4 時，提示詞 4 的購物車仍是上週的 localStorage 版本，這沒有問題；回家做完 Part 3 再貼一次提示詞 4 的第 2 點（清空 cart_items）即可，提示詞裡已註明。

**時間不夠時的底線：** 做到步驟 12（手機能用 Supabase 帳號登入）就算完成本週目標；訂單進後台可以回家做。

**完整版（4 小時或自學）分配：**

| 時間 | 段落 | 完成後你會有 |
| --- | --- | --- |
| 0:00 | Part 0 準備（5 分鐘） | VS Code 開著上週的 pickle-charm-shop，Copilot 可用 |
| 0:05 | Part 1 建立 Supabase 專案（20 分鐘） | 一個專案、三張資料表、安全規則、Project URL 與 anon key |
| 0:25 | Part 2 真正的註冊與登入（30 分鐘） | 用 Email 密碼註冊；Supabase 後台看到使用者；換裝置登入 |
| 0:55 | Part 3 購物車存進雲端（25 分鐘） | 電腦加入商品，手機登入後看得到 |
| 1:20 | Part 4 訂單進資料庫與後台（25 分鐘） | 下單後在 Table Editor 看到訂單；改狀態；匯出 CSV |
| 1:45 | Part 5 收尾（15 分鐘） | 互相下單；看自己的後台；出場券 |

**上課方式：** 兩人一組，駕駛與導航員每個 Part 交換。每一步做完先對照「完成後你應該看到」。

---

## Part 0：準備（0:00–0:05）

### 步驟 1：打開上週的專案（約 5 分鐘）

1. VS Code → **檔案（File）→ 開啟最近使用的項目（Open Recent）** → `pickle-charm-shop`。沒有的話照 [上週步驟 2](../wk02_1014_baas-cicd/pickle_charm_lab.md) 重新 clone。
2. 點左側 **原始檔控制**，按一次 **同步變更（Sync Changes）**，確保是最新版。
3. 按 `Ctrl+Alt+I`（Mac：`⌃⌘I`）打開 Copilot，模式選 **Agent**。

**完成後你應該看到：** 檔案總管有 `index.html`、`script.js`、`styles.css`；上週做的註冊視窗與購物車都在。

**如果不一樣：** 上週沒做完 → 先把老師的完成版 [samples/pickle-charm-shop](../../samples/pickle-charm-shop/) 三個檔案複製進你的資料夾（覆蓋），提交、同步後再開始。

---

## Part 1：建立 Supabase 專案（0:05–0:25）

這一段全部在 Supabase 網站上點按鈕和貼文字，不寫程式。

### 步驟 2：註冊 Supabase（約 3 分鐘）

1. 打開 <https://supabase.com/dashboard>。
2. 按 **Sign in with GitHub**，授權。
3. 第一次會請你建立組織（Organization）：名稱填你的名字，方案選 **Free**，按 **Create organization**。

**完成後你應該看到：** Supabase 的儀表板，左上角是你的組織名稱。

### 步驟 3：建立專案（約 4 分鐘）

1. 按 **New project**。
2. **Name** 填 `pickle-charm`。
3. **Database Password**：按 **Generate a password**，然後**把它複製存到你的筆記**（這把密碼之後很少用到，但遺失就要重設）。
4. **Region** 選離台灣最近的，例如 **Northeast Asia (Tokyo)**。
5. 按 **Create new project**，等 1–2 分鐘。

**完成後你應該看到：** 專案頁面左側有一排圖示（Table Editor、SQL Editor、Authentication…），上方不再顯示「Setting up project」。

### 步驟 4：建立資料表與安全規則（貼 SQL，約 5 分鐘）

1. 在 VS Code 或瀏覽器打開課程的 [supabase_setup.sql](supabase_setup.sql)，全選複製（`Ctrl+A`、`Ctrl+C`）。
2. 回到 Supabase，點左側 **SQL Editor**（圖示像一張紙上有 `>_`）。
3. 按 **New query**（或 **+ New**）。
4. 在編輯區貼上（`Ctrl+V`）。
5. 按右下角綠色的 **Run**（或 `Ctrl+Enter`）。

**完成後你應該看到：** 下方出現「Success. No rows returned」。點左側 **Table Editor**，看到三張表：`profiles`、`cart_items`、`orders`。

**如果不一樣：** 出現紅字錯誤 → 把編輯區清空，重新貼一次完整的 SQL 再 Run（這份 SQL 可以重複執行）。還是錯 → 把紅字截圖貼到群組。

### 步驟 5：關閉 Email 確認（上課用，約 2 分鐘）

Supabase 預設要求註冊後到信箱點確認連結才能登入。課堂上為了省時間先關掉；課後可以再打開。

1. 點左側 **Authentication**（人像圖示）→ 上方分頁 **Sign In / Providers**（舊版叫 **Providers**）。
2. 點 **Email**，把 **Confirm email** 關掉（開關變灰），按 **Save**。

**完成後你應該看到：** Email 那一列顯示 Enabled，Confirm email 為關閉。

**如果不一樣：** 找不到 Confirm email → 在 **Authentication → Settings** 或 **Sign In / Providers → Email** 裡找「Confirm email」或「Enable email confirmations」。

### 步驟 6：抄下 Project URL 與 anon key（約 3 分鐘）

1. 點左側齒輪 **Project Settings** → **API**（新版在 **Project Settings → Data API** 或首頁的 **Connect** 按鈕）。
2. 找到 **Project URL**（像 `https://abcdefgh.supabase.co`），按旁邊的複製圖示，貼到你的筆記。
3. 找到 **Project API keys** 裡標示 **anon / public** 的那一串（很長，以 `eyJ` 開頭；新版可能叫 **Publishable key**，以 `sb_publishable_` 開頭），複製貼到筆記。

**完成後你應該看到：** 筆記裡有兩行：一個網址、一串鑰匙。

**不要抄 `service_role` / `secret` 那一把**：那是管理員鑰匙，放到網頁上等於把後台鑰匙交給所有人。

### 步驟 7：加入允許的網址（約 3 分鐘）

1. 左側 **Authentication** → **URL Configuration**。
2. **Site URL** 填你上週的 Netlify 網址，例如 `https://pickle-charm-123.netlify.app`。
3. **Redirect URLs** 按 **Add URL**，加入同一個網址，再加一個 `http://localhost:*`（本機預覽用）。按 **Save**。

**完成後你應該看到：** Redirect URLs 列出兩筆。

**這一步在架構中的位置：** 你剛剛租了一個「真正的廚房」：資料庫＋帳號系統。接下來只要把網站接上它。

請交換駕駛與導航員。

---

## Part 2：真正的註冊與登入（0:25–0:55）

### 步驟 8：把 Supabase 接進網站（約 8 分鐘）

1. 打開 [提示詞](prompts.md)，先貼最上面的 **「約定」**（這週的對話第一次貼）。
2. 複製 **提示詞 1：接上 Supabase**，把裡面的 `【Project URL】` 和 `【anon key】` 換成你筆記裡的兩行，貼上 → Enter → **保留（Keep）**。
3. 在 `index.html` 按 `Ctrl+F` 搜尋 `supabase-js`。

**完成後你應該看到：** `index.html` 的 `<head>` 或 `script.js` 前面多了一行載入 `@supabase/supabase-js` 的 `<script>`，以及一段寫著你的 URL 和 key 的程式。

**如果不一樣：** Copilot 把 key 寫成 `YOUR_KEY` 之類的佔位文字 → 再貼一次，確認提示詞裡的【】已換成真的值。

### 步驟 9：註冊、登入、登出改用 Supabase（約 10 分鐘）

1. 貼 **提示詞 2：真正的註冊與登入** → **保留**。
2. 對 `index.html` 按右鍵 → **Show Preview**。按右上角 **登入**。

**完成後你應該看到：** 小視窗多了「密碼」欄位，和兩個分頁或按鈕：「註冊」與「登入」。本機預覽**可以**直接註冊（這週不用等部署，因為資料是送到 Supabase，不是 Netlify）。

### 步驟 10：在本機註冊第一個帳號（約 5 分鐘）

1. 在預覽的小視窗選「註冊」，填姓名、Email（可以用假的，例如 `test1@example.com`）、密碼（至少 6 個字），送出。
2. 重新整理預覽。
3. 按「登出」。
4. 再按「登入」，用同一組 Email 密碼登入。

**完成後你應該看到：** 註冊後右上角顯示「歡迎回來，〔姓名〕」；重新整理還在；登出後消失；登入後再出現。

**如果不一樣：** 顯示「Email not confirmed」→ 步驟 5 沒關 Confirm email。顯示「Invalid API key」→ 步驟 8 的 key 貼錯。其他見 [疑難排解](troubleshooting.md)。

### 步驟 11：到 Supabase 後台看使用者（約 3 分鐘）

1. Supabase → 左側 **Authentication** → **Users**。
2. 左側 **Table Editor** → `profiles`。

**完成後你應該看到：** Users 列出 `test1@example.com`；`profiles` 表有一列，`name` 是你填的姓名。

### 步驟 12：提交、同步、換裝置登入（約 4 分鐘）

1. 原始檔控制 → 訊息 `接上 Supabase 註冊登入` → **提交** → **同步變更**。
2. Netlify → Deploys 等 **Published**。
3. 用**手機**打開你的 netlify.app 網址，按登入，用剛才在電腦註冊的帳號登入。

**完成後你應該看到：** 手機上顯示「歡迎回來，〔姓名〕」。這就是「帳號在雲端」：上週的做法換手機就不認得你。

**這一步在架構中的位置：** 註冊與登入走的是「前端 → Supabase Auth（帳號服務）」。

請交換駕駛與導航員。

---

## Part 3：購物車存進雲端（兩小時版本改為課後作業）

### 步驟 13：購物車跟著帳號走（約 10 分鐘）

1. 貼 **提示詞 3：購物車存進 Supabase** → **保留**。
2. 預覽：登入後加入兩種商品，打開購物車面板按「＋」。
3. 重新整理。

**完成後你應該看到：** 購物車內容和數量都在；Supabase → Table Editor → `cart_items` 出現對應的列（`user_id`、`product_name`、`qty`）。

**如果不一樣：** `cart_items` 沒資料但畫面有 → Copilot 可能還在用 localStorage，貼 [疑難排解](troubleshooting.md) 的修正句。沒登入時加入商品 → 應該跳出「請先登入」或自動打開登入視窗（提示詞有要求）。

### 步驟 14：提交、同步，手機驗證（約 8 分鐘）

1. 提交 `購物車存進 Supabase` → 同步 → 等 Published。
2. 手機打開網址，用同一帳號登入，按右上角購物車。

**完成後你應該看到：** 手機上的購物車和電腦上一樣。在手機改數量，回電腦重新整理，數量也變了。

### 步驟 15：確認別人看不到你的購物車（約 7 分鐘）

1. 在瀏覽器開一個**無痕視窗**，打開你的網址，註冊第二個帳號 `test2@example.com`。
2. 打開購物車。

**完成後你應該看到：** 第二個帳號的購物車是空的。這是步驟 4 貼的 RLS 規則在生效：每個人只讀得到自己的列。

**這一步在架構中的位置：** 購物車走的是「前端 → Supabase Database（資料表 cart_items）」，由 RLS 把關。

請交換駕駛與導航員。

---

## Part 4：訂單進資料庫與後台（1:20–1:45）

### 步驟 16：下訂單存進 orders 表（約 8 分鐘）

1. 貼 **提示詞 4：訂單存進 Supabase** → **保留**。
2. 預覽：登入、加入商品、填收件資料、送出訂單。

**完成後你應該看到：** 畫面顯示「訂單已送出」與訂單編號；購物車清空。

### 步驟 17：在後台看訂單（約 5 分鐘）

這就是你的「訂單管理後台」。

1. Supabase → **Table Editor** → `orders`。
2. 點開那一列。

**完成後你應該看到：** 欄位有 `created_at`（時間）、`user_id`、`email`、`name`、`phone`、`address`、`items`（商品清單，JSON）、`total`、`status`（預設 `pending`）。

### 步驟 18：像老闆一樣處理訂單（約 5 分鐘）

1. 在 `orders` 表，雙擊那一列的 `status` 欄，改成 `shipped`，按 Enter（或下方 **Save**）。
2. 按表格上方的 **Export**（或 **…** → **Export to CSV**），下載。
3. 回到網站重新整理，打開「我的訂單」。

**完成後你應該看到：** CSV 打開是一張訂單表；網站的「我的訂單」顯示那筆訂單狀態變成 `shipped`（提示詞 4 有做這個區塊）。

### 步驟 19：提交、同步（約 3 分鐘）

提交 `訂單存進 Supabase` → 同步 → 等 Published → 手機下一筆真的訂單 → 後台看到。

**這一步在架構中的位置：** 訂單走「前端 → Supabase Database（orders）」。老闆看訂單的畫面，就是 Supabase 的 Table Editor，不用自己寫後台。

請交換駕駛與導航員。

---

## Part 5：收尾（1:45–2:00）

### 步驟 20：互相下單（約 7 分鐘）

1. 網址貼到群組，到兩位同學的商店註冊、下單。
2. 回自己的 Supabase 後台看 `orders` 多了幾筆、`Authentication → Users` 多了誰。

### 步驟 21：出場券（約 5 分鐘）

寫在 [學習單](worksheet.md)：
1. 上週和這週的「登入」差在哪裡？用一句話說。
2. 為什麼 anon key 可以放在網頁裡，service_role key 不行？
3. 老闆想知道「今天總共賣了多少錢」，在後台怎麼做？

### 步驟 22：下課前（約 3 分鐘）

公用電腦：瀏覽器登出 GitHub、Netlify、Supabase；VS Code 帳戶登出。

---

## 課後作業（下週前）

**必做**
- [ ] 完成 Part 3（步驟 13–15）：購物車存進 Supabase。做完後再貼一次 [提示詞 4](prompts.md) 的第 2 點，讓下單後清空雲端購物車。
- [ ] 補完課堂未完成的步驟，確認手機能註冊、登入、下單，後台看得到。
- [ ] 回 Supabase → Authentication → Sign In / Providers → Email，把 **Confirm email 打開**；用一個真的 Email 註冊一次，確認收到確認信、點完才能登入。
- [ ] 學習歷程檔案補上第 3 週反思，提交、同步。

**選做**
- [ ] 貼 [延伸提示詞](prompts.md)：忘記密碼（Supabase 會寄重設信）。
- [ ] 在 Supabase SQL Editor 貼 [supabase_setup.sql](supabase_setup.sql) 最後的「老闆報表」查詢，看每種商品賣了幾個。
- [ ] 到 [作品牆](../../showcase/README.md) 更新你的作品說明。

**個資與安全提醒：**
- 訂單含姓名、電話、地址。不公開、不轉傳；課程結束後到 Table Editor 刪除資料，或在 Project Settings → General 刪除整個專案。
- `service_role` 鑰匙和資料庫密碼不要貼到任何地方（群組、提示詞、GitHub）。
- Supabase 免費專案一週沒人用會暫停（Paused）；到儀表板按 **Restore** 即可，資料不會消失。
