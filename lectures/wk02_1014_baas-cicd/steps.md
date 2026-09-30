# 第 2 週一頁版步驟卡

做完一項勾一項。導航員讀步驟、駕駛操作，每做完一個 Part 交換。每一步的詳細說明見 [第 2 週手把手實作](README.md)，提示詞見 [prompts.md](prompts.md)。

---

## 開始前確認

- [ ] 手機打得開上週的 `https://…netlify.app` 網址
- [ ] VS Code：**檔案（File）→ 開啟最近使用的項目（Open Recent）** → 打開上週的 repo 資料夾
- [ ] 左側 **原始檔控制（Source Control）** → 按一次 **同步變更（Sync Changes）**

## Part 0：回顧上週（0:00，5 分鐘）

- [ ] 和搭檔完成 [學習單](worksheet.md) 第 1 題

## Part 1：資料去哪了（0:05，15 分鐘）

- [ ] 打開 [data_flow.html](slides/data_flow.html) → 分頁 **1. 表單資料的去向**
- [ ] 按 **沒有後端** → 填表 → **送出** → **重新整理網頁**：資料不見了
- [ ] 按 **使用 BaaS** → 填表 → **送出** → **重新整理網頁** → **換一台裝置**：後台資料還在
- [ ] 學習單第 2 題：寫下報名目標人數

## Part 2：Netlify Forms 候補名單（0:20，40 分鐘）→ 檢核點 4

- [ ] [提示詞產生器](../wk01_1007_saas-storefront/slides/prompt_builder.html) 按 **第 2 週** 產生提示詞（或複製 prompts.md 的提示詞 1）
- [ ] Copilot Chat → 模式選 **Agent** → 貼上 → 送出
- [ ] 按 **保留（Keep）** → `Ctrl+S` 存檔
- [ ] `Ctrl+F` 搜尋得到 `data-netlify` 和 `form-name`
- [ ] Netlify → 你的網站 → 左側 **Forms** → **Enable form detection**
- [ ] 原始檔控制 → 訊息 `新增早鳥名單表單` → **提交（Commit）** → **同步變更（Sync Changes）**
- [ ] Netlify → **Deploys** → 最上面一筆變成 **Published**（先同步才開偵測的話：**Trigger deploy**）
- [ ] 用 `https://…netlify.app` 網址（不是 `file:///`）自己填一次
- [ ] 請 3 位同學用手機填寫
- [ ] Netlify → **Forms** → **waitlist** 看到 3 筆以上 → **檢核點 4 完成**
- [ ] 交換駕駛與導航員

## Part 3：LocalStorage 會員畫面（1:00，35 分鐘）→ 檢核點 5

- [ ] data_flow.html 分頁 1：送出 → **重新整理網頁** → **換一台裝置** → **登出**，看差異
- [ ] Copilot Chat（Agent）貼上提示詞 2 → 送出 → **保留（Keep）** → 存檔
- [ ] 訊息 `新增會員畫面` → **提交（Commit）** → **同步變更（Sync Changes）** → 等 **Published**
- [ ] 手機：填表送出 → 看到「歡迎回來，〔姓名〕」
- [ ] 手機：重新整理，歡迎畫面還在
- [ ] 手機：按 **登出**，回到表單
- [ ] （選做）電腦按 `F12` → **Application** → **Local storage**，只看到名字
- [ ] [網站自我檢核工具](../../tools/vibe_check.html) Level 3 通過 → **檢核點 5 完成**
- [ ] 交換駕駛與導航員

## Part 4：自動更新 CI/CD（1:35，15 分鐘）→ 檢核點 6

- [ ] 手機記下目前按鈕的顏色；學習單第 3 題寫下預測
- [ ] Copilot Chat 貼上提示詞 3 → **保留（Keep）** → 存檔
- [ ] 訊息 `改按鈕顏色` → **提交（Commit）** → **同步變更（Sync Changes）**
- [ ] **不打開 Netlify**，等 30 秒，手機重新整理，看到新顏色 → **檢核點 6 完成**
- [ ] Netlify → **Deploys**：看到 `改按鈕顏色` 這一筆
- [ ] （選做）點較舊的一筆 → **Publish deploy** → 確認回到舊版 → 再把最新一筆 **Publish deploy**

## Part 5：一分鐘發表與收尾（1:50，10 分鐘）→ 檢核點 7

- [ ] 填好 README Part 5 的一分鐘講稿
- [ ] 向鄰組發表，並互填對方的表單 → **檢核點 7 完成**
- [ ] 學習單出場券
- [ ] [學習歷程檔案](../../templates/portfolio_README.md) 勾選檢核點

---

卡住時：先查 [疑難排解手冊](../../docs/tutorials/error_guide.md)（Q14–Q16 表單、Q17–Q18 LocalStorage）。自己試 15 分鐘仍沒有進展，請舉手。
