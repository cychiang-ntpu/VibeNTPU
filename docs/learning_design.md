# 教學設計理據

[← 回課程首頁](../README.md)

本文件說明本單元各項教學安排背後的學理依據，供授課教師、助教與有意改作本教材的教師參考。每一節依「原則 → 對本課程的意涵 → 在本 repo 中的具體做法」的順序撰寫，並於文末列出參考文獻。本文件亦說明本版教材為何移除先前版本的點數、等級與徽章設計。

**本版更新**：依授課教師回饋（「內容太難，請改成手把手一步步做」），學生教材（課前準備、各週 `README.md`、操作教學）已改寫為逐步操作的實作指南：每個編號只做一個動作，並附「完成後你應該看到」與常見狀況處理；概念說明壓縮為一句話。原有的理論內容移至 [深入原理（選讀）](deep_dive/README.md)，課堂不要求。本文件的學理論證維持不變。

---

## 1. 學習者分析

### 1.1 目標學習者

- 國立臺北大學非電機資訊背景之大學部學生，主要來自法律、商、公共事務、社會科學與人文學院。
- 多數未曾撰寫程式，對 HTML、伺服器、部署、版本控制等概念沒有操作經驗；但每天大量使用 SaaS 產品（社群媒體、通訊軟體、雲端文件），具有豐富的「使用者端」經驗。
- 課程時間僅兩次各 2 小時，學生人數多、電腦環境不一（個人筆電、電腦教室公用電腦、Windows 與 macOS 混合）。

### 1.2 常見迷思概念

學習者帶入課堂的先備知識不一定正確，未被處理的迷思概念會妨礙新知識的建構（Ambrose et al., 2010）。本課程預期並刻意處理下列迷思：

| 迷思概念 | 正確概念 | 處理方式 |
| --- | --- | --- |
| 「雲端」是一個抽象、神祕的地方 | 雲端是分布在資料中心的實體伺服器，由不同業者以服務形式出租 | 社群媒體架構圖逐層拆解至資料中心與 IaaS |
| 按下 Commit 就等於上傳到網路 | Commit 只在本機建立版本；Sync（push）才會送到 GitHub，GitHub 更新後才觸發 Netlify 部署 | 步驟卡與 Git 流程模擬器分開呈現三個位置；教師反覆強調 |
| AI 產生的程式碼一定正確 | AI 輸出是機率性的，可能錯誤、過時或不安全，須人工檢查與測試 | AI 使用規範中的驗證要求；自我檢核工具揭露缺漏 |
| 架設網站一定要自己管理伺服器 | 靜態網站可由託管平台透過 CDN 發布，無需自行維運伺服器 | 美食街類比引入後，轉換為 Netlify 的實際機制 |
| LocalStorage 是一種資料庫，資料安全地存在網站上 | LocalStorage 存在使用者自己的瀏覽器，換裝置即消失，且任何在該網頁執行的腳本皆可讀取 | 第 2 週以開發者工具實際觀察，並完成比較表 |
| 在本機雙擊打開 `index.html` 就能測試表單 | Netlify Forms 須部署到 Netlify 後，由平台端解析表單才能收件 | 疑難排解手冊與教師示範說明 `file:///` 與 HTTPS 網址的差異 |

### 1.3 常見焦慮

- **身分認同焦慮**：「我不是讀理工的料」。此類信念會降低投入與堅持（見第 6 節自我效能）。
- **弄壞東西的恐懼**：擔心誤刪檔案、帳號被收費或網站被他人看到錯誤。
- **公開曝光的壓力**：作品上線即可被任何人瀏覽，發表需面對同儕。
- **環境問題的挫折**：帳號驗證、Copilot 額度、公用電腦還原等非學習本身的障礙，最容易在第一堂課消耗學生的信心。

因此本課程的首要設計目標，不是在 4 小時內傳授最多技術，而是讓每位學生**在正確的概念框架下完成一次完整的產品發布流程**，並建立足以支持後續自學的自我效能。

---

## 2. 學習目標與布魯姆修訂版分類法

Anderson 與 Krathwohl（2001）將布魯姆分類法修訂為六個認知歷程層次：記憶（remember）、理解（understand）、應用（apply）、分析（analyze）、評鑑（evaluate）、創造（create），並區分事實、概念、程序與後設認知四類知識。

**對本課程的意涵**：非電資學生在 4 小時內不可能達到程式設計的高階能力，但仍可在「架構概念」與「產品決策」上達到分析、評鑑與創造層次。本課程刻意讓程序性知識（操作步驟）由步驟卡與 AI 輔助承擔，將課堂的認知資源保留給概念理解與取捨判斷。

**具體做法**：[course_plan.md](course_plan.md#1-學習目標) 的八項學習目標（LO1–LO8）均以可觀察的動詞撰寫，涵蓋理解（解釋架構）、應用（部署、串接）、分析（比較 LocalStorage 與資料庫）、評鑑（說明 CI/CD 的影響、資料倫理）到創造（建構 MVP 與發表）。

---

## 3. 建構式對準

Biggs（1996）提出建構式對準（constructive alignment）：學習目標、教學活動與評量任務應彼此一致，使學生為了通過評量而從事的活動，恰好就是達成目標所需的學習活動。

**具體做法**：

| 學習目標 | 教學活動 | 評量任務 |
| --- | --- | --- |
| LO1、LO2 架構理解 | 架構講義、互動教材、POE | 架構互動測驗（檢核點 1）；發表的架構說明（規準第 5 項） |
| LO3、LO4 產生與部署 | 示範 → 引導填寫 → 獨立完成；配對程式設計 | GitHub commit、Netlify 網址、自我檢核 Level 1（檢核點 2、3） |
| LO5 表單與資料倫理 | 表單串接、資料流教材、個資討論 | 後台收件證據、Level 2（檢核點 4）；規準第 6 項 |
| LO6 儲存比較 | 會員狀態實作、開發者工具觀察 | Level 3（檢核點 5）；學習單比較題 |
| LO7 CI/CD | 修改後觀察自動部署 | 部署紀錄與 commit 對應（檢核點 6）；規準第 4 項 |
| LO8 發表 | 發表模板、同儕回饋 | 1 分鐘發表（檢核點 7）；期末發表 |

完整對應見 [course_plan.md](course_plan.md) 與 [checkpoints.md](checkpoints.md)。

---

## 4. 認知負荷理論

### 4.1 原則

認知負荷理論（Cognitive Load Theory, CLT）指出，工作記憶容量有限，學習時的負荷可分為三類（Sweller, 1988; Sweller, van Merriënboer, & Paas, 1998）：

- **內在負荷（intrinsic load）**：由教材本身元素間的交互程度決定，例如同時理解「repo、commit、部署、網域」之間的關係。
- **外在負荷（extraneous load）**：由不良的教學設計造成，例如在多個分頁間來回尋找步驟、介面截圖與文字說明分離。
- **增生負荷（germane load）**：投入於建構基模（schema）的有益心力，例如比較兩種儲存方式的取捨。

設計目標是管理內在負荷、降低外在負荷，並將節省的容量導向增生負荷。

### 4.2 範例效應與逐步撤除

對新手而言，研讀完整解題範例（worked example）比直接解題更有效率，因為直接解題時的搜尋行為會消耗大量工作記憶（Sweller, 1988）。隨著能力提升，應逐步撤除範例中的步驟（fading），轉為獨立解題（Renkl & Atkinson, 2003）；否則對已具能力的學習者，詳盡的引導反而成為冗餘負荷，即專業反轉效應（expertise reversal effect; Kalyuga et al., 2003）。

### 4.3 注意力分散效應

當學習者必須在空間或時間上分離的多個資訊來源之間進行心智整合（例如一邊看投影片、一邊找網頁上的按鈕、再對照另一份文件），會產生額外的外在負荷，稱為注意力分散效應（split-attention effect; Chandler & Sweller, 1992）。

### 4.4 在本 repo 中的做法

| 設計 | 對應機制 |
| --- | --- |
| 每週講義每一段只引入一個新概念 | 管理內在負荷，避免元素同時交互 |
| 一頁式 [步驟卡](../lectures/wk01_1007_saas-storefront/steps.md) 集中全部操作，按鈕名稱與介面位置寫在同一行 | 降低注意力分散效應 |
| 各週 `README.md` 改為手把手實作指南，理論移至 [docs/deep_dive/](deep_dive/README.md)（選讀） | 降低新手的內在與外在負荷；深入內容保留給有興趣者，因應專業反轉效應 |
| [提示詞產生器](../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html) 以欄位填寫取代從零撰寫提示詞 | 部分完成範例（completion problem），降低搜尋負荷 |
| 「教師示範 → 引導填寫 → 獨立修改」三階段 | 範例效應與逐步撤除 |
| 以 VS Code 圖形介面操作 Git，不要求命令列 | 移除與學習目標無關的外在負荷 |
| 類比僅在引入時使用一次，隨即轉換為精確術語 | 以熟悉基模承接新概念，同時避免類比長期取代正確模型 |
| 延伸任務（選做）供進度較快者自選 | 因應專業反轉效應，避免對能力較強者造成冗餘 |

---

## 5. 動機設計

### 5.1 ARCS 動機模式

Keller（1987）的 ARCS 模式將學習動機拆解為注意（Attention）、相關（Relevance）、信心（Confidence）與滿足（Satisfaction）四個可設計的面向。

| 面向 | 本課程的做法 |
| --- | --- |
| 注意 | 第 1 週開場由教師現場示範「以一段提示詞產生網站並部署上線」，全班以手機開啟網址 |
| 相關 | 從學生每天使用的社群媒體拆解架構；學生自選與所屬學院或生活相關的產品題目 |
| 信心 | 課前成功經驗；每段目標明確且可達成；自我檢核工具提供具體的下一步 |
| 滿足 | 作品公開上線，並收到真實使用者的表單回應；於發表中展示成果 |

### 5.2 自我決定論

自我決定論（Self-Determination Theory, SDT）認為，當自主（autonomy）、勝任（competence）與關係（relatedness）三項基本心理需求獲得滿足時，內在動機與學習品質較高（Ryan & Deci, 2000）。

- **自主**：題目、視覺風格、延伸任務由學生選擇。
- **勝任**：檢核點將整體任務切分為可完成的階段，並提供即時、具體的回饋。
- **關係**：配對程式設計、作品巡禮與作品牆。

### 5.3 外在獎勵的風險：為何移除點數、等級與徽章

先前版本以經驗值、等級稱號與徽章包裝學習進度。本版予以移除，理由如下：

1. **過度辯證效應（overjustification effect）**：當原本具有內在興趣的活動被附加可預期的、與表現掛鉤的外在獎勵時，內在動機可能下降（Lepper, Greene, & Nisbett, 1973）。Deci、Koestner 與 Ryan（1999）的後設分析顯示，可預期的具體獎勵整體而言會削弱內在動機；具資訊性的正向回饋則不會，甚至有助益。
2. **控制性與資訊性的區別**：依 SDT 的認知評價理論，獎勵若被知覺為「控制行為」的工具，會損害自主感；若被知覺為「關於能力的資訊」，則可支持勝任感。點數與等級稱號偏向前者；明確說明「已達成什麼、證據為何、下一步是什麼」的檢核點偏向後者。
3. **社會比較與排行榜**：將進度量化為點數，容易引發比較。Hanus 與 Fox（2015）在大學課堂的縱貫研究中發現，採用徽章與排行榜的組別，其內在動機、滿意度與期末成績反而低於對照組。本課程對象的起點差異大，公開比較對落後者特別不利。
4. **目標受眾與語境**：大學課程的學習者期待被當作成人對待，幼稚化的包裝可能降低教材的可信度；授課教師亦反映此設計使內容顯得膚淺。

替代做法是 [學習檢核點](checkpoints.md)：每個檢核點說明完成條件、可驗證的證據與驗證方式，功能在於提供資訊性回饋與自我監控，而非獎勵。檢核點本身不計分，也不排名。

---

## 6. 自我效能

Bandura（1977）指出，自我效能（self-efficacy）即個人對自己能成功執行特定行為的信念，會影響是否投入、投入多少努力與遇挫時能否堅持。其四個來源及本課程的對應如下：

| 來源 | 說明 | 本課程的做法 |
| --- | --- | --- |
| 精熟經驗（mastery experiences） | 親身成功是最強的來源 | 課前以 Copilot 產生 Hello NTPU 頁面（檢核點 0）；第一個實作採低失敗率的結構化填寫；每個檢核點皆可在課堂時間內完成 |
| 替代經驗（vicarious experiences） | 觀察「與自己相似的人」成功 | [示範作品](../samples/README.md) 皆以學生可能提出的校園題目製作；作品巡禮觀摩同學作品；教師示範時刻意呈現錯誤與修正過程 |
| 言語說服（verbal persuasion） | 可信的他人給予具體回饋 | 回饋聚焦於策略與過程（例如「你換了一種描述方式請 AI 修改」），避免空泛稱讚或歸因於天分 |
| 生理與情緒狀態（physiological and emotional states） | 焦慮會被解讀為能力不足 | 明確告知「錯誤是正常現象」；提供 [疑難排解手冊](tutorials/error_guide.md)；15 分鐘求助原則降低長時間卡關的挫折 |

課前成功經驗的另一個作用，是把帳號、安裝與額度等環境問題移到課前處理，避免第一堂課的前 30 分鐘被非學習性障礙占用。

---

## 7. 提取練習與間隔

提取練習（retrieval practice）指主動從記憶中回想資訊。Roediger 與 Karpicke（2006）的實驗顯示，相較於重複閱讀，接受測驗的組別在一週後的保留量顯著較高，即測驗效應（testing effect）。間隔效應（spacing effect）則指將練習分散於不同時間，比集中練習更有利於長期保留（Cepeda et al., 2006）。

**具體做法**：

- 架構互動測驗於第 1 週講解後立即進行（檢核點 1），作為低風險的提取機會，不計分。
- 第 2 週開場以回顧題重新提取第 1 週的架構與 Git 流程概念，兩次提取間隔一週。
- 每週以出場券（exit ticket）請學生以自己的話寫出本週核心概念。
- 學習歷程檔案的反思題要求學生回想並說明具體事件，而非複述講義。

---

## 8. 形成性評量

Black 與 Wiliam（1998）的文獻回顧指出，形成性評量（formative assessment），即在學習過程中蒐集證據並據以調整教學與學習，對學習成效有顯著助益。Hattie 與 Timperley（2007）進一步指出，有效回饋須回答三個問題：目標為何、目前進展如何、下一步為何。

**具體做法**：

| 工具 | 蒐集的證據 | 如何據以調整 |
| --- | --- | --- |
| [網站自我檢核工具](../tools/vibe_check.html) | 學生 `index.html` 各項要求的達成情形 | 每一未通過項目附具體修正建議，學生可立即行動 |
| 課堂即時回饋卡（紅／綠） | 全班當下進度與卡關位置 | 綠色約達八成再進入下一段；紅色由助教個別協助 |
| 預測—觀察—解釋（Predict-Observe-Explain, POE; White & Gunstone, 1992） | 學生對機制的預期與實際觀察之差距 | 揭露迷思概念，例如預測「只按 Commit 網站是否會更新」 |
| 出場券 | 學生是否能以自己的話說明核心概念 | 教師於下週開場針對共同錯誤補充 |
| 快速檢核題（quick check） | 關鍵概念的理解 | 於轉換段落前確認，必要時重講 |

---

## 9. 配對程式設計

配對程式設計（pair programming）由兩人共用一台電腦，駕駛（driver）負責操作，導航員（navigator）負責檢查、查閱與規劃，並定期交換角色。Williams 等人（2000）的研究顯示配對產出的程式品質較佳；McDowell、Werner、Bullock 與 Fernald（2006）在入門程式設計課程的研究中發現，配對組的學生在課程完成率、對自身能力的信心與程式品質上均優於獨自作業的學生，且對修課前信心較低的學生尤其有益。

**具體做法**：兩人一組，導航員負責對照步驟卡並檢查 Copilot 的輸出；每個實作段落交換一次角色，確保雙方都有操作經驗。教師分組時可將較有信心與較緊張的學生搭配。需注意：兩人皆須完成各自的 repo 與部署，配對是協作學習的形式，而非分工代勞。

---

## 10. 心理安全感

Edmondson（1999）將心理安全感（psychological safety）定義為團隊成員共享的一種信念：在團隊中承擔人際風險（例如提問、承認錯誤、提出不同意見）是安全的。其研究顯示，心理安全感透過促進學習行為而影響團隊表現。

**具體做法**：

- 提供不需在全班面前開口的求助管道：課堂即時回饋卡、線上 [求助單](../.github/ISSUE_TEMPLATE/help_request.yml)。
- 15 分鐘求助原則將「求助」定義為專業行為，而非能力不足。
- 教師示範時公開犯錯並示範除錯過程。
- 作品巡禮採用「我喜歡／我希望／如果」的結構化回饋，避免評價性語言。
- 作品牆展示所有作品，不排名。

---

## 11. 真實學習

真實學習（authentic learning）強調在接近真實專業情境的任務中學習，包含真實的工具、開放性的問題、專家示範與成果的公開呈現（Herrington & Oliver, 2000）。

**具體做法**：

- 使用業界實際採用的工具鏈（VS Code、GitHub Copilot、Git／GitHub、Netlify），而非教學專用的模擬環境；學生在課後可直接沿用。
- 作品部署於公開網址，並以非同學的目標使用者進行市場驗證，使「收集名單」具有真實意義。
- 以精實創業的 MVP 概念框定任務，要求學生說明架構取捨，與產業決策情境一致。

**取捨**：真實工具會帶來真實的環境問題（帳號驗證、介面改版、額度限制）。本課程以課前準備、教師事先以新帳號走完流程、備援 `index.html` 與疑難排解手冊降低此風險，詳見 [teacher_guide.md](teacher_guide.md)。

---

## 12. 透明化評量與示範作品

透明化教與學（Transparency in Learning and Teaching, TILT）主張在指派任務時明確說明目的（purpose）、任務內容（task）與評量標準（criteria）。Winkelmes 等人（2016）的研究顯示，接受透明化作業設計的大學生在學業自信、歸屬感與技能掌握上均有提升，且對第一代大學生與弱勢學生的效果更明顯。提供不同品質等級的範例並搭配評語，可協助學生建立對品質標準的具體理解。

**具體做法**：

- [course_plan.md](course_plan.md#4-分析式評分規準) 事先公開六項準則、三個等級的分析式評分規準。
- [samples/](../samples/README.md) 提供 LOW、MEDIUM、HIGH 三份示範作品，並逐項以規準說明其表現與改進方向。
- 每個 [檢核點](checkpoints.md) 皆說明完成證據與驗證方式。

---

## 13. 參考文獻

- Ambrose, S. A., Bridges, M. W., DiPietro, M., Lovett, M. C., & Norman, M. K. (2010). *How Learning Works: Seven Research-Based Principles for Smart Teaching*. Jossey-Bass.
- Anderson, L. W., & Krathwohl, D. R. (Eds.). (2001). *A Taxonomy for Learning, Teaching, and Assessing: A Revision of Bloom's Taxonomy of Educational Objectives*. Longman.
- Bandura, A. (1977). Self-efficacy: Toward a unifying theory of behavioral change. *Psychological Review, 84*(2), 191–215.
- Biggs, J. (1996). Enhancing teaching through constructive alignment. *Higher Education, 32*(3), 347–364.
- Black, P., & Wiliam, D. (1998). Assessment and classroom learning. *Assessment in Education: Principles, Policy & Practice, 5*(1), 7–74.
- Cepeda, N. J., Pashler, H., Vul, E., Wixted, J. T., & Rohrer, D. (2006). Distributed practice in verbal recall tasks: A review and quantitative synthesis. *Psychological Bulletin, 132*(3), 354–380.
- Chandler, P., & Sweller, J. (1992). The split-attention effect as a factor in the design of instruction. *British Journal of Educational Psychology, 62*(2), 233–246.
- Deci, E. L., Koestner, R., & Ryan, R. M. (1999). A meta-analytic review of experiments examining the effects of extrinsic rewards on intrinsic motivation. *Psychological Bulletin, 125*(6), 627–668.
- Edmondson, A. (1999). Psychological safety and learning behavior in work teams. *Administrative Science Quarterly, 44*(2), 350–383.
- Hanus, M. D., & Fox, J. (2015). Assessing the effects of gamification in the classroom: A longitudinal study on intrinsic motivation, social comparison, satisfaction, effort, and academic performance. *Computers & Education, 80*, 152–161.
- Hattie, J., & Timperley, H. (2007). The power of feedback. *Review of Educational Research, 77*(1), 81–112.
- Herrington, J., & Oliver, R. (2000). An instructional design framework for authentic learning environments. *Educational Technology Research and Development, 48*(3), 23–48.
- Kalyuga, S., Ayres, P., Chandler, P., & Sweller, J. (2003). The expertise reversal effect. *Educational Psychologist, 38*(1), 23–31.
- Keller, J. M. (1987). Development and use of the ARCS model of instructional design. *Journal of Instructional Development, 10*(3), 2–10.
- Lepper, M. R., Greene, D., & Nisbett, R. E. (1973). Undermining children's intrinsic interest with extrinsic reward: A test of the "overjustification" hypothesis. *Journal of Personality and Social Psychology, 28*(1), 129–137.
- McDowell, C., Werner, L., Bullock, H. E., & Fernald, J. (2006). Pair programming improves student retention, confidence, and program quality. *Communications of the ACM, 49*(8), 90–95.
- Renkl, A., & Atkinson, R. K. (2003). Structuring the transition from example study to problem solving in cognitive skill acquisition: A cognitive load perspective. *Educational Psychologist, 38*(1), 15–22.
- Roediger, H. L., III, & Karpicke, J. D. (2006). Test-enhanced learning: Taking memory tests improves long-term retention. *Psychological Science, 17*(3), 249–255.
- Ryan, R. M., & Deci, E. L. (2000). Self-determination theory and the facilitation of intrinsic motivation, social development, and well-being. *American Psychologist, 55*(1), 68–78.
- Sweller, J. (1988). Cognitive load during problem solving: Effects on learning. *Cognitive Science, 12*(2), 257–285.
- Sweller, J., van Merriënboer, J. J. G., & Paas, F. G. W. C. (1998). Cognitive architecture and instructional design. *Educational Psychology Review, 10*(3), 251–296.
- White, R., & Gunstone, R. (1992). *Probing Understanding*. Falmer Press.
- Williams, L., Kessler, R. R., Cunningham, W., & Jeffries, R. (2000). Strengthening the case for pair programming. *IEEE Software, 17*(4), 19–25.
- Winkelmes, M.-A., Bernacki, M., Butler, J., Zochowski, M., Golanics, J., & Weavil, K. H. (2016). A teaching intervention that increases underserved college students' success. *Peer Review, 18*(1/2), 31–36.

### 13.1 線上資源

- TILT Higher Ed：<https://tilthighered.com/>
- Center for Self-Determination Theory：<https://selfdeterminationtheory.org/>
- ARCS Model（John M. Keller）：<https://www.arcsmodel.com/>
