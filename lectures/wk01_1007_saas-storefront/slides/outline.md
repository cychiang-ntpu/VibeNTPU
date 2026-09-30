# 第 1 週授課大綱（2026/10/7）

本單元不另製投影片，以講義 [../README.md](../README.md) 為主軸，搭配四個互動網頁與 VS Code 現場示範。互動網頁皆為單一 HTML 檔，可直接以瀏覽器離線開啟，不受教室網路狀況影響。架構圖的完整版（Mermaid，GitHub 上可直接顯示）見 [../social_media_architecture.md](../social_media_architecture.md) 與 [../saas_architecture.md](../saas_architecture.md)。

---

## 1. 互動教材

| 檔案 | 使用段落 | 內容 |
| --- | --- | --- |
| [social_saas.html](social_saas.html) | 段落 1（7.2、7.4） | 架構圖（點選元件看說明、MVP 對照）；操作流程動畫（按讚、發布限時動態、瀏覽動態牆、傳送訊息）；商業模式與測驗 |
| [foodcourt.html](foodcourt.html) | 段落 1（7.3–7.5） | 自建與購買的累積成本比較（月數拉桿）；課程架構資料流；測驗 |
| [git_flow.html](git_flow.html) | 段落 2（8.2） | Git 流程模擬（修改 → Stage → Commit → Sync → Netlify 更新；Pull；回復版本）；VS Code 原始檔控制介面導覽；測驗 |
| [prompt_builder.html](prompt_builder.html) | 段落 3（9.4） | 依欄位產生提示；可選擇 AI 工具；完整度檢查；一鍵複製 |

## 2. 課前 10 分鐘

- 助教於教室門口協助尚未完成 [課前準備](../../../docs/tutorials/before_class.md) 的學生。
- 投影設定：VS Code 字級（`editor.fontSize`）20 以上，`window.zoomLevel` 設為 1 至 2。
- 確認示範用 repo 已連結 Netlify，並備妥 QR Code 產生工具。

## 3. 段落 0：開場示範（0:00–0:05）

1. 在 VS Code 以一句提示請 Copilot 建立「三峽美食地圖」頁面 → Keep → Commit → Sync → Netlify 自動部署。
2. 將網址轉為 QR Code，學生以手機開啟。
3. 學生於學習單第 1 題寫下預測（POE 的預測階段；ARCS 動機模型的「引起注意」）。

## 4. 段落 1：現代網路服務與 SaaS 架構（0:05–0:35）

4. 課堂調查：每天使用 Instagram 或 LINE、每月訂閱串流或 AI 服務的人數 → 引出訂閱與廣告兩種模式。
5. 買斷與 SaaS 對照表；說明高固定成本、低邊際成本與經常性收入（MRR）。提及流失率與 CAC，指向核心閱讀第 4 節的計算範例。
6. 〔social_saas.html 架構圖〕由上而下說明各層；點選 CDN、推薦系統、推播三個元件。
7. 〔social_saas.html 操作流程〕播放「按讚」，提問：「愛心變色後，還有哪些服務在工作？」→ 訊息佇列、非同步處理、樂觀更新。
8. 重點：推播必須經由 Apple 與 Google 的服務，大型平台同樣使用外部 SaaS；各公司的差異在於哪些自建、哪些租用。
9. 〔social_saas.html 商業模式〕廣告制平台出售注意力 → 推薦系統的優化目標與其社會爭議（連結學生經驗；ARCS 的「關聯」）。
10. 轉折：「大型平台有數千名工程師，新創團隊如何在有限資源下建立產品？」
11. 〔foodcourt.html 成本比較〕以深山蓋餐廳與進駐美食街的類比引入，隨即切換為自建與購買的專業比較：前期成本、上市時間、維運負擔、供應商鎖定。
12. 〔foodcourt.html 資料流〕＋〔social_saas.html MVP 對照〕→ 本課程四個元件與其服務模式（Netlify 為 PaaS、Netlify Forms 為 BaaS）。
13. 說明本課程不直接操作 IaaS 的理由：早期新創的人力與時間比伺服器費用更稀缺。
14. 〔測驗〕學生以手機作答，答對 80% 以上達成檢核點 1（提取練習）。

## 5. 段落 2：以 GitHub 建立專案儲存庫（0:35–0:55）

15. 概念說明：Git 與 GitHub 的區別；repo 包含完整歷史；commit 是具識別碼的快照；stage 決定納入哪些變更。
16. 〔git_flow.html 模擬器〕教師操作一輪，強調「commit 只在本機，sync 後 GitHub 與 Netlify 才看得到」。
17. 〔git_flow.html 介面導覽〕對照 VS Code 原始檔控制畫面的各編號位置。
18. 教師示範：建立 Public repo 並勾選 Add README → VS Code 從 GitHub 複製。
19. 學生依 [steps.md](../steps.md) 第 2 節操作。巡視重點：瀏覽器授權視窗、存放位置、按下「開啟」。
20. 提醒：repo 為公開，commit 歷史會永久保留，不可放入個人資料或金鑰。

## 6. 段落 3：以 GitHub Copilot 建立產品前端（0:55–1:30）

21. Vibe coding 的定義（Karpathy，2025）與其界限：降低撰寫門檻，但不降低對結果負責的要求。
22. 選題：以學院題目表引導，強調選擇自己能具體描述使用者與痛點的題目（自我決定理論的「自主」）。
23. 概念說明：Ask 與 Agent 模式的差異；Agent 模式的風險（修改非預期檔案、提議執行指令、幻覺）；課堂規則為指令一律略過、接受前先讀差異。
24. 教師完整示範「三峽租屋雷達」：提示產生器 → Agent 模式 → 檢視差異 → Keep → Show Preview（範例效應）。
25. 〔prompt_builder.html〕學生填寫至完整度 100% 後複製，於 Copilot 送出。
26. 自主修改：示範具體、限定範圍、合併相關需求的修改提示；說明免費方案的使用額度。
27. 示範驗證清單：手機寬度檢查、Console 錯誤檢查、虛構內容標示（[prompts.md 第 3 節](../prompts.md#3-ai-輸出的驗證清單)）。
28. 巡視確認檢核點 2：repo 中有可預覽的 `index.html`。

## 7. 段落 4：提交、同步與 Netlify 部署（1:30–1:55）

29. 教師示範：輸入有意義的提交訊息 → Commit → Sync → GitHub 網頁確認 → Netlify 從 Git 匯入 → Deploy。
30. 概念說明：Netlify 監聽推送事件、取得檔案、建置（本課程為空）、原子化發布、配發子網域與 HTTPS、分發至 CDN。
31. 學生依 [steps.md](../steps.md) 第 4 節操作；助教處理紅色便利貼。
32. 巡視重點：Git 使用者名稱與 Email 未設定、只 Commit 未 Sync、檔名非 `index.html`、Build 設定未留空。
33. 邀請先完成的學生協助鄰座（同儕教學）。
34. 重點：未購買或設定任何伺服器，網站已由 CDN 以 HTTPS 對外服務。
35. 隨機投影兩到三位學生的網站，簡短說明其題目與設計選擇（ARCS 的「滿足」）。
36. 確認檢核點 3：GitHub 可見 commit、Netlify 部署成功、自我檢核工具 Level 1 通過。

## 8. 段落 5：作品巡禮與出場券（1:55–2:00）

37. 作品巡禮：以「我喜歡／我希望／如果」提供一則具體回饋。
38. 出場券：對照段落 0 的預測並解釋差異（POE 的解釋階段）。
39. 預告第 2 週：「訪客按下送出之後，資料會到哪裡？靜態網站如何接收資料？」
