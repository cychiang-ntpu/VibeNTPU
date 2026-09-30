# 第 2 週（2026/10/14）｜SaaS 的靈魂 — 串接後端與體驗自動化迭代

對應關卡：📦 Q4 收單 → 💾 Q5 記住客人 → 🔄 Q6 自動傳真魔法 → 🎤 Q7 MVP 發表
時間：2 小時（兩節）

> **課前準備（同學）**：確認上週的網站用手機打得開，並準備好你的 `index.html`（電腦裡的檔案，或到 GitHub repo 點檔案 → 下載）。上週還沒完成？先照 [第 1 週步驟卡](../wk01_1007_saas-storefront/steps.md) 補完，卡住就請助教幫忙。
>
> **上課請開著 👉 [steps.md（一頁版步驟卡）](steps.md)**。
>
> **兩人一組**：延續上週的 🚗 駕駛／🧭 領航員，今天從上週最後一位駕駛的隊友開始開車。

---

## 🎯 本週目標

上完課你應該能：

1. **解釋**為什麼創業初期（MVP 階段）不需要自己寫後端，以及 BaaS 怎麼幫我們省下這些工作。
2. 用一行 `data-netlify="true"` **串接** Netlify Forms，並在後台看到收集到的名單。
3. **比較**「雲端資料庫」與「瀏覽器 LocalStorage」兩種記住使用者的方式，說出各自適合的情境。
4. **體驗** CI/CD：改版上傳 GitHub 後，網站自動更新，並說明它為什麼讓科技公司能每天改版。
5. 用 1 分鐘向別人**介紹**自己的 MVP 與背後的架構。

## 💼 這跟我有什麼關係？

- 「先驗證有沒有人要，再投入大錢」這個**精實創業**思維，不只用在科技業：開店、辦活動、寫企劃、選研究題目都適用。
- 今天做的「早鳥名單」是真實新創最常用的市場驗證工具。**下課後把網址分享出去，你就是在做真正的市場調查。**
- 你會第一次看見「資料」在網路上是怎麼流動的，之後讀到個資外洩、隱私權的新聞，你會更懂它在說什麼。

## ⏱️ 時程

| 段落 | 時間 | 內容 | 🆕 本段唯一新概念 | 教材 |
| --- | --- | --- | --- | --- |
| 0 | 0:00–0:05 | 🔁 暖身回想：上週的四塊積木 | —（回想） | [worksheet.md](worksheet.md) |
| 1 | 0:05–0:20 | 🧠 觀念建立：SaaS 怎麼記住使用者？ | BaaS | [slides/data_flow.html](slides/data_flow.html) ① |
| 2 | 0:20–1:00 | 📦 實戰一：零後端名單收集系統 | Netlify Forms | [prompts.md](prompts.md)、[Forms 教學](../../docs/tutorials/netlify_forms.md) |
| 3 | 1:00–1:35 | 💾 實戰二：打造無縫體驗（模擬登入狀態） | LocalStorage | [slides/data_flow.html](slides/data_flow.html) ①②、[LocalStorage 解說](../../docs/tutorials/localstorage.md) |
| 4 | 1:35–1:50 | 🔄 實戰三：體驗 CI/CD | CI/CD | [slides/data_flow.html](slides/data_flow.html) ③、[CI/CD 教學](../../docs/tutorials/cicd.md) |
| 5 | 1:50–2:00 | 🎤 MVP 發表＋收尾 | — | [Pitch 模板](../../docs/pitch_template.md) |

---

## 段落 0｜🔁 暖身回想（5 分鐘）

**不看筆記**，跟隊友一起回答（寫在 [學習單](worksheet.md) 第 1 題）：

1. SaaS 跟買斷制最大的差別是什麼？
2. 美食街的四塊積木是哪四塊？
3. 上週我們已經用到哪三塊？還差哪一塊？

> 🧠 **為什麼要先回想？** 隔一週再「想起來」，比重讀一次筆記更能把知識存進長期記憶（間隔效應＋提取練習）。
> 想不起來也沒關係，「努力想」這個動作就已經在幫你了。

<details>
<summary>對答案</summary>

1. 軟體放在雲端、打開瀏覽器就能用、按月訂閱；程式寫一次可以租給全世界。
2. 前端（裝潢）、GitHub（保險箱＋傳真機）、Netlify（攤位）、BaaS（訂單代收中心）。
3. 已經用了前端、GitHub、Netlify；**今天要補上最後一塊：BaaS！**

</details>

---

## 段落 1｜🧠 觀念建立：SaaS 怎麼記住使用者？（15 分鐘）🔥【本次重點】

🆕 **本段唯一新概念**：BaaS（Backend as a Service，後端即服務）。

### 1.1 🤔 客人按下「註冊」，資料去哪了？

打開 👉 **[slides/data_flow.html](slides/data_flow.html)** 第一個分頁，先選 **「沒有後端」**，在模擬手機上填表送出……

**資料哪裡都沒去！** 因為我們的餐廳只有「裝潢（前端）」，還沒有「廚房（後端）」和「倉庫（資料庫）」。

### 1.2 自己蓋廚房要多久？

| 要做的事 | 需要學的技術 | 時間 |
| --- | --- | --- |
| 租伺服器 | Linux、雲端主機 | 數天 |
| 寫接收資料的程式 | Python／Node.js、API | 數週 |
| 設計資料庫 | SQL | 數週 |
| 顧好資安 | 防駭、個資保護 | 永無止境 |

### 1.3 🚀 精實創業：先試吃，再開店

> **創業初期（MVP 階段），我們的目標只是「驗證有沒有人想用」。**

- **MVP（最小可行產品）**：用最少成本做出剛好能測試市場的產品。
- 📖 **真實故事**：Dropbox 產品還沒做好，只放了一支[示範影片](https://techcrunch.com/2011/10/19/dropbox-minimal-viable-product/)收集候補名單，一夜之間從 5,000 人暴增到 75,000 人，證明了市場需求。
- 流程：**建造 → 測量 → 學習**，越快跑完一圈越好。📖 [The Lean Startup 原則](https://theleanstartup.com/principles)

### 1.4 🦹 現代駭客解法：BaaS

> **我們不自己蓋廚房，我們直接去「借」別人的資料庫！**

回到 data_flow.html，切換成 **「有 BaaS（data-netlify="true"）」** 再送出一次：資料飛進 Netlify 後台了！
今天的主角就是 **Netlify Forms**：只要在表單加一行字，Netlify 就幫你收資料。

---

## 段落 2｜📦 實戰一：零後端名單收集系統（40 分鐘）

🆕 **本段唯一新概念**：Netlify Forms，一行字接上「訂單代收中心」。

| 步驟 | 動作 | 教材 |
| --- | --- | --- |
| 2.1 👀 我做 | 老師示範：加表單 → 開啟偵測 → 上傳 → 填表 → 看後台（5 分鐘） | 投影 |
| 2.2 🤝 我們做 | 用 [咒語產生器](../wk01_1007_saas-storefront/slides/prompt_builder.html)（切到「第 2 週」模式）或 [咒語 1](prompts.md#咒語-1加入早鳥候補名單waitlist表單)，**先把你的 index.html 貼給 AI**，請它加上早鳥表單 | [prompts.md](prompts.md) |
| 2.3 🔍 自我檢查 | 用 `Ctrl+F` 搜尋 `data-netlify`，找得到就對了；或丟進 [Vibe 健檢站](../../tools/vibe_check.html) 看 Level 2 | [健檢站](../../tools/vibe_check.html) |
| 2.4 ⚠️ 開偵測 | Netlify → 你的專案 → **Forms** → **Enable form detection**（**最多人漏掉這步！**） | [Forms 教學 步驟 2](../../docs/tutorials/netlify_forms.md#步驟-2在-netlify-開啟表單偵測form-detection) |
| 2.5 上傳 | 新的 `index.html` 拖到 GitHub 覆蓋舊檔 → Commit | [steps.md](steps.md) |
| 2.6 🤝 互相填 | 網址丟群組，**幫 3 位同學填表**，也請他們幫你填 | — |
| 2.7 🎉 看後台 | Netlify → **Forms** → **waitlist**，看到名單了！ | [Forms 教學 步驟 4](../../docs/tutorials/netlify_forms.md#步驟-4到後台查看收集到的名單) |

> 🔑 **關鍵魔法**：交代 AI「請務必在表單 `<form>` 標籤中加入 `data-netlify="true"` 屬性」。

> 🏗️ **架構呼應**：只要加一行字，Netlify 這個房東就會變成你的警衛，**免費幫你把客人的資料收好放在雲端後台**。這就是串接 BaaS 的威力！
> 📦 **Q4 過關**：後台收到 3 筆以上＋健檢站 Level 2 全亮 → **收單徽章（60 XP）**

🔄 **交換駕駛／領航員！**

---

## 段落 3｜💾 實戰二：打造 SaaS 的無縫體驗 — 模擬登入狀態（35 分鐘）

🆕 **本段唯一新概念**：LocalStorage，存在客人瀏覽器裡的「集點卡」。

### 3.1 兩種記住客人的方式（10 分鐘）

回到 [data_flow.html](slides/data_flow.html) 第一個分頁，送出表單後試試：
- 按 **🔄 重新整理網頁**：歡迎畫面還在（集點卡記得你）。
- 按 **📱 換一台手機**：歡迎畫面不見了，**但 Netlify 後台的名單還在！**

| | ☁️ 雲端資料庫（剛剛做的） | 💻 LocalStorage |
| --- | --- | --- |
| 比喻 | 櫃檯的「會員登記簿」 | 帶回家的「集點卡」 |
| 存在哪 | Netlify 雲端 | 客人自己的瀏覽器 |
| 誰看得到 | 老闆 | 只有那台裝置 |
| 換電腦還在嗎 | ✅ | ❌ |

接著玩第二個分頁 **「集點卡 vs 登記簿」分類小遊戲**，檢查自己真的懂了。📖 [LocalStorage 白話解說](../../docs/tutorials/localstorage.md)

### 3.2 Vibe Coding 實作（25 分鐘）

使用 [咒語 2：送出後原地變成會員儀表板](prompts.md#咒語-2送出後原地變成會員儀表板)，效果：

> 🎉 歡迎回來，**小明**！這是您的會員儀表板，建置中……

1. 送出表單後，網頁**不跳轉**，原地變成歡迎畫面。
2. 重新整理，歡迎畫面**還在**。
3. 按「登出」，回到表單。
4. 上傳 GitHub → 用手機測試 → 丟進 [健檢站](../../tools/vibe_check.html) 看 Level 3。

📂 參考 🥇 卓越示範作品：[samples/HIGH](../../samples/HIGH/index.html)

> 🏗️ **架構呼應**：這雖然是前端的視覺魔法，換台電腦就不見了。但在創業初期的 Demo 時，**這樣就足以讓投資人完整體驗你的 SaaS 服務流程！**
> 💾 **Q5 過關**：歡迎畫面會出現、重新整理還在＋健檢站 Level 3 全亮 → **記憶徽章（50 XP）**

🔄 **交換駕駛／領航員！**

---

## 段落 4｜🔄 實戰三：體驗 CI/CD（持續整合／部署）（15 分鐘）

🆕 **本段唯一新概念**：CI/CD，設計圖一改，分店自動換裝潢。

1. 先在 [data_flow.html](slides/data_flow.html) 第三個分頁「CI/CD 自動傳真機」看一次模擬（也試試 ⏪ 回到上一版）。
2. **🔮 預測**：等一下你上傳新版後，需要進 Netlify 按什麼按鈕嗎？（寫在學習單）
3. 請 AI 做一個**明顯**的修改（例如按鈕改亮橘色）：[咒語 3](prompts.md#咒語-3快速改版體驗-cicd)。
4. 拖曳上傳到 GitHub 覆蓋舊檔 → Commit。
5. **不要進 Netlify**，直接用手機重新整理……🪄 **網頁已經自動更新了！**

> 🏗️ **架構呼應**：這叫做 **CI/CD 自動化部署**！這就是為什麼 IG、Netflix 每天都在更新，你卻不會遇到「維修中」。
> 只要架構對了（GitHub 串 Netlify），老闆一句話，AI 寫出 Code，上傳後幾十秒內全世界的用戶都會看到更新！**這就是科技公司的敏捷開發！**
> 🔄 **Q6 過關** → **魔法師徽章（50 XP）**

📖 [CI/CD 完整教學](../../docs/tutorials/cicd.md)

---

## 段落 5｜🎤 MVP 發表＋收尾（10 分鐘）

### 5.1 一分鐘 MVP 發表（跟隔壁組互相發表，老師抽 2～3 組上台）

用手機展示你的網站，套用這個句型：

> 「我們的產品是 ______，解決 ______ 的問題。我們用 **AI 輔助開發** 做出前端，部署在 **Netlify** 上，用 **Netlify Forms** 收集早鳥名單，目前已經收到 ___ 筆！」

🎤 **Q7 過關** → **說書人徽章（80 XP）**。完整期末版 👉 [Pitch 模板](../../docs/pitch_template.md)

### 5.2 收尾

1. **出場券**：完成 [學習單](worksheet.md) 最後一題。
2. **冒險護照**：勾選今天的關卡，寫下第 2 週 3-2-1 反思，並回答「跟第 1 週比，我覺得自己『做得到』的信心」。
3. 主線全破的同學 → 到 [Vibe 健檢站](../../tools/vibe_check.html) 列印你的 **🎓 完課證書**！

---

## 📂 本週教材

| 檔案 | 用途 |
| --- | --- |
| [steps.md](steps.md) | 一頁版步驟卡 |
| [slides/data_flow.html](slides/data_flow.html) | 互動教材：資料去哪了（有／無 BaaS、換手機）、集點卡 vs 登記簿分類遊戲、CI/CD 自動傳真機 |
| [slides/outline.md](slides/outline.md) | 老師上課大綱 |
| [prompts.md](prompts.md) | 本週咒語集（表單、會員儀表板、快速改版、急救） |
| [worksheet.md](worksheet.md) | 學習單：暖身回想、預測、出場券 |
| [announcement.md](announcement.md) | 課前公告 |

## 🏠 期末前要做的事

- [ ] 🟢 **必做**：冒險護照填好第 2 週反思與 AI 使用紀錄。
- [ ] 🟡 **挑戰**：把網址分享給 5 位**不是同學**的目標客群（支線 🎯 市場獵人），記錄在護照的「市場驗證紀錄」。
- [ ] 🟡 **挑戰**：設定表單 Email 通知（支線 🔔 小鈴鐺）。
- [ ] 🟡 **挑戰**：在自己的 repo 裝上 [自動健檢](../../docs/tutorials/vibe_check_ci.md)（支線 🤖 機器人助教）。
- [ ] 🔵 **延伸**：研究 [Supabase](https://supabase.com/) 或 [Firebase](https://firebase.google.com/)：做「真的」會員系統，下一塊積木是什麼？
- [ ] 🖼️ 到 [作品牆](../../showcase/README.md) 登記你的作品！

## 📚 延伸學習

- [Netlify Forms 官方文件](https://docs.netlify.com/manage/forms/setup/)
- [MDN：Window.localStorage（繁中）](https://developer.mozilla.org/zh-TW/docs/Web/API/Window/localStorage)
- [GitHub：什麼是 CI/CD？](https://github.com/resources/articles/devops/ci-cd)
- [Y Combinator：How to Build an MVP（影片）](https://www.ycombinator.com/library/Io-how-to-build-an-mvp)
- 更多 👉 [延伸學習資源總整理](../../docs/resources.md)

---

上一週 👉 [第 1 週](../wk01_1007_saas-storefront/README.md)　｜　期末準備 👉 [Pitch 模板](../../docs/pitch_template.md)
