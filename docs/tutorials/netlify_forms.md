# Netlify Forms 步驟教學：設定、測試、查看名單

[回第 2 週手把手實作](../../lectures/wk02_1014_baas-cicd/README.md)

Netlify Forms 是 Netlify 提供的「收表單」服務，屬於 BaaS（後端即服務，別人幫你架好的後端）。你只要在網頁的表單加上 `data-netlify="true"`，再到 Netlify 打開表單偵測，訪客送出的資料就會存進 Netlify 後台。你不需要自己寫伺服器程式，也不需要架資料庫。本頁帶你完成設定、測試、查看名單、收到通知與匯出資料。

想了解原理：見 [表單、儲存與 CI/CD 深入閱讀](../deep_dive/forms_storage_cicd.md)（選讀）。

---

## 步驟 1：確認表單寫對了（約 3 分鐘）

先用 [第 2 週提示詞 1](../../lectures/wk02_1014_baas-cicd/prompts.md) 請 Copilot 加好表單，並按 **保留（Keep）**。

1. 在 VS Code 打開 `index.html`。
2. 按 `Ctrl+F`（Mac：`⌘F`）打開搜尋框。
3. 輸入 `data-netlify`。
4. 再輸入 `form-name`。
5. 再輸入 `method="POST"`。

**完成後你應該看到：** 三個搜尋都找得到。

**如果不一樣：** 有任何一個找不到 → 在 Copilot Chat（Agent 模式）輸入：`請檢查 #index.html 的表單是否符合 Netlify Forms 的規定，並直接修正`。

## 步驟 2：在 Netlify 打開表單偵測（約 3 分鐘）

2023 年 4 月之後新建的網站，這個功能預設是關閉的，每個網站要手動打開一次。

1. 打開 <https://app.netlify.com/> 並登入。
2. 點選你的網站（專案）名稱。
3. 點選左側選單的 **Forms**。
4. 按下 **Enable form detection**。

**完成後你應該看到：** 頁面顯示表單偵測已啟用，並提示下一次部署後生效。

**如果不一樣：** 找不到按鈕 → 點選左側 **Project configuration** → **Forms** → **Form detection** 打開。

## 步驟 3：提交、同步，等部署完成（約 5 分鐘）

1. 點選 VS Code 左側 **原始檔控制（Source Control）** 圖示（形狀像樹枝分岔）。
2. 在訊息欄輸入 `新增早鳥名單表單`。
3. 按下 **提交（Commit）**。
4. 按下 **同步變更（Sync Changes）**。
5. 回到 Netlify，點選左側 **Deploys**。
6. 等最上面一筆變成 **Published**。

**完成後你應該看到：** 最上面一筆顯示 `新增早鳥名單表單` 和 **Published**。

**如果不一樣：** 你是先同步、之後才打開表單偵測 → 在 **Deploys** 頁面按 **Trigger deploy** → **Deploy site** 重新部署一次。

## 步驟 4：測試送出（約 3 分鐘）

1. 用瀏覽器打開你的 `https://…netlify.app` 網址。
2. 填入姓名和 Email，按下送出。

**完成後你應該看到：** 「感謝」或「已送出」的畫面。

**如果不一樣：** 網址開頭是 `file:///` → 你開的是電腦裡的檔案，資料不會送到 Netlify。請改用 netlify.app 網址。

## 步驟 5：查看名單（約 2 分鐘）

1. 在 Netlify 點選左側 **Forms**。
2. 在表單清單中點選 **waitlist**。

**完成後你應該看到：** 每一筆資料的姓名、Email 和送出時間。

**如果不一樣：** 看不到 `waitlist` 或沒有資料 → 見 [疑難排解手冊](error_guide.md) Q14–Q16。有些資料可能被判定為垃圾訊息，可在頁面上切換到 spam 清單查看。

## 步驟 6（選做）：有人填表就寄信給我（約 3 分鐘）

1. 在 Netlify 你的專案頁面，點選左側 **Forms**。
2. 找到 **Submission notifications**（表單通知）區塊，按 **Add notification**。
3. 選擇 **Email notification**。

   **如果找不到：** 舊版介面放在 **Project configuration → Notifications → Emails and webhooks → Form submission notifications**；也可參考 [官方說明](https://docs.netlify.com/manage/forms/notifications/)。
4. **Event to listen for** 選 **New form submission**。
5. 填入你的 Email。
6. **Form** 選 `waitlist`。
7. 按 **Save**。

**完成後你應該看到：** 通知清單多了一筆。之後有人填表，你會收到一封信。

**如果不一樣：** 介面名稱不同 → 參考官方說明 [Netlify Forms notifications](https://docs.netlify.com/manage/forms/notifications/)。

## 步驟 7（選做）：匯出成 Excel 可開的檔案（約 2 分鐘）

1. 在 **Forms** → **waitlist** 頁面，找到 **Download as CSV**（下載 CSV）。
2. 按下後存到電腦。
3. 用 Excel 或 Google 試算表打開。

**完成後你應該看到：** 每一列是一筆報名，每一欄是一個表單欄位。

**如果不一樣：** 找不到下載按鈕 → 參考官方說明 [Netlify Forms submissions](https://docs.netlify.com/manage/forms/submissions/)。

## 收集個資前的提醒

姓名和 Email 是個人資料，受《[個人資料保護法](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021)》規範。請做到：

- [ ] **告知用途**：表單旁寫清楚資料要做什麼（例如「僅用於產品上線通知」）。
- [ ] **只收必要資料**：不要求身分證字號、生日、電話等用不到的欄位。
- [ ] **不外流**：不公開名單、不轉傳，匯出的檔案不放到公開的地方；不再使用時到後台刪除。
- [ ] **截圖遮蔽個資**：放進報告或簡報的截圖，要把姓名和 Email 遮住。

免費方案的送出次數有上限，課堂使用通常足夠；實際額度以 [Netlify 價格頁面](https://www.netlify.com/pricing/) 為準。

---

下一份：[LocalStorage 步驟教學](localstorage.md)
