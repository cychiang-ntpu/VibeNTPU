# 操作教學（docs/tutorials/）

本資料夾收錄課程所需的逐步操作教學與概念說明。每篇教學均以「學習目標 → 核心概念 → 操作步驟 → 疑難排解 → 參考資料」的結構撰寫，假設讀者沒有程式設計背景，但會說明每一個操作背後的技術機制，讓讀者不只「會按按鈕」，也能理解系統為何如此運作。

[← 回課程首頁](../../README.md)　｜　[學習檢核點](../checkpoints.md)　｜　[名詞解釋](../glossary.md)　｜　[延伸學習資源](../resources.md)

## 1. 建議閱讀順序

| 順序 | 教學 | 主要內容 | 建議閱讀時間點 | 對應檢核點 |
| --- | --- | --- | --- | --- |
| 1 | [before_class.md](before_class.md)：課前準備清單 | 帳號申請、軟硬體需求、每項工具的用途 | 10/7 上課前 | 檢核點 0 |
| 2 | [vscode_copilot_starter.md](vscode_copilot_starter.md)：VS Code 與 GitHub Copilot 入門 | 編輯器與工作區概念、Copilot 運作原理與模式、方案、隱私與負責任使用 | 10/7 上課前 | 檢核點 0 |
| 3 | [git_intro.md](git_intro.md)：Git 與 GitHub 入門 | 工作目錄、暫存區、本機與遠端儲存庫；commit、分支、同步與合併衝突 | 課前預習；第 1 週 | 檢核點 2、3 |
| 4 | [github_netlify_deploy.md](github_netlify_deploy.md)：GitHub 與 Netlify 部署 | 部署的意義、Netlify 匯入時的授權與 webhook 機制、發布目錄、HTTPS 與網域 | 第 1 週 | 檢核點 3 |
| 5 | [netlify_forms.md](netlify_forms.md)：Netlify Forms 表單串接 | 後端即服務（BaaS）的表單收集 | 第 2 週 | 檢核點 4 |
| 6 | [localstorage.md](localstorage.md)：LocalStorage 狀態保存 | 瀏覽器端儲存與其限制 | 第 2 週 | 檢核點 5 |
| 7 | [cicd.md](cicd.md)：持續整合與持續部署 | 從 Commit 到網站自動更新的流程 | 第 2 週 | 檢核點 6 |
| 選讀 | [vibe_check_ci.md](vibe_check_ci.md)：以 GitHub Actions 自動檢核 | 工作流程檔、觸發條件、執行器、狀態檢查 | 完成檢核點 3 之後 | 延伸任務（選做）：GitHub Actions 自動檢核 |
| 隨時 | [error_guide.md](error_guide.md)：疑難排解手冊 | 一般除錯方法與 Q1–Q18 常見問題 | 遇到問題時 | 全部 |

## 2. 使用建議

1. **先讀概念，再做操作。** 每篇教學前半段的「核心概念」說明了操作背後的原因。理解原因之後，即使介面改版、按鈕位置改變，也能自行找到對應功能。
2. **介面可能與文件不同。** VS Code、GitHub 與 Netlify 皆持續更新介面。若找不到文件描述的按鈕，請以各篇所附的官方文件為準。
3. **遇到問題時的處理順序。** 先依 [疑難排解手冊](error_guide.md) 的「一般除錯方法」自行診斷；15 分鐘內仍無法解決，請依課堂的 15 分鐘求助原則向同學、助教或教師求助，並附上你預期的結果、實際發生的狀況，以及已嘗試過的做法。
4. **互動教材。** 課程另提供可在瀏覽器操作的模擬器，例如 [Git 流程模擬器](../../lectures/wk01_1007_saas-storefront/slides/git_flow.html) 與 [社群媒體 SaaS 架構](../../lectures/wk01_1007_saas-storefront/slides/social_saas.html)。在 GitHub 網頁上點開 `.html` 只會看到原始碼，請將課程 repo clone 到電腦後以瀏覽器開啟。
