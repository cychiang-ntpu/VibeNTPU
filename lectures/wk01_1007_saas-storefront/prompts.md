# 🪄 第 1 週 Copilot 咒語集：詠唱你的 SaaS 產品前端

> 使用方式：
> 1. VS Code 左側打開**你 clone 下來的 repo 資料夾**。
> 2. 打開 Copilot Chat（`Ctrl+Alt+I`／`⌃⌘I`，或點上方 Copilot 圖示）。
> 3. 選模式：要 Copilot **改檔案**選 **Agent**；只想**問問題**選 **Ask**。
> 4. 複製咒語 → 把 `【】` 裡的內容換成你自己的 → 送出 → 看完變更按 **Keep**。
>
> 懶得改【】？用 👉 [咒語產生器](slides/prompt_builder.html)，填表就好。

[← 回第 1 週](README.md)

---

## 💡 好咒語的四個秘訣

1. **給角色**：「你是一位資深前端工程師」→ AI 會用更專業的標準做事。
2. **給情境**：說清楚你的產品是什麼、給誰用、想要什麼感覺。
3. **給限制**：「只要一個檔案」、「不要用外部圖片」→ 避免 AI 產生你無法處理的東西。
4. **指定檔案**：用 `#index.html` 告訴 Copilot 要看、要改哪個檔案。

📖 延伸閱讀：[VS Code：Copilot 提示詞技巧](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting)｜[GitHub：Copilot 提示工程](https://docs.github.com/zh/copilot/concepts/prompting/prompt-engineering)｜[Anthropic 提示工程指南](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview)

---

## 咒語 0：腦力激盪創業題目

🤖 模式：**Ask**

```text
我是一位大學生，正在修一門創業通識課。
請幫我發想 5 個適合「大學生」作為目標客群的 SaaS（訂閱制網路服務）創業點子。

每個點子請用以下格式說明：
- 產品名稱（要好記、有梗）
- 一句話介紹（像電梯簡報）
- 解決什麼痛點
- 可能的收費方式（例如：免費＋進階付費、月訂閱）

我的興趣是：【例如：美食、寵物、運動、占卜、租屋、二手交易】
```

---

## 咒語 1：產生 SaaS 形象首頁（核心咒語）

🤖 模式：**Agent**

```text
你是一位資深的前端工程師兼 UI 設計師。
請在目前的工作區（資料夾）根目錄建立一個 index.html，做成 SaaS 新創產品的「形象首頁（Landing Page）」。

【產品資訊】
- 產品名稱：【例如：三峽租屋雷達】
- 一句話介紹：【例如：北大學生專屬的真實租屋評價平台，避開雷房東】
- 目標客群：【例如：國立臺北大學的學生】
- 三個核心功能：【例如：1. 真實評價 2. 房東紅黑榜 3. 找室友媒合】
- 收費方式：【例如：基本免費，進階會員每月 49 元】
- 想要的風格：【例如：清新、活潑、年輕、有信任感，主色調是青綠色】

【技術要求（很重要）】
1. 所有 HTML、CSS、JavaScript 都寫在「同一個 index.html 檔案」裡。
2. 不要使用任何需要安裝的框架（例如 React、Vue），使用純 HTML/CSS/JS。
3. 不要引用外部圖片檔，圖示請使用 Emoji 或內嵌 SVG。
4. 必須支援手機版（RWD 響應式設計），並包含 <meta charset="UTF-8"> 與 viewport 設定。
5. 使用繁體中文。

【頁面需要包含的區塊】
1. 導覽列（Logo + 選單）
2. 主視覺（大標題、副標題、行動呼籲按鈕 CTA，例如「搶先體驗」）
3. 痛點區（目標客群現在遇到什麼困擾）
4. 功能介紹（三個核心功能，用卡片呈現）
5. 價格方案（免費版 vs. 進階版）
6. 常見問題 FAQ
7. 頁尾（版權宣告）

完成後請告訴我怎麼在瀏覽器預覽。
改完後請不要幫我執行 git 指令，我會自己用 VS Code 的原始檔控制存檔。
```

> 🏗️ **架構呼應**：Copilot 產出的這個檔案，就是 SaaS 架構中的 **前端（Frontend）**，也就是你這家雲端餐廳的 **裝潢與門面**。

✅ 完成後：按 **Keep** → 在 `index.html` 上按右鍵 **Show Preview**（或雙擊用瀏覽器打開）。

---

## 咒語 2：改到你滿意為止

🤖 模式：**Agent**

AI 第一次產出的結果通常不會完美，這很正常！Vibe Coding 的精髓就是「**看結果 → 給回饋 → 再修改**」。

```text
請把 #index.html 的主色調改成【莫蘭迪藍】，整體感覺更【沉穩專業】。其他部分保持不變。
```

```text
請在 #index.html 的主視覺區加上一個簡單的動畫效果，例如標題淡入。其他部分保持不變。
```

```text
請在 #index.html 的功能介紹和價格方案之間，新增一個「使用者推薦」區塊，放 3 則虛構的學生好評。
```

```text
#index.html 在手機上導覽列跑版了，請改成手機上顯示「漢堡選單」。
```

```text
請只修改 #index.html 的【價格方案】區塊，改成三個方案：免費、學生 49 元、團體 199 元。其他部分保持不變。
```

> 💡 **省次數小技巧**：Copilot 免費版每月次數有限。把 2～3 個修改**合在一句話**一次說完。
> 💡 **看得到才改得準**：可以截圖（`Win+Shift+S`／`⌘⇧4`）直接貼進 Copilot Chat，說「這個地方跑版了」。

> 🔁 **每改到一個滿意的版本，就 Commit 一次！** 訊息寫清楚改了什麼，例如 `改成莫蘭迪藍`。改壞了隨時可以回來。

---

## 咒語 3：卡關急救包 🚑

```text
我用 Show Preview 打開 #index.html，【畫面一片空白 / 排版很亂 / 按鈕沒反應】。
請幫我檢查可能的原因，並直接修正檔案。
```

```text
（Ask 模式）請用非電資背景的大學生也聽得懂的方式，解釋 #index.html 的每個區塊在做什麼。
```

```text
（Ask 模式）我在 VS Code 原始檔控制按 Commit，出現這個訊息：【貼上訊息】。我該怎麼辦？請一步一步教我。
```

---

## 🧰 沒有 Copilot 時的備案

Copilot 次數用完、或帳號出問題？一樣可以完成：

1. 用網頁版 AI（[Claude](https://claude.ai/)／[ChatGPT](https://chatgpt.com/)／[Gemini](https://gemini.google.com/)），把咒語 1 開頭改成「請給我完整的 index.html 程式碼」。
   （[咒語產生器](slides/prompt_builder.html) 選這些 AI 會自動幫你改好。）
2. 在 VS Code 的 repo 資料夾按 **新增檔案** 圖示，取名 `index.html`。
3. 把 AI 給的程式碼**全部**貼進去，按 `Ctrl+S`（Mac：`⌘S`）存檔。
4. 接下來一樣用 **原始檔控制** Commit ＋ Sync。

---

存好 `index.html` 了嗎？下一步 👉 [存檔、上雲、開店](steps.md#段落-4存檔上雲開店)
