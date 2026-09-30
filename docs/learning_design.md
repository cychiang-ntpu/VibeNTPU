# 🧠 這個 repo 是怎麼設計的？——教育心理學設計說明

> 給老師、助教，也給好奇的同學：這門課的每個安排都有它的「為什麼」。
> 知道自己**為什麼這樣學**，本身就是一種學習（這叫後設認知 metacognition）。

[← 回課程首頁](../README.md)

---

## 🎯 設計對象：完全沒有電機資訊背景的同學

我們假設你：
- 沒寫過程式，也不知道 HTML 是什麼；
- 聽到「伺服器」「部署」會有點緊張；
- 可能曾經覺得「我不是讀理工的料」。

所以這門課的設計目標不是「塞進最多技術」，而是讓你在 4 小時內**親手做出一個真的能用的東西**，並且**相信自己做得到**。

---

## 🗺️ 一張表看懂：理論 → 這個 repo 的哪個設計

| 教育心理學概念 | 一句話白話 | 在這個 repo 裡長什麼樣子 |
| --- | --- | --- |
| **ARCS 動機模式**（Keller） | 動機 = 注意 × 相關 × 信心 × 滿足 | 每週 README 的「🎬 開場魔術」「💼 跟你有什麼關係」「✅ 小步成功」「🎉 作品牆」 |
| **自我決定論 SDT**（Deci & Ryan） | 人在「自主、勝任、歸屬」被滿足時最有內在動機 | 自選創業題目與 AI 工具（自主）；小關卡與健檢站（勝任）；兩人一組、作品牆（歸屬） |
| **自我效能**（Bandura） | 「我做得到」的信念來自成功經驗、看別人成功、被鼓勵、情緒安定 | 課前關卡先成功一次；[samples/](../samples/) 看示範作品；錯誤急救手冊安定情緒 |
| **認知負荷理論**（Sweller） | 大腦工作記憶很小，一次只塞一件新東西 | 每段只教一個新概念；[一頁版步驟卡](../lectures/wk01_1007_saas-storefront/steps.md)；[咒語產生器](../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html)用填表取代從零寫咒語 |
| **範例效應 → 逐步撤除**（worked example & fading） | 先看完整示範，再做填空，最後獨立完成 | 老師示範 → 咒語產生器填空 → 自由改版（「我做、我們做、你做」） |
| **鷹架與近側發展區**（Vygotsky） | 在「自己做不到、但有人帶就做得到」的區間學最快 | 每週三層任務：🟢 必做主線／🟡 挑戰支線／🔵 延伸閱讀，依能力自選 |
| **雙重編碼**（Paivio） | 文字＋圖像一起記得更牢 | 「美食街比喻」全課貫穿；每個概念都有圖或互動動畫 |
| **先備知識與基模**（Ausubel） | 新知識要掛在已經懂的東西上 | 從同學每天滑的 IG、LINE 切入，先看 [社群媒體的 SaaS 架構圖](../lectures/wk01_1007_saas-storefront/social_media_architecture.md)，再縮小到自己的 MVP |
| **真實學習**（authentic learning） | 在真實情境、用真實工具學，才帶得走 | 使用業界標準的 VS Code、GitHub、Copilot，而不是教學專用玩具；作品真的上線、真的收名單 |
| **具體 → 抽象**（concreteness fading） | 先用熟悉的東西理解，再換上專業術語 | 先說「訂單代收中心」，再說「BaaS」；先說「集點卡」，再說「LocalStorage」 |
| **提取練習與間隔效應** | 「想起來」比「再讀一次」更能記住；隔一段時間再考更有效 | 互動小測驗；第 2 週開場回想第 1 週；每週出場券 |
| **經驗學習圈**（Kolb） | 做 → 反思 → 歸納 → 再應用 | 每個實作後都有「🏗️ 架構呼應」把操作連回概念；學習單的「預測—觀察—解釋」 |
| **成長型思維**（Dweck） | 能力是可以練出來的，錯誤是成長的材料 | 錯誤訊息被稱為「經驗值」；健檢站失敗時說「還差一步」；[卡關急救手冊](tutorials/error_guide.md) |
| **心理安全感**（Edmondson） | 敢問、敢錯，才敢嘗試 | 紅綠便利貼求救法、15 分鐘求救法則、匿名[求救單](../.github/ISSUE_TEMPLATE/help_request.yml) |
| **遊戲化學習** | 用遊戲的回饋機制讓進度「看得見」 | [冒險地圖](quest_map.md)、徽章、經驗值、[冒險護照](../templates/passport_README.md)、完課證書 |
| **透明化評量**（TILT） | 先讓你知道「好作品長怎樣」，再請你做 | [samples/](../samples/) 入門／進階／卓越三級示範作品＋評語；[評分規準](course_plan.md#-評分方式) |
| **同儕教學與結對程式設計** | 教別人是最好的學習；兩人一組互相照應 | 「駕駛／領航員」輪流制；作品互評「我喜歡／我希望／如果」 |
| **後設認知** | 想想自己是怎麼學的 | 冒險護照的每週 3-2-1 反思 |

---

## 🔬 七個關鍵設計，詳細說明

### 1. 15 分鐘內一定要有第一次成功 ✅
**理論**：自我效能最強的來源是「親身成功經驗」（mastery experience）。
**做法**：
- 課前關卡 Q0 只要求你跟 AI 說一句話，做出「Hello NTPU」網頁。**上課前你就已經成功過一次了。**
- 第 1 週開場，老師用 3 分鐘現場示範「一句話 → 網站上線」，讓你看到終點線。
- 第一個實作不是寫程式，而是「填表」（咒語產生器），失敗機率極低。

### 2. 一次只教一件新東西 🧩
**理論**：認知負荷理論。新手的工作記憶一次只能處理 3～5 個新元素。
**做法**：
- 每週 README 的每一段都標明「🆕 本段新概念」，永遠只有一個。
- 操作步驟全部集中在一頁 `steps.md`，上課開著照做，不用在多個分頁間跳來跳去（避免注意力分散效應）。
- 專有名詞第一次出現時，一定先配比喻（「訂單代收中心」），第二次才用術語（BaaS）。

### 3. 「我做 → 我們做 → 你做」📐
**理論**：範例效應與逐步撤除鷹架。
**做法**：
| 階段 | 第 1 週 | 第 2 週 |
| --- | --- | --- |
| 我做（完整示範） | 老師示範詠唱＋部署 | 老師示範表單＋後台 |
| 我們做（填空） | 咒語產生器填空 | 咒語產生器第 2 週模式 |
| 你做（獨立） | 自由改版到滿意 | 自己決定要加什麼功能 |

### 4. 錯誤 = 經驗值 💪
**理論**：成長型思維、心理安全感。
**做法**：
- 卡關急救手冊不叫「FAQ」，而是「打怪攻略」：每個錯誤都寫「這很正常，因為…」。
- **紅綠便利貼**：電腦上貼綠色＝順利，貼紅色＝需要幫忙，不用舉手打斷課堂。
- **15 分鐘法則**：自己試 15 分鐘沒進展就求救。卡太久不是毅力，是浪費。
- 健檢站的失敗訊息會直接告訴你「請跟 AI 說：……」，把挫折轉成下一步行動。

### 5. 進度看得見 📈
**理論**：遊戲化的即時回饋、目標梯度效應（越接近終點越有動力）。
**做法**：
- [冒險地圖](quest_map.md)：8 個主線關卡＋支線任務，每關有經驗值。
- [Vibe 健檢站](../tools/vibe_check.html)：丟進你的 `index.html`，立刻看到哪些徽章亮了。
- [冒險護照](../templates/passport_README.md)：貼到你自己的 GitHub repo，每完成一關就打勾。

> ⚠️ **設計上刻意避開的**：我們**不做排行榜**。研究指出排行榜會讓落後的同學更想放棄（社會比較焦慮）。
> 徽章是「告訴你做到了什麼」的資訊，不是拿來跟別人比的。作品牆展示**每一個人**的作品，不排名。

### 6. 跟你有關係 💼
**理論**：ARCS 的「相關性」、SDT 的「自主性」。
**做法**：
- 創業題目自己選，[samples/](../samples/README.md) 有依學院分類的點子（法律、商、公共事務、社科、人文）。
- AI 工具自己選（Claude／ChatGPT／Gemini），風格顏色自己選。
- 每週 README 都有一段「💼 這跟我以後有什麼關係？」：不管你以後做行銷、法務、公職還是研究，都會用到 SaaS 和 AI。

### 7. 一起學，不孤單 🤝
**理論**：SDT 的「歸屬感」、同儕教學。
**做法**：
- **駕駛／領航員**：兩人一組，一人操作（駕駛）、一人看步驟卡提醒（領航員），每個實作交換。
- **作品巡禮（Gallery Walk）**：用手機逛同學的網站，留下「我喜歡／我希望／如果」三句回饋。
- **[作品牆](../showcase/README.md)**：每個人的網站都會被展示，課程結束後也看得到。

---

## 📚 延伸閱讀（給想深入的老師與同學）

| 主題 | 資源 |
| --- | --- |
| ARCS 動機模式 | [ARCS Model（John Keller 官方網站）](https://www.arcsmodel.com/) |
| 自我決定論 | [Center for Self-Determination Theory](https://selfdeterminationtheory.org/theory/) |
| 自我效能 | [Self-efficacy（維基百科）](https://en.wikipedia.org/wiki/Self-efficacy) |
| 認知負荷理論 | [Cognitive load（維基百科）](https://en.wikipedia.org/wiki/Cognitive_load) |
| 範例效應 | [Worked-example effect（維基百科）](https://en.wikipedia.org/wiki/Worked-example_effect) |
| 近側發展區與鷹架 | [Zone of proximal development](https://en.wikipedia.org/wiki/Zone_of_proximal_development)・[Instructional scaffolding](https://en.wikipedia.org/wiki/Instructional_scaffolding) |
| 雙重編碼 | [Dual-coding theory（維基百科）](https://en.wikipedia.org/wiki/Dual-coding_theory) |
| 提取練習 | [RetrievalPractice.org](https://www.retrievalpractice.org/)・[Testing effect](https://en.wikipedia.org/wiki/Testing_effect)・[Spacing effect](https://en.wikipedia.org/wiki/Spacing_effect) |
| 經驗學習 | [Experiential learning（維基百科）](https://en.wikipedia.org/wiki/Experiential_learning) |
| 成長型思維 | [Mindset（維基百科）](https://en.wikipedia.org/wiki/Mindset) |
| 心理安全感 | [Psychological safety（維基百科）](https://en.wikipedia.org/wiki/Psychological_safety) |
| 遊戲化學習 | [Gamification of learning（維基百科）](https://en.wikipedia.org/wiki/Gamification_of_learning) |
| 透明化教學 | [TILT Higher Ed](https://tilthighered.com/) |
| 布魯姆分類法（學習目標） | [Bloom's taxonomy（維基百科）](https://en.wikipedia.org/wiki/Bloom%27s_taxonomy) |
| 同儕教學 | [Peer instruction](https://en.wikipedia.org/wiki/Peer_instruction)・[Pair programming](https://en.wikipedia.org/wiki/Pair_programming) |
| 後設認知 | [Metacognition（維基百科）](https://en.wikipedia.org/wiki/Metacognition) |
| 綜合 | Ambrose et al.《How Learning Works: Eight Research-Based Principles for Smart Teaching》（2nd ed., 2023） |
