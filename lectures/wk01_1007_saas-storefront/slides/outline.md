# 第 1 週授課大綱（2026/10/7，教師用）


> 學生未做課前準備時，改用 [調整版授課計畫](../no_prep_plan.md)。

學生照 [../README.md](../README.md)（第 1 週手把手實作）的步驟 1–27 操作；本大綱列出每段教師要做的事與巡視重點。步驟編號與 README 一致，方便口頭指示（例如「現在做步驟 11」）。

---

## 課前 10 分鐘

- 助教在門口協助未完成 [課前準備](../../../docs/tutorials/before_class.md) 的學生。
- 投影設定：VS Code 字級（`editor.fontSize`）20 以上，`window.zoomLevel` 1–2。
- 示範用 repo 已連結 Netlify；備妥 QR Code 產生工具。
- 本機已開好四個互動網頁：[social_saas.html](social_saas.html)、[foodcourt.html](foodcourt.html)、[git_flow.html](git_flow.html)、[prompt_builder.html](prompt_builder.html)（單一 HTML 檔，可離線開啟）。

## Part 0：開場示範（0:00–0:05，步驟 1–2）

1. 在 VS Code 以一句提示詞請 Copilot 建立「三峽美食地圖」→ **保留（Keep）** → **提交（Commit）** → **同步變更（Sync Changes）**。
2. 展示 Netlify 自動部署，投影 QR Code。
3. 請學生在學習單第 1 題寫預測（事後對照）。

## Part 1：認識 SaaS 架構（0:05–0:35，步驟 3–8）

4. 一句話定義 SaaS，舉 IG、Gmail、Canva。不展開收費模型（留在選讀）。
5. 帶學生下載課程 ZIP 並打開 `social_saas.html`（步驟 3）；網路不佳時直接投影。
6. 分層架構圖：依序點 **手機 App**、**內容傳遞網路**、**推薦系統**、**推播服務**，每個只講一句；按 **對照 MVP 架構**（步驟 4）。
7. 請求流程演示：播放 **按讚**，逐步按 **下一步 →**；提問「愛心變紅之後，還有哪些服務在工作？」（步驟 5）。
8. 強調一句：推播必須經過 Apple 與 Google，大公司也使用別人的雲端服務。
9. 投影 README 的簡單架構圖（步驟 6），對照 [../social_media_architecture.md](../social_media_architecture.md)。
10. `foodcourt.html`：拖動拉桿、播放資料流；用美食街一句帶過自建與雲端服務，接著展示四塊對照表（步驟 7）。
11. 測驗（步驟 8），答對 80% 以上達成檢核點 1，學生貼綠色便利貼。

巡視重點：有人在 GitHub 網頁上直接點 `.html` 看到原始碼。

## Part 2：GitHub 建 repo 並 clone（0:35–0:55，步驟 9–12）

12. 一句話：repo 是會記住每次修改的專案資料夾；clone 是下載到自己電腦並保持同步。
13. 示範步驟 9–11 一次，全程唸出中英文按鈕名稱。可用 [git_flow.html](git_flow.html) 補充說明（選用）。
14. 學生操作。巡視重點：
    - VS Code 已開啟其他資料夾，看不到 **複製存放庫（Clone Repository）** → 開新視窗。
    - 瀏覽器授權頁面沒按 **Authorize**。
    - 右下角 **開啟（Open）** 通知被關掉 → **檔案** → **開啟資料夾**。
    - repo 忘記勾 README。
15. 提醒：repo 是公開的，不可放個人資料或密碼。交換駕駛與導航員。

## Part 3：用 Copilot 做網頁（0:55–1:30，步驟 13–19）

16. 選題：投影學院題目表，給 3 分鐘（步驟 13）。
17. 示範提示詞產生器 → Copilot Chat 選 **Agent** → 貼上 → 要求執行指令時 **略過（Skip）** → 檢查只改 `index.html` → **保留（Keep）** → **顯示預覽（Show Preview）**（步驟 14–17）。
18. 學生操作。巡視重點：模式仍在 Ask；`index.html` 建在錯的資料夾；Copilot 額度不足 → 改用 [../prompts.md](../prompts.md) 的網頁版 AI 備案。
19. 示範一則現成修改提示詞與「只改某區塊，其他維持不變」的寫法（步驟 18）。
20. 示範開發者工具的手機寬度檢查（步驟 19）。
21. 確認檢核點 2：repo 資料夾裡有可預覽的 `index.html`。交換駕駛與導航員。

## Part 4：提交、同步、Netlify 上線（1:30–1:55，步驟 20–25）

22. 一句話：提交是存在自己電腦；同步後 GitHub 與 Netlify 才看得到。
23. 示範步驟 20–23：提交 → 同步 → GitHub 重新整理 → Netlify **Add new project** → **Import an existing project** → **GitHub** → 選 repo → Build 設定留空 → **Deploy**。
24. 示範改名（步驟 24）：**Project configuration** → **General** → **Project details** → **Change project name**。
25. 學生操作。巡視重點：
    - Git 未設定 user.name／user.email（引導查 [疑難排解手冊](../../../docs/tutorials/error_guide.md)）。
    - 只提交沒同步，GitHub 上沒有 `index.html`。
    - Netlify 清單找不到 repo → **Configure the Netlify app on GitHub**。
    - Build command 或 Publish directory 被填了東西。
    - 檔名不是全小寫 `index.html`。
26. 先完成的學生協助鄰座。
27. 隨機投影兩三位學生的網站。確認檢核點 3：GitHub 有 commit、Netlify 顯示 Published、手機可開啟、自我檢核工具 Level 1 通過。

## Part 5：收尾（1:55–2:00，步驟 26–27）

28. 作品巡禮：「我喜歡／我希望／如果」一則回饋。
29. 出場券：對照開場預測。
30. 預告第 2 週：訪客留下 Email，資料要存到哪裡？

---

教師補充資料（選讀，不在課堂講授）：[SaaS 模式與網站運作](../../../docs/deep_dive/saas_and_web.md)、[社群媒體系統設計深入](../../../docs/deep_dive/social_media_systems.md)。
