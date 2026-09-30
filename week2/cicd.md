# 🔄 體驗 CI/CD：上傳即上線的魔法

[← 回第二週](README.md)

---

## 🧠 什麼是 CI/CD？

- **CI（Continuous Integration，持續整合）**：每次修改程式，都自動合併、自動檢查有沒有壞掉。
- **CD（Continuous Deployment，持續部署）**：檢查通過後，自動把新版本送上線給使用者。

**美食街比喻**：總部（GitHub）的裝潢設計圖一改，自動傳真機就立刻傳給所有分店（Netlify），分店當天就換好新裝潢，**完全不用關店**。

```mermaid
flowchart LR
    A["🤖 AI 修改程式碼"] --> B["💻 你上傳到 GitHub<br/>(Commit)"]
    B -- "GitHub 自動通知" --> C["☁️ Netlify 自動部署"]
    C --> D["📱 全世界用戶<br/>重新整理就看到新版"]
```

> 你上週在 Netlify 按下「Import from Git」的那一刻，就已經把這條自動化生產線接好了！

📖 延伸閱讀：[Red Hat：什麼是 CI/CD？（繁中）](https://www.redhat.com/zh-tw/topics/devops/what-is-ci-cd)｜[GitHub：CI/CD 解說](https://github.com/resources/articles/devops/ci-cd)｜[Netlify：持續部署](https://docs.netlify.com/deploy/create-deploys/#deploy-with-git)

---

## 🪄 動手體驗（10 分鐘）

### 1. 先用手機打開你的網站
記住現在的樣子（例如按鈕的顏色、標題的文字）。

### 2. 請 AI 做一個「明顯」的修改
使用 [咒語 3](prompts.md#咒語-3快速改版體驗-cicd)，例如把按鈕改成亮橘色。存成 `index.html`。

### 3. 上傳到 GitHub 覆蓋舊檔案
1. 到你的 GitHub repo → **Add file** → **Upload files**。
2. 拖曳新的 `index.html`（同檔名會自動覆蓋）。
3. Commit 說明寫 `改按鈕顏色`，按 **Commit changes**。

### 4. 什麼都不要做，直接看手機！
- **不用進 Netlify 點任何按鈕**。
- 等 10～30 秒，用手機**重新整理**網頁。
- 🎉 網頁已經自動更新了！

> 💡 想看幕後發生什麼事？打開 Netlify → 你的專案 → **Deploys**，會看到一筆新的部署紀錄，旁邊寫著你剛剛的 Commit 說明。

> 📱 手機沒更新？可能是瀏覽器快取，試試「下拉重新整理」，或用無痕模式開啟。

---

## ⏪ 加碼：時光機功能（改壞了怎麼辦？）

CI/CD 搭配版本控制，還有一個超強的保險：**隨時可以回到上一版**。

- **在 Netlify 回復**：Deploys 頁面 → 點選之前某一筆成功的部署 → **Publish deploy**，網站立刻變回那個版本。
  📖 [Netlify：Rollbacks](https://docs.netlify.com/deploy/manage-deploys/manage-deploys-overview/#rollbacks)
- **在 GitHub 查看歷史**：repo 頁面點 **Commits**（時鐘圖示），可以看到每一次修改的內容。
  📖 [GitHub：檢視 Commit 歷史](https://docs.github.com/zh/pull-requests/committing-changes-to-your-project/viewing-and-comparing-commits/differences-between-commit-views)

---

## 🏗️ 架構呼應

> 這叫做 **CI/CD 自動化部署**！這就是為什麼 IG、Netflix 每天都在更新，你卻不會遇到「維修中」。
> 只要架構對了（GitHub 串 Netlify），老闆一句話，AI 寫出 Code，上傳後幾十秒內全世界的用戶都會看到更新！
> **這就是科技公司的敏捷開發（Agile）！**

📖 延伸閱讀：[敏捷軟體開發宣言（繁中）](https://agilemanifesto.org/iso/zhcht/manifesto.html)｜[Atlassian：什麼是敏捷開發？](https://www.atlassian.com/agile)

---

完成了！準備你的 MVP 發表 👉 [期末 Pitch 模板](../docs/pitch-template.md)
