# 📂 範例完成品

[← 回課程首頁](../README.md)

| 範例 | 對應進度 | 重點 |
| --- | --- | --- |
| [week1-landing/index.html](week1-landing/index.html) | 第一週完成品 | SaaS 形象首頁：導覽列、主視覺、痛點、功能、價格、FAQ、RWD |
| [week2-waitlist/index.html](week2-waitlist/index.html) | 第二週完成品 | 第一週＋早鳥名單表單（Netlify Forms）＋ AJAX 送出＋ LocalStorage 會員儀表板 |

兩個範例都是**單一 `index.html` 檔案**，跟你請 AI 產生的格式一樣，可以直接打開程式碼對照學習（程式碼裡有中文註解）。

## 👀 怎麼看範例？

- **看程式碼**：在 GitHub 上直接點開檔案。
- **看畫面**：把檔案下載到電腦（點開檔案 → 右上角「Download raw file」），雙擊用瀏覽器打開。
  > ⚠️ 第二週的表單在本機（`file:///`）打開時**送出一定會失敗**，因為 Netlify Forms 只在部署到 Netlify 後才有作用。

## 🚀 想把範例部署起來試玩？

1. 下載 `week2-waitlist/index.html`。
2. 照 [第一週部署教學](../week1/deploy-github-netlify.md) 建立一個新 repo，上傳這個 `index.html` 並部署到 Netlify。
3. 照 [Netlify Forms 教學](../week2/netlify-forms.md) 開啟 Form detection 並重新部署。
4. 填寫表單，到 Netlify 後台查看名單。

> 💡 給老師：如果想直接部署**這整個 repo** 的範例，在 Netlify 匯入時把 **Base directory**（或 Publish directory）設為 `examples/week2-waitlist` 即可。
