# GitHub 與 Netlify 部署

> **對應檢核點**：檢核點 3（提交並同步到 GitHub、Netlify 部署成功、網站自我檢核工具 Level 1 通過）
> **預估時間**：約 20 分鐘
> **做完你會得到**：一個 `https://你的名稱.netlify.app` 網址，任何人用手機或電腦都能打開你的網站。

[← 回第 1 週](../../lectures/wk01_1007_saas-storefront/README.md)　｜　[教學目錄](README.md)

---

## 先懂一件事

**部署（deploy）** ＝把你電腦上的網頁放到網路上，讓別人也能打開。你在 VS Code 預覽時，只有你自己看得到；部署到 Netlify 之後，網址可以分享給任何人。Netlify 會從你的 GitHub repo 讀取檔案，所以要先把檔案同步到 GitHub。

介面可能改版，按鈕名稱若與本文略有不同，請找意思相近的按鈕，或參考 [Netlify 官方說明](https://docs.netlify.com/start/quickstarts/deploy-from-repository/)。

想了解原理（授權、webhook、CDN、HTTPS、發布目錄）：見 [Git、Copilot 與部署機制（選讀）](../deep_dive/git_and_copilot.md)。

---

## 步驟 1：確認 index.html 已經在 GitHub 上（約 2 分鐘）

1. 打開瀏覽器，前往你的 repo 頁面（`github.com/你的帳號/rent-radar`）。
2. 看檔案清單。

**完成後你應該看到：** 清單最外層（不是在某個資料夾裡面）有一個 `index.html`，檔名全部是小寫。

**如果不一樣：** 沒有 `index.html` → 回到 [Git 與 GitHub 入門](git_intro.md) 完成步驟 4 提交與步驟 5 同步變更。檔名是 `Index.html` 或放在資料夾裡 → 在 VS Code 改名或移到最外層，再提交、同步變更。

---

## 步驟 2：在 Netlify 匯入 GitHub 專案（約 5 分鐘）

這一步讓 Netlify 連上你的 GitHub repo。

1. 前往 <https://app.netlify.com/>，按 **Log in with GitHub** 登入。
2. 在 **Projects** 頁面，按 **Add new project**（舊版介面為 **Add new site**）。
3. 在選單中點選 **Import an existing project**。
4. 按 **GitHub** 按鈕。
5. 若跳出 GitHub 授權視窗，按 **Authorize Netlify**。
6. 若要求安裝 Netlify App，選擇 **Only select repositories**，在下拉選單中勾選 `rent-radar`，按 **Install**（或 **Save**）。
7. 回到 Netlify 的 repo 清單，點選 `rent-radar`。

**完成後你應該看到：** 進入一個設定頁面，上方寫著你的 repo 名稱，下方有 **Project name**、**Branch to deploy** 等欄位。

**如果不一樣：** 清單中沒有你的 repo → 按清單下方的 **Configure the Netlify app on GitHub**，把 repo 加入後回來重新整理（見 [疑難排解手冊](error_guide.md) Q12）。

---

## 步驟 3：設定名稱並部署（約 3 分鐘）

1. 在 **Project name** 欄位輸入網址要用的名稱，例如 `ntpu-rent-radar`（只能用英文小寫、數字和 `-`）。
2. 其他欄位**全部不要改**，保持預設或空白：

   | 欄位 | 應該是 |
   | --- | --- |
   | Branch to deploy | `main` |
   | Base directory | 空白 |
   | Build command | 空白 |
   | Publish directory | 空白 |

3. 按頁面最下方的 **Deploy**（按鈕可能寫成 **Deploy rent-radar**）。
4. 等待 10–30 秒。

**完成後你應該看到：** 頁面上方出現綠色的網址，例如 `https://ntpu-rent-radar.netlify.app`，部署狀態顯示 **Published**。

**如果不一樣：**

- 顯示名稱已被使用 → 加上學號末三碼，例如 `ntpu-rent-radar-123`。
- 部署狀態是 **Failed** → 確認 Build command 與 Publish directory 是空白（見下方問題排除表）。

---

## 步驟 4：修改網址名稱（只有在步驟 3 沒設定名稱時才需要）（約 2 分鐘）

沒設定名稱時，Netlify 會給一個隨機網址，例如 `https://jolly-pony-123abc.netlify.app`。

1. 在 Netlify 左側選單點選 **Project configuration**。
2. 點選 **General** → **Project details**。
3. 按 **Change project name**（或 **Manage project name and cover image**）。
4. 輸入新名稱，例如 `ntpu-rent-radar`，按 **Save**。

**完成後你應該看到：** 網址變成 `https://ntpu-rent-radar.netlify.app`。

**如果不一樣：** 改名後舊網址會失效，記得更新你分享過的連結。參考：[Netlify：變更專案名稱](https://docs.netlify.com/manage/projects/customize-project-name-and-cover-image/)。

---

## 步驟 5：用手機確認網站（約 5 分鐘）

1. 在電腦上點 Netlify 顯示的網址，確認網站能打開。
2. 看瀏覽器網址列，確認開頭是 `https://`（有鎖頭圖示）。
3. 用手機瀏覽器輸入同一個網址（或用手機掃描、傳訊息給自己）。
4. 在手機上確認文字沒有太小、沒有被切掉、不需要左右滑動。
5. 用 [網站自我檢核工具](../../tools/vibe_check.html) 做 Level 1 檢核。
6. 把網址分享到課程群組。

**完成後你應該看到：** 手機和電腦都能正常打開你的網站，網站自我檢核工具 Level 1 通過。

**如果不一樣：** 手機上排版跑掉 → 請 Copilot：「請讓這個網頁在手機寬度下正常顯示，並確認有 viewport 設定。」修改後提交、同步變更，等 1 分鐘再重新整理手機。

**這一步在架構中的位置：** 你的網站已經上線，也就是課程架構中的「部署」。從現在起，每次在 VS Code 提交並同步變更，Netlify 都會在約 1 分鐘內自動更新網站（詳見 [CI/CD 教學](cicd.md)）。

---

## 問題排除

| 你看到的狀況 | 怎麼做 |
| --- | --- |
| 網站顯示 `Page not found` | 確認 GitHub 上最外層有全小寫的 `index.html`；確認 Netlify 的 Publish directory 是空白（[疑難排解手冊](error_guide.md) Q11） |
| Netlify 清單中找不到 repo | 按 **Configure the Netlify app on GitHub** 把 repo 加入（Q12） |
| GitHub 已更新，網站沒變 | 確認已按同步變更；到 Netlify 的 **Deploys** 看最新一筆；用無痕視窗重新開啟（Q13） |
| 部署狀態 Failed | 點開失敗的那一筆看最後幾行紀錄；把 Build command 與 Publish directory 清空，按 **Trigger deploy** 重新部署 |
| 中文變亂碼 | 請 Copilot 確認 `<head>` 中有 `<meta charset="UTF-8">`，再提交、同步變更 |
| 圖片在電腦上看得到、網站上看不到 | 確認圖片已提交並出現在 GitHub；檔名大小寫要完全一致 |

**註：** Netlify 也有 [Netlify Drop](https://app.netlify.com/drop) 可以直接拖曳資料夾上線，但它沒有連接 GitHub，不會自動更新。課堂作業請用本篇的 GitHub 匯入方式。

---

## 完成檢查

- [ ] GitHub repo 最外層有 `index.html`
- [ ] Netlify 部署狀態為 **Published**
- [ ] 網址是我設定的名稱，開頭是 `https://`
- [ ] 手機上可以正常開啟與閱讀
- [ ] 網站自我檢核工具 Level 1 通過

完成後請回到 [第 1 週步驟卡](../../lectures/wk01_1007_saas-storefront/steps.md)。
