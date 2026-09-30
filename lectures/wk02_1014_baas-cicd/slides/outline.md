# 第 2 週授課大綱（2026/10/14，教師用）

學生照 [第 2 週手把手實作](../README.md) 操作，教師依下表帶節奏。互動網頁 [data_flow.html](data_flow.html) 直接用瀏覽器開啟，不需網路。原理補充（選講）見 [精實創業、MVP 與指標](../../../docs/deep_dive/lean_startup_and_metrics.md)、[表單、儲存與 CI/CD](../../../docs/deep_dive/forms_storage_cicd.md)。

## 課前準備

- 教師自己的示範網站已完成第 1 週，並且**尚未**開啟表單偵測（現場示範用）。
- 投影畫面同時開：VS Code、Netlify 後台（Forms、Deploys）、手機投影或模擬器。
- 開啟 [提示詞產生器](../../wk01_1007_saas-storefront/slides/prompt_builder.html) 的 **第 2 週** 模式。

## 流程

| 時間 | 段落 | 教師動作 | 學生完成 |
| --- | --- | --- | --- |
| 0:00（5） | Part 0 回顧 | 學習單第 1 題，1 分鐘討論後公布答案；帶出「報名資料哪裡都沒去」 | 學習單第 1 題 |
| 0:05（15） | Part 1 資料去哪了 | data_flow.html 分頁 1：**沒有後端** → 送出 → 重新整理；**使用 BaaS** → 送出 → 重新整理 → 換一台裝置。用 3–4 句話說明 MVP 與早鳥名單 | 學習單第 2 題（報名目標） |
| 0:20（40） | Part 2 Netlify Forms | 先完整示範一次（5 分鐘）：Agent 模式送提示詞 1 → Keep → `Ctrl+F` 找 `data-netlify` → **Enable form detection** → Commit＋Sync → 等 **Published** → 用 netlify.app 網址填表 → Forms → waitlist。之後巡堂 | 3 筆以上資料，檢核點 4 |
| 1:00（35） | Part 3 LocalStorage | data_flow.html 分頁 1 示範重新整理、換裝置、登出。現場按 `F12` → Application → Local storage 給大家看存了什麼，並說明這只是模擬登入 | 手機測試送出、重新整理、登出；Level 3，檢核點 5 |
| 1:35（15） | Part 4 CI/CD | 先請學生猜「要不要去 Netlify 按」。投影自己的網站改按鈕顏色 → Commit＋Sync → 不碰 Netlify → 手機重新整理。再打開 Deploys 看紀錄，示範 **Publish deploy** 回到上一版（data_flow.html 分頁 3 可輔助） | 手機看到新版，檢核點 6 |
| 1:50（10） | Part 5 發表與收尾 | 說明一分鐘講稿格式；兩組互相發表，抽 1–2 組上台；提醒出場券 | 檢核點 7、出場券 |

## 巡堂時最常見的狀況

| 狀況 | 處理 |
| --- | --- |
| Copilot 沒有改檔案，只在對話裡貼程式碼 | 模式改成 **Agent** 再送一次 |
| 後台沒有 waitlist | 忘了 **Enable form detection**；開啟後到 Deploys 按 **Trigger deploy** |
| 資料送不到 | 用的是 `file:///` 而不是 netlify.app 網址 |
| 手機沒更新 | 等 30 秒、往下拉重新整理或用無痕視窗；Deploys 顯示 Failed 時看疑難排解手冊 Q11–Q13 |
| 歡迎畫面沒出現 | F12 → Console 看紅字，貼給 Copilot；見疑難排解手冊 Q17–Q18 |

完整問題清單：[疑難排解手冊](../../../docs/tutorials/error_guide.md)。

## 提醒學生的兩句話

- 同學互填只能證明表單能用，不能代表市場需求。
- 名單是別人的個人資料：告知用途、只收必要資料、不外流、截圖時遮住個資。
