# 第 1 週投影片大綱（2026/10/7）

> 沒有另外製作投影片；上課以講義 [../README.md](../README.md) 為主，搭配四支互動網頁與 VS Code 現場示範。
> 互動網頁都是單一 HTML 檔，**瀏覽器直接開、不需要網路**，投影也不怕教室網路塞車。
> 架構圖的完整版（Mermaid，GitHub 上直接顯示）在 [../social_media_architecture.md](../social_media_architecture.md)。

## 互動教材

| 檔案 | 用在 | 操作 |
| --- | --- | --- |
| [social_saas.html](social_saas.html) | 段落 1.2、1.4 | ①架構圖（點方塊看說明、「🔍 對照我們的 MVP」開關）②按下去發生什麼事（❤️按讚／📸發限動／📰滑動態／💬傳訊息，逐步或自動播放）③商業模式與小測驗 |
| [foodcourt.html](foodcourt.html) | 段落 1.3–1.5 | ①深山 vs 美食街（月數拉桿）②組裝樂高積木（▶ 播放資料流、←→ 逐步）③小測驗 |
| [git_flow.html](git_flow.html) | 段落 2.1 | ①Git 模擬器（Copilot 修改 → Stage → Commit → Sync → Netlify 更新；Pull；回到存檔點）②對照 VS Code 原始檔控制畫面（7 個編號說明）③小測驗 |
| [prompt_builder.html](prompt_builder.html) | 段落 3.3 | 填表產生咒語；AI 選 GitHub Copilot；🎲 隨機範例；咒語健康度；📋 一鍵複製 |

## 課前 10 分鐘

- 助教在門口協助還沒裝好 VS Code／Git／Copilot 的同學（[before_class.md](../../../docs/tutorials/before_class.md)）
- 投影機先開好 VS Code（字體放大：設定 → `editor.fontSize` 20 以上；`window.zoomLevel` 1～2）

## 段落 0：🎬 開場魔術（5 分鐘）

1. **不講理論，直接示範**：在 VS Code 對 Copilot 說「幫我做一個三峽美食地圖的網站」→ Keep → Commit → Sync → Netlify 自動部署
   （事先建好 repo 並接好 Netlify，現場只示範「說一句話 → 按兩個按鈕 → 網站更新」）
2. 把網址做成 QR Code，全班用手機掃
3. 請同學在學習單第 1 題**預測**：10 年前做這個要多少錢、多少時間？（ARCS：引起注意；POE：預測）

## 段落 1：🧠 觀念建立（30 分鐘）

4. **舉手調查**：誰每天打開 IG／LINE？誰有訂閱 Netflix／Spotify／ChatGPT？→ 帶出 SaaS
5. **買斷 vs SaaS** 對照表 →「程式寫一次，放在雲端，可以租給全世界」
6. 〔切到 social_saas.html ①〕**社群媒體架構圖**：由上往下講一次六層；點 CDN、推薦 AI、推播三個方塊
7. 〔social_saas.html ②〕**播放「❤️ 在 IG 按讚」**：問全班「你看到愛心變紅之後，還有幾個服務在工作？」→ 訊息佇列、推播
8. 金句：「連 IG 都在用別人的 SaaS 積木，推播一定要經過 Apple 和 Google。沒有公司什麼都自己做。」
9. 〔social_saas.html ③〕**免費的社群怎麼賺錢**：「如果你沒有付錢，你就是商品」→ 為什麼推薦演算法讓你停不下來（連結學生生活經驗，ARCS：相關）
10. 轉折：「社群巨頭有幾萬名工程師。我們只有自己＋隊友＋Copilot，怎麼辦？」
11. 〔切到 foodcourt.html ①〕**深山 vs 美食街**：拉桿拉到 3 個月、6 個月
12. 〔foodcourt.html ②〕**四塊積木**＋〔回到 social_saas.html 打開「對照我們的 MVP」〕→ 幾十種服務 vs 4 塊積木
13. 金句：「我們完全不碰複雜的 GCP，因為聰明的現代創業者，是用 SaaS 服務來打造自己的 SaaS 產品！」
14. 〔小測驗〕全班用手機作答（提取練習）

## 段落 2：🗄️ GitHub（20 分鐘）

15. 〔切到 git_flow.html ①〕**Git 模擬器**：老師操作一輪，強調「Commit 只在你電腦；Sync 才送到 GitHub」
16. 〔git_flow.html ②〕**對照 VS Code 畫面**：7 個編號，等一下實際會用到
17. **我做**：投影建 repo（Public、Add README）→ VS Code Clone from GitHub
18. **你做**：同學照 [steps.md](../steps.md) 段落 2；巡堂重點：授權視窗、選對資料夾、按「開啟」
19. 🏗️ 架構呼應：「你在總部開了保險箱，並在自己的工作台放了一份副本」

## 段落 3：🎨 Copilot Vibe Coding（35 分鐘）

20. **Vibe Coding 是什麼**：Karpathy 2025 年提出；你是導演，Copilot 是演員
21. **選題**：學院點子表；強調「選你在乎的」（SDT：自主）
22. **我做**：老師完整示範一次「三峽租屋雷達」：咒語產生器 → Copilot Agent → Keep → Show Preview（範例效應）
23. **我們做**：〔切到 prompt_builder.html〕AI 選 Copilot，健康度 100% 再複製
24. **你做**：自由修改；示範好的修改咒語（具體、合併多個需求、用 `#index.html`）
25. ⚠️ 提醒：Copilot 要求執行指令時按 Skip；免費版次數省著用
26. 🏗️ 架構呼應：「你們現在做出來的，就是 SaaS 架構中的前端，對應 IG 的 App 畫面」

## 段落 4：🏪 存檔上線（25 分鐘）

27. **我做**：投影 Commit（寫好訊息）→ Sync → GitHub 網頁看到檔案 → Netlify Import → Deploy
28. **你做**：同學照 [steps.md](../steps.md) 段落 4；助教巡紅色便利貼
29. **巡堂重點**：user.name/email 未設定、只 Commit 沒 Sync、檔名 `index.html`、Build 設定留空
30. 第一個成功的同學 → 請他當「小助教」幫隔壁（同儕教學）
31. 🏗️ 架構呼應：「沒有碰任何一台實體伺服器，就把網站推向全世界；Netlify 背後的 CDN 跟 IG 是同一種技術！」
32. 隨機挑 2～3 位同學的網址投影，全班鼓掌 👏（ARCS：滿足感）

## 段落 5：🎉 收尾（5 分鐘）

33. 作品巡禮：「我喜歡／我希望／如果」
34. 出場券：回頭看段落 0 的預測（POE：解釋）
35. 預告下週：「如果客人按下『註冊』，資料去哪了？」（留下懸念）
