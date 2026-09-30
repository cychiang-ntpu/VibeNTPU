# 教師備課指南

[← 回課程首頁](../README.md)

本文件供授課教師與助教使用，內容包括課前準備、課堂引導、常見故障點與處理方式、評量流程、倫理與隱私議題，以及作品牆維護。各週逐段時間分配與講述重點見各週的 `slides/outline.md`（[第 1 週](../lectures/wk01_1007_saas-storefront/slides/outline.md)、[第 2 週](../lectures/wk02_1014_baas-cicd/slides/outline.md)）；教學安排的學理依據見 [教學設計理據](learning_design.md)。

---

## 1. 教學核心原則

1. **先說明 Why，再示範 How**。每個實作段落結束時，將剛完成的操作對應回四個架構元件（前端、版本控制、雲端託管、BaaS），讓學生知道自己組裝了哪一部分。
2. **環境問題不應占用學習時間**。非學習性障礙（帳號、額度、公用電腦設定）應盡可能在課前排除，並準備備援方案。
3. **以證據確認進度**。依 [學習檢核點](checkpoints.md) 所列證據確認學生進度，而非僅詢問「大家都完成了嗎」。
4. **示範錯誤與除錯**。示範時不必刻意避開錯誤；公開處理錯誤能降低學生對失敗的焦慮。

## 2. 課前準備清單

### 2.1 課前兩週

- [ ] 於課程群組提醒學生申請 [GitHub Education](https://education.github.com/)。審核通常需要數日，且需上傳在學證明；通過後可免費使用 Copilot 的學生方案。未通過者仍可使用 Copilot Free，但每月有用量上限。
- [ ] 確認教室網路可連線至 `github.com`、`app.netlify.com`、VS Code 延伸模組市集與 GitHub Copilot 服務；最好於教室實際以 Copilot Chat 送出一次請求測試。
- [ ] 若使用電腦教室：確認已安裝 VS Code 與 Git；確認是否有開機還原。若有，每次上課學生都須重新登入 GitHub、重新授權 Copilot 並設定 `git config`，應預留時間或改請學生攜帶個人筆電。

### 2.2 課前一週

- [ ] 張貼 [第 1 週課前公告](../lectures/wk01_1007_saas-storefront/announcement.md)（課前 3 天與當天早上各一次）。
- [ ] 教師以**全新帳號**從頭操作 [課前準備](tutorials/before_class.md)、[第 1 週步驟卡](../lectures/wk01_1007_saas-storefront/steps.md) 與 [第 2 週步驟卡](../lectures/wk02_1014_baas-cicd/steps.md)，確認 GitHub、Netlify、VS Code 介面未改版；若有改版，更新 [部署教學](tutorials/github_netlify_deploy.md) 中的按鈕名稱與截圖描述。
- [ ] 準備示範 repo，並**事先連接 Netlify**，確認推送後能自動部署（第 1 週開場示範使用）。
- [ ] 將 [samples/HIGH](../samples/HIGH/index.html) 部署為教師 Demo 網站（Netlify 的 Base directory 設為 `samples/HIGH`），**開啟 Form detection** 並重新部署，第 2 週用於展示後台收件。
- [ ] 準備備援用 `index.html`（可使用 [samples/MEDIUM](../samples/MEDIUM/index.html)），提供給 Copilot 帳號或額度出問題的學生，避免任何人因帳號問題停滯整堂課。
- [ ] 規劃 Copilot 無法使用時的替代流程：以網頁版 AI 產生程式碼，手動貼入 VS Code 存檔（見 [第 1 週提示詞](../lectures/wk01_1007_saas-storefront/prompts.md)）。
- [ ] 預先分組，建議將較有信心與較緊張的學生搭配。
- [ ] 準備紅、綠兩色便利貼（每人各 2 張），作為課堂即時回饋卡。

### 2.3 上課當天

- [ ] 投影電腦的 VS Code 放大字級：`editor.fontSize` 設為 20 以上，`window.zoomLevel` 設為 1–2；終端機字級一併調整。確認教室後排可讀。
- [ ] 於投影電腦開啟互動教材並確認可正常顯示：[social_saas.html](../lectures/wk01_1007_saas-storefront/slides/social_saas.html)、[foodcourt.html](../lectures/wk01_1007_saas-storefront/slides/foodcourt.html)、[prompt_builder.html](../lectures/wk01_1007_saas-storefront/slides/prompt_builder.html)、[git_flow.html](../lectures/wk01_1007_saas-storefront/slides/git_flow.html)、[data_flow.html](../lectures/wk02_1014_baas-cicd/slides/data_flow.html)。這些檔案不需網路即可開啟。
- [ ] 關閉投影電腦上的通知與含個資的分頁。
- [ ] 確認示範 repo 的 Copilot 額度尚有餘裕。

## 3. 課堂引導

### 3.1 動機經營

| 目的 | 做法 | 時機 |
| --- | --- | --- |
| 引起注意 | 開場 3 分鐘：以一段提示詞產生網站並推送，Netlify 自動部署後全班以手機掃描 QR Code 開啟 | 第 1 週開場 |
| 建立相關 | 請學生列舉自己使用的 SaaS；選擇與自己生活或學院相關的題目 | 第 1 週前段 |
| 建立信心 | 第一個實作採提示詞產生器的結構化填寫；每段只引入一個新概念 | 全程 |
| 帶來滿足 | 部署成功後隨機投影 2–3 個學生網站；第 2 週投影教師後台，呈現全班送出的資料（遮蔽個資） | 段落結束 |
| 支持自主 | 題目、風格、延伸任務由學生選擇 | 全程 |
| 建立連結 | 配對程式設計角色輪替；作品巡禮；請先完成的學生協助同儕 | 全程 |

### 3.2 課堂即時回饋卡

- 學生完成當前步驟時於螢幕上緣貼綠色；需要協助時貼紅色。
- 助教巡視時優先處理紅色，無需等待學生舉手；許多初學者不願在全班面前提問。
- 教師觀察綠色比例決定進度：約八成為綠色時進入下一段，其餘由助教個別協助。

### 3.3 配對程式設計

- 駕駛（driver）操作電腦；導航員（navigator）對照步驟卡、閱讀 Copilot 的回覆並提醒下一步。
- 每個實作段落交換一次角色。兩人皆須完成各自的 repo 與部署。
- 若發現某組長時間由同一人操作，提醒交換。

### 3.4 回饋用語

回饋應聚焦於策略與過程，避免評價能力或天分：

| 避免 | 建議改為 |
| --- | --- |
| 「這很簡單。」 | 「這一步很多人第一次操作時都會遇到問題，我們一起看。」 |
| 「怎麼又錯了？」 | 「我們先看錯誤訊息說了什麼。」 |
| 「你很聰明。」 | 「你剛才改變了描述需求的方式，所以 Copilot 的輸出更接近目標。」 |
| 「有沒有問題？」 | 「目前貼紅色卡的組別，助教會依序過去。」 |

### 3.5 形成性評量活動

- **預測—觀察—解釋（POE）**：例如在示範前請學生預測「只按 Commit、不按 Sync，網站會更新嗎？」，再實際觀察並解釋。
- **快速檢核題**：段落轉換前以一題選擇題確認關鍵概念。
- **出場券**：下課前請學生寫出本週最重要的一個概念與一個仍不理解之處，作為下週開場補充依據。

## 4. 常見故障點與處理

依經驗發生頻率排序。完整排除步驟見 [疑難排解手冊](tutorials/error_guide.md)。

| 症狀 | 原因 | 處理方式 |
| --- | --- | --- |
| Commit 時出現要求設定 `user.name`／`user.email` 的訊息 | 首次使用 Git，尚未設定身分 | 於 VS Code 終端機執行 `git config --global user.name "姓名"` 與 `git config --global user.email "GitHub Email"` |
| 學生反映「網站沒有更新」 | 只按了 Commit，未按 Sync | 說明 Commit 僅存於本機，Sync 才會推送至 GitHub；檢查 GitHub 上是否有該 commit |
| Copilot 只回答文字，沒有修改檔案 | Copilot Chat 處於 Ask 模式 | 切換為 Agent 模式 |
| 原始檔控制面板沒有 Sync 按鈕或顯示「初始化存放庫」 | VS Code 開啟的資料夾不是 clone 下來的 repo | 以「檔案 → 開啟資料夾」重新開啟正確的 repo 資料夾 |
| Copilot 要求執行終端機指令 | Agent 模式嘗試安裝套件或啟動伺服器 | 本課程為單一 HTML 檔案，請學生選擇略過（Skip） |
| Copilot 提示額度用盡 | Copilot Free 每月用量上限 | 改用備援 `index.html` 或網頁版 AI 替代流程；提醒申請 GitHub Education |
| Netlify Forms 後台看不到資料 | 未開啟 Form detection，或開啟後未重新部署（Netlify 目前預設關閉此功能） | 於 Netlify 後台開啟 Form detection，並觸發一次重新部署 |
| 第 2 週推送後網站未自動更新 | 第 1 週以 Netlify Drop 拖曳部署，未連接 GitHub | 以 Import from Git 重新建立網站 |
| 表單送出後 Netlify 收不到 | AI 以 JavaScript 動態產生 `<form>`，Netlify 部署時掃描不到 | 請 Copilot 將 `<form>` 直接寫在 HTML 中 |
| 表單送出失敗 | 以 `file:///` 在本機開啟測試 | 必須在部署後的 `https://*.netlify.app` 網址上測試 |
| Copilot 另建新檔而非修改 `index.html` | 提示詞未指定目標檔案 | 在提示詞中以 `#index.html` 指定檔案，或先開啟該檔案再下指令 |
| GitHub 登入卡在雙重驗證（2FA） | 未事先設定驗證器或備援碼 | 課前公告即提醒完成 2FA 設定；現場先使用備援 `index.html` 進行後續步驟 |

## 5. 評量流程

評分規準與示範作品已公開於 [course_plan.md](course_plan.md#4-分析式評分規準) 與 [samples/](../samples/README.md)。

### 5.1 收集證據

1. 請學生於作業系統或表單繳交：GitHub repo 網址、Netlify 網址、學習歷程檔案（即 repo 的 `README.md`）。
2. 由 repo 網址檢視 Commits 頁面，確認 commit 次數、訊息品質與 CI/CD 更新紀錄（檢核點 6）。
3. Netlify 後台截圖須遮蔽個資；教師不需要取得學生後台的存取權限。

### 5.2 批次自我檢核

將學生的 `index.html` 下載至同一資料夾（建議以學號命名），以命令列版本批次檢查：

```bash
python3 tools/ci/vibe_check.py FILE --level 3 --json
```

批次處理範例：

```bash
for f in submissions/*.html; do
  python3 tools/ci/vibe_check.py "$f" --level 3 --json > "reports/$(basename "$f" .html).json"
done
```

JSON 輸出包含每一項檢查的 `id`、`level`、`kind`（必要、建議、加分）與 `pass`，可彙整為試算表。結束代碼為 0 表示指定等級以內的必要項目全部通過，1 表示有未通過項目，2 表示讀檔失敗。

**限制**：此工具為靜態分析，只能確認 HTML 中是否包含必要元素，不能確認網站已部署或表單已收件，亦無法評估內容品質。它是評分的輔助證據，不能取代依規準的人工評閱。

### 5.3 評分原則

- 反思不評文筆，而評是否具體：能指出具體事件、錯誤與解決過程即可取得滿分。
- 檢核點用於回饋，不直接換算成績，也不公布排名（理由見 [教學設計理據](learning_design.md#53-外在獎勵的風險為何移除點數等級與徽章)）。
- 市場驗證評的是方法與觀察品質，不以名單數量比較。
- 對 AI 使用的評量重點是揭露與驗證，而非是否使用。

## 6. 倫理與隱私

| 議題 | 課堂上的要求 | 說明重點 |
| --- | --- | --- |
| 個人資料蒐集 | 表單附近說明資料用途；只收集必要欄位 | 《個人資料保護法》的告知義務與目的限制概念 |
| 截圖與投影 | 後台截圖遮蔽 Email、姓名；投影前關閉含個資的分頁 | 課堂投影亦屬公開揭露 |
| AI 與個資 | 不得將同學填寫的資料貼入 AI 對話 | 輸入 AI 服務的內容可能被保存或用於改進服務，應依各服務條款判斷 |
| 憑證安全 | 不得將密碼、token 寫入程式碼或提交至 GitHub | 公開 repo 的內容任何人皆可讀取，且 Git 歷史會保留已刪除的內容 |
| LocalStorage | 不存放密碼或敏感資料 | 任何在該頁面執行的腳本都能讀取 LocalStorage |
| 誠實呈現 | Demo 虛構資料須標示；驗證數據須真實 | 誤導性的數據違反學術誠信，也違反對使用者的承諾 |
| AI 產出責任 | 學生須能說明 AI 產生的程式碼，並於學習歷程檔案揭露使用情形 | 見 [AI 使用規範](course_plan.md#5-ai-使用規範) |

## 7. 作品牆與 Issue 維護

- 學生透過 [作品牆登記表](https://github.com/cychiang-ntpu/VibeNTPU/issues/new?template=showcase.yml) 登記；教師確認網址可開啟、內容無不當資訊與個資後，將資料加入 [showcase/README.md](../showcase/README.md)，再關閉 Issue。
- 求助單使用 `求助` 標籤，作品牆登記使用 `作品牆` 標籤；請於 repo 的 Labels 頁面事先建立，Issue 表單才能自動套用。
- 求助單可由助教回覆，也鼓勵已完成的同學回答；問題解決後請提問者說明解法再關閉，以累積可搜尋的紀錄。
- 學期結束後檢查作品牆連結是否仍有效，已失效者標註或移除；若學生要求下架，應立即處理。

## 8. 課後檢討

建議每週課後記錄：各檢核點的完成比例、最常出現的故障、出場券中最常見的誤解、需更新的教材位置。這些資料可作為下一次開課調整教材的依據。
