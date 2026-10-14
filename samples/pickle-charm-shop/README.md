# Pickle Charm Shop 參考實作

這個資料夾是第 2 週實作指南中兩段提示詞的「參考結果」：

- 提示詞 1：註冊／登入對話框，表單以 Netlify Forms（`name="signup"`）收件，登入狀態存在 localStorage 的 `pickleUser`。
- 提示詞 2：可下訂單的購物車，內容存在 localStorage 的 `pickleCart`，訂單以 Netlify Forms（`name="order"`）收件。

提示詞全文見 `lectures/wk02_1014_baas-cicd/pickle_charm_prompts.md`。老師可以用這份程式碼示範預期的畫面與行為；同學的版本不必和它一模一樣，但應符合提示詞中的每一項要求。

## 檔案

- `index.html`：頁面內容，兩個表單都直接寫在 HTML 裡（Netlify 部署時才掃得到）。
- `script.js`：登入狀態、購物車、以 `fetch()` 送出表單的邏輯。
- `styles.css`：原本的版面樣式，加上對話框與購物車面板。

## 如何部署

1. 把這三個檔案放進自己的 GitHub 儲存庫（或 fork 課程儲存庫後只取這個資料夾）。
2. 到 Netlify 新增站台，選擇該儲存庫；不需要 build 指令，publish directory 設為放這三個檔案的資料夾。
3. 在 Netlify 站台設定中開啟 **Forms → Enable form detection**，然後重新部署一次。
4. 用 `*.netlify.app` 網址測試：送出註冊與訂單後，Netlify 後台的 Forms 應看得到 `signup` 與 `order` 兩個表單的資料。

本機直接開 `index.html` 時，`fetch("/")` 不會有伺服器回應，送出會顯示失敗訊息，這是正常的；要看到成功流程請部署到 Netlify。

## 注意

- 「登入」只是模擬：任何姓名與 Email 送出後就視為登入，資料只存在瀏覽器的 localStorage，沒有密碼也沒有驗證。
- 沒有金流：送出訂單只是把資料送進 Netlify Forms，不會收款。
