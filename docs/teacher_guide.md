# 👩‍🏫 教師備課指南

> 給授課老師與助教：課前檢查、課堂動力經營、常見卡關點與評量建議。學生可略過本頁。
> 每週的逐段時間分配與台詞在各週的 `slides/outline.md`；設計背後的理論在 [learning_design.md](learning_design.md)。

[← 回課程首頁](../README.md)

---

## 🎯 教學核心理念

> **先教 Why（為什麼要這樣做），再教 How（怎麼做）。**
> 對零背景的同學，**「我做得到」的感受比「我學到多少技術」更重要**，它決定了他們下課後會不會繼續。

每個實作完成時，都要回到「美食街比喻」做一次 **🏗️ 架構呼應**，讓學生知道自己剛剛組裝了哪一塊積木。

## 📅 課前一週檢查清單

- [ ] 在課程群組貼 [第 1 週課前公告](../lectures/wk01_1007_saas-storefront/announcement.md)（上課前 3 天＋當天早上）。
- [ ] 老師自己用**全新帳號**從頭走一遍 [第 1 週步驟卡](../lectures/wk01_1007_saas-storefront/steps.md) 與 [第 2 週步驟卡](../lectures/wk02_1014_baas-cicd/steps.md)，確認 GitHub／Netlify 介面沒有大改版；若有，更新 [部署教學](tutorials/github_netlify_deploy.md) 的按鈕名稱。
- [ ] 把 [samples/HIGH](../samples/HIGH/index.html) 部署成老師的 Demo 網站（Netlify Base directory 設 `samples/HIGH`），並**開啟 Form detection**，第 2 週現場展示後台名單。
- [ ] 在投影電腦上先打開三支互動教材，確認能正常顯示：[foodcourt.html](../lectures/wk01_1007_saas-storefront/slides/foodcourt.html)、[prompt_builder.html](../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html)、[data_flow.html](../lectures/wk02_1014_baas-cicd/slides/data_flow.html)。
- [ ] 確認教室 Wi-Fi 能連上 github.com、app.netlify.com、AI 助理網站。
- [ ] 準備**紅色、綠色便利貼**（每人各 2 張）。
- [ ] 準備「救援用」的 `index.html`（可直接用 [samples/MEDIUM](../samples/MEDIUM/index.html)），給 AI 帳號出問題的學生使用，**不要讓任何人因為帳號問題卡住整堂課**。
- [ ] 排好兩人一組（建議把「有信心的」和「比較緊張的」同學搭配）。

## 🔥 課堂動力經營（ARCS × SDT 實務）

| 目的 | 做法 | 時機 |
| --- | --- | --- |
| 🎬 **引起注意** | 開場 3 分鐘魔術：一句話 → 網站上線 → 全班掃 QR Code | 第 1 週開場 |
| 💼 **建立相關** | 請學生選「自己在乎」的題目；舉手調查訂閱了哪些 SaaS | 第 1 週段落 1、2 |
| ✅ **建立信心** | 第一個實作是「填表」（咒語產生器），不是寫程式；每段只有一個新概念 | 全程 |
| 🎉 **帶來滿足** | 每次部署成功就隨機挑 2～3 個網站投影、全班鼓掌；第 2 週投影老師後台看到全班名字 | 段落結尾 |
| 🎯 **給予自主** | 題目、AI、風格、支線任務都由學生選 | 全程 |
| 🤝 **建立歸屬** | 駕駛／領航員輪替；作品巡禮；第一個成功的同學當「小助教」 | 全程 |

### 🗣️ 建議的語言（成長型思維）

| 😬 避免說 | 😊 改成說 |
| --- | --- |
| 「這很簡單」 | 「這一步很多人第一次都會卡，我們一起看」 |
| 「你怎麼又錯了」 | 「好，這是很好的經驗值，我們看錯誤訊息在說什麼」 |
| 「你很聰明」 | 「你剛剛換了一種問法問 AI，這個策略很棒」（稱讚策略與努力，不稱讚天分） |
| 「有沒有問題？」（通常沒人回） | 「現在貼紅色便利貼的人，助教馬上過去」 |

## 🟥🟩 紅綠便利貼操作方式

- 每位學生桌上兩張便利貼。**綠色**貼在螢幕上＝「我完成這一步了」；**紅色**＝「我需要幫忙」。
- 助教只要掃視教室，看到紅色就過去，不用等學生舉手（很多零背景學生不敢舉手）。
- 老師看綠色比例決定是否往下：**約 80% 綠色再進下一段**，其餘由助教個別協助。

## ⚠️ 常見卡關點（依發生頻率排序）

1. 檔名變成 `index.html.txt` → 教學生開啟「顯示副檔名」。
2. Netlify Forms 沒開 **Form detection**，或開了沒重新部署（自 2023 年 4 月起預設關閉）。
3. 用 Netlify Drop 部署（沒串 GitHub），第 2 週 CI/CD 無效 → 請學生重新 Import from Git。
4. AI 用 JavaScript 動態產生表單，Netlify 掃描不到 → 請 AI 把 `<form>` 直接寫在 HTML 裡。
5. 在 `file:///` 本機開啟測試表單，資料當然收不到。
6. 第 2 週忘記先把舊的 `index.html` 貼給 AI，AI 重做了一個完全不同的網站。
7. GitHub 2FA 設定卡住 → 課前公告就提醒。

完整排除步驟見 [卡關急救手冊](tutorials/error_guide.md)。

## 🩺 善用 Vibe 健檢站

- [tools/vibe_check.html](../tools/vibe_check.html) 讓學生**自我檢查**，失敗項目會直接給「請跟 AI 說……」的提示，大幅減少助教重複回答。
- 巡堂時可以請學生打開健檢站，一眼看出卡在哪個 Level。
- 想批次檢查全班作業：把學生的 `index.html` 收齊後執行 `python3 tools/ci/vibe_check.py 檔案 --level 3 --json`。

## 📝 評量建議

評分規準與三級示範作品已在 [course_plan.md](course_plan.md#-評分方式) 與 [samples/](../samples/README.md) 公開。建議：

- **冒險護照的反思只看「有沒有真誠填寫」**，不看文筆，降低零背景學生的焦慮。
- **徽章與 XP 當作回饋，不直接換算成績**，也**不公布排行榜**（避免社會比較讓落後的同學放棄；見 [learning_design.md](learning_design.md#5-進度看得見-)）。
- 市場驗證重視「觀察與反思」，不是名單數量比賽。

## 🖼️ 作品牆維護

- 學生透過 [作品牆登記表（Issue）](https://github.com/cychiang-ntpu/VibeNTPU/issues/new?template=showcase.yml) 登記，老師把資料加到 [showcase/README.md](../showcase/README.md) 後關閉 Issue。
- 求救單（Issue）可以由助教回覆，也鼓勵同學互相回答（同儕教學）。

## 🔐 提醒學生的倫理議題

- 收集他人 Email 時要說明用途；發表時截圖要**遮蔽個資**。
- 不要把同學填的名單貼進 AI 對話。
- Demo 用虛構數據沒關係，但正式對外請勿誤導使用者。
- AI 產生的程式碼仍需自己理解與負責，並在冒險護照誠實記錄 AI 使用情形。
