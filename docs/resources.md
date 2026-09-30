# 延伸學習資源

課堂時間僅兩次、共四小時，只能涵蓋每個主題的核心概念。本清單依主題整理可信的延伸閱讀，並附簡要說明與難度標示，供課後依興趣深入。

**難度說明**

| 難度 | 意義 |
| --- | --- |
| 入門 | 無需背景知識，適合所有修課同學 |
| 進階 | 需要本課程內容作為基礎，或涉及較多專業術語 |
| 深入 | 專業文件、學術論文或完整教科書，適合有志於相關領域者 |

**選讀建議**：若只有一小時，建議依序閱讀第 1 節的 NIST 雲端定義與 Lean Startup 原則、第 2 節的社群媒體架構講義、第 9 節的 AI 輔助程式設計限制，這四份資料對應本課程最核心的概念。

[← 回課程首頁](../README.md)　｜　[名詞解釋](glossary.md)

---

## 1. SaaS 商業模式與創業方法

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [NIST SP 800-145：The NIST Definition of Cloud Computing](https://csrc.nist.gov/pubs/sp/800/145/final) | 美國國家標準與技術研究院對雲端運算及 SaaS、PaaS、IaaS 的正式定義，篇幅僅數頁，是引用最廣的定義來源 | 進階 |
| [Microsoft Azure：什麼是 SaaS？](https://azure.microsoft.com/zh-tw/resources/cloud-computing-dictionary/what-is-saas) | SaaS 的定義、優缺點與常見應用，繁體中文 | 入門 |
| [Red Hat：IaaS、PaaS、SaaS 的差異](https://www.redhat.com/zh/topics/cloud-computing/iaas-vs-paas-vs-saas) | 以責任分工的角度比較三種雲端服務模式 | 入門 |
| [The Lean Startup：核心原則](https://theleanstartup.com/principles) | Eric Ries 的精實創業方法：MVP、建造—測量—學習、驗證式學習 | 入門 |
| [Y Combinator Startup Library](https://www.ycombinator.com/library) | 知名創業加速器的免費影片與文章庫，涵蓋找題目、募資、成長 | 進階 |
| [Y Combinator：How to Build an MVP](https://www.ycombinator.com/library/Io-how-to-build-an-mvp) | 如何界定 MVP 的範圍，以及常見的過度開發陷阱 | 進階 |
| [Paul Graham：Do Things That Don't Scale](https://paulgraham.com/ds.html) | 說明新創初期為何應親自接觸使用者、手動完成看似無法規模化的工作 | 進階 |
| [Steve Blank 部落格](https://steveblank.com/) | 「顧客開發（Customer Development）」方法的提出者，精實創業的理論來源之一 | 進階 |

## 2. SaaS 經濟學與指標

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [Stripe：什麼是月經常性收入（MRR）](https://stripe.com/resources/more/what-is-monthly-recurring-revenue) | MRR 的定義、計算方式與常見誤區 | 入門 |
| [a16z：16 Startup Metrics](https://a16z.com/16-startup-metrics/) | 創投機構整理的新創核心指標，包括 CAC、LTV、流失率、毛利 | 進階 |
| [David Skok：SaaS Metrics 2.0](https://www.forentrepreneurs.com/saas-metrics-2/) | SaaS 單位經濟學的經典長文，說明 LTV 與 CAC 的關係及現金流「J 曲線」 | 深入 |
| [Bessemer Venture Partners：Atlas](https://www.bvp.com/atlas) | 創投機構對雲端與 SaaS 產業的長期研究與年度報告 | 深入 |

## 3. 系統架構

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [社群媒體的 SaaS 架構（本課講義）](../lectures/wk01_1007_saas-storefront/social_media_architecture.md) | 按讚、發布限時動態時，背後各系統元件的分工 | 入門 |
| [SaaS 架構（本課講義）](../lectures/wk01_1007_saas-storefront/saas_architecture.md) | 本課程網站的前端、BaaS 與部署架構 | 入門 |
| [MDN：CDN](https://developer.mozilla.org/zh-TW/docs/Glossary/CDN) | 內容傳遞網路的定義與用途 | 入門 |
| [Cloudflare Learning Center](https://www.cloudflare.com/zh-tw/learning/) | 以淺顯方式說明 CDN、DNS、負載平衡、無伺服器等網路基礎概念，有繁體中文 | 入門 |
| [Red Hat：什麼是微服務？](https://www.redhat.com/zh/topics/microservices/what-are-microservices) | 微服務與單體式架構的比較 | 進階 |
| [Martin Fowler：Microservices](https://martinfowler.com/articles/microservices.html) | 定義微服務架構特徵的經典文章 | 深入 |
| [The Twelve-Factor App](https://12factor.net/zh_cn/) | 建構 SaaS 應用的十二項原則，例如設定與程式碼分離、無狀態程序（簡體中文版） | 深入 |
| [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/) | 雲端架構在可靠性、安全性、成本、效能等面向的設計準則 | 深入 |
| [System Design Primer](https://github.com/donnemartin/system-design-primer) | 大型系統設計的開放教材，含大量架構圖與取捨分析 | 深入 |
| [Meta Engineering](https://engineering.fb.com/)・[Netflix TechBlog](https://netflixtechblog.com/) | 大型科技公司工程團隊公開的架構實務文章 | 深入 |

## 4. VS Code 與 GitHub Copilot

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [VS Code 與 GitHub Copilot 入門（本課教學）](tutorials/vscode_copilot_starter.md) | 從安裝、運作原理到第一個網頁 | 入門 |
| [VS Code 入門影片](https://code.visualstudio.com/docs/getstarted/introvideos) | 官方系列短片，介紹編輯器基本操作 | 入門 |
| [VS Code：設定 Copilot](https://code.visualstudio.com/docs/copilot/setup) | 官方設定步驟 | 入門 |
| [VS Code：Copilot 總覽](https://code.visualstudio.com/docs/copilot/overview) | Copilot 在 VS Code 中的各項功能 | 入門 |
| [VS Code：Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat) | Ask 與 Agent 等模式的差異與用法 | 進階 |
| [VS Code：提示詞撰寫技巧](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting) | 如何提供上下文與明確需求 | 進階 |
| [GitHub Copilot 文件](https://docs.github.com/zh/copilot) | 官方完整文件，包括資料使用與負責任使用說明 | 進階 |
| [GitHub Copilot 方案](https://github.com/features/copilot/plans) | Free 與付費方案的額度比較 | 入門 |
| [GitHub Education](https://education.github.com/) | 學生身分驗證後可免費使用 Copilot Pro 與其他開發工具 | 入門 |

## 5. 網頁基礎

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [MDN：網頁入門](https://developer.mozilla.org/zh-TW/docs/Learn_web_development/Getting_started/Your_first_website) | Mozilla 的網頁開發入門課程，繁體中文 | 入門 |
| [MDN：Learn web development](https://developer.mozilla.org/en-US/docs/Learn_web_development) | MDN 完整的網頁開發學習路徑，由 HTML、CSS 到 JavaScript | 進階 |
| [MDN：網際網路如何運作](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work) | 在瀏覽器輸入網址後發生的事 | 入門 |
| [MDN：HTTP 概觀](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Overview) | 瀏覽器與伺服器之間的通訊協定 | 進階 |
| [MDN：響應式設計](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) | viewport、彈性版面與媒體查詢 | 進階 |
| [web.dev Learn](https://web.dev/learn) | Google 的現代網頁開發課程，包括無障礙與效能 | 進階 |
| [freeCodeCamp](https://www.freecodecamp.org/) | 免費的互動式程式設計課程 | 進階 |
| [Flexbox Froggy](https://flexboxfroggy.com/#zh-tw) | 以遊戲練習 CSS Flexbox 排版，有繁體中文 | 入門 |
| [W3C Web Accessibility Initiative](https://www.w3.org/WAI/fundamentals/accessibility-intro/) | 網頁無障礙的基本概念，說明為何網站應讓所有人都能使用 | 進階 |

## 6. Git 與版本控制

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [Git 與 GitHub 入門（本課教學）](tutorials/git_intro.md) | 四個區域、commit、分支、同步與合併衝突 | 入門 |
| [VS Code：Git 入門](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git) | 以 VS Code 介面操作 Git 的官方教學 | 入門 |
| [GitHub Docs：Hello World](https://docs.github.com/zh/get-started/start-your-journey/hello-world) | GitHub 官方入門，含分支與 Pull Request | 入門 |
| [GitHub Skills](https://skills.github.com/) | 在 GitHub 上逐步完成的互動課程 | 入門 |
| [Learn Git Branching](https://learngitbranching.js.org/?locale=zh_TW) | 以視覺化方式練習分支、合併與重定基底，有繁體中文 | 進階 |
| [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials) | 圖解 Git 概念與團隊工作流程的比較 | 進階 |
| [Chris Beams：How to Write a Git Commit Message](https://cbea.ms/git-commit/) | 廣受引用的 commit 訊息撰寫七原則 | 進階 |
| [Conventional Commits](https://www.conventionalcommits.org/zh-hant/v1.0.0/) | 結構化 commit 訊息的規範，常用於自動產生版本紀錄 | 深入 |
| [Pro Git（繁體中文）](https://git-scm.com/book/zh-tw/v2) | Git 官方教科書，第 10 章說明 Git 的內部資料結構 | 深入 |

## 7. Netlify 與雲端部署

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [GitHub 與 Netlify 部署（本課教學）](tutorials/github_netlify_deploy.md) | 部署機制、webhook、CDN 與 HTTPS | 入門 |
| [Netlify Docs](https://docs.netlify.com/) | 官方文件首頁 | 入門 |
| [Netlify：從 Git 儲存庫部署](https://docs.netlify.com/start/quickstarts/deploy-from-repository/) | 本課程第 1 週使用的部署方式 | 入門 |
| [Netlify：網域入門](https://docs.netlify.com/manage/domains/get-started-with-domains/) | 自訂網域與 DNS 設定 | 進階 |
| [Netlify Functions](https://docs.netlify.com/build/functions/overview/) | 在 Netlify 上執行無伺服器函式，是加入後端邏輯的下一步 | 深入 |
| 其他託管平台：[Vercel](https://vercel.com/docs)・[GitHub Pages](https://pages.github.com/)・[Cloudflare Pages](https://pages.cloudflare.com/) | 比較不同平台的免費額度、功能與限制，思考平台依賴風險 | 進階 |

## 8. BaaS 與資料儲存

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [Netlify Forms 教學（本課）](tutorials/netlify_forms.md)・[LocalStorage 教學（本課）](tutorials/localstorage.md) | 第 2 週使用的兩種資料保存方式 | 入門 |
| [Netlify Forms 官方文件](https://docs.netlify.com/manage/forms/setup/) | 表單偵測、垃圾訊息過濾與通知設定 | 入門 |
| [MDN：localStorage](https://developer.mozilla.org/zh-TW/docs/Web/API/Window/localStorage) | 瀏覽器端儲存的 API 與限制 | 入門 |
| [MDN：Fetch API](https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API) | 以 JavaScript 非同步送出資料的方式 | 進階 |
| [Supabase 文件](https://supabase.com/docs) | 開源 BaaS，提供 PostgreSQL 資料庫、身分驗證與檔案儲存 | 深入 |
| [Firebase 文件](https://firebase.google.com/docs) | Google 的 BaaS 平台 | 深入 |
| 表單服務：[Google 表單](https://www.google.com/forms/about/)・[Tally](https://tally.so/)・[Formspree](https://formspree.io/) | Netlify Forms 的替代方案，可比較其資料所有權與額度 | 入門 |

## 9. AI 輔助程式設計：能力與限制

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [Vibe coding（Wikipedia）](https://en.wikipedia.org/wiki/Vibe_coding) | 名詞的由來、應用範圍與爭議 | 入門 |
| [Andrej Karpathy 的原始貼文](https://x.com/karpathy/status/1886192184808149383) | 2025 年 2 月提出「vibe coding」一詞的貼文 | 入門 |
| [Anthropic：提示工程概觀](https://docs.anthropic.com/en/docs/build-with-claude/prompt-engineering/overview) | 撰寫清楚提示詞的原則與範例 | 進階 |
| [OpenAI：提示工程指南](https://platform.openai.com/docs/guides/prompt-engineering) | 同主題，OpenAI 的版本 | 進階 |
| [Pearce et al. (2021). Asleep at the Keyboard? Assessing the Security of GitHub Copilot's Code Contributions](https://arxiv.org/abs/2108.09293) | 研究發現 Copilot 在特定資安情境下產生的程式碼中，有相當比例含有弱點 | 深入 |
| [Perry et al. (2023). Do Users Write More Insecure Code with AI Assistants?](https://arxiv.org/abs/2211.03622) | 使用者實驗：使用 AI 助理的受試者寫出的程式碼較不安全，卻更傾向相信自己的程式碼是安全的 | 深入 |
| [OWASP Top 10 for LLM Applications](https://genai.owasp.org/) | 大型語言模型應用的主要資安風險，例如提示詞注入 | 深入 |
| [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework) | 美國 NIST 發布的 AI 風險管理框架 | 深入 |
| AI 網站產生服務：[v0](https://v0.dev/)・[Bolt](https://bolt.new/)・[Lovable](https://lovable.dev/) | 以一段描述產生完整網站的新創服務，本身即是 AI 時代的 SaaS 案例 | 進階 |

**使用提醒**：上述研究顯示，AI 產生的程式碼可能含有錯誤或安全弱點，而使用者容易高估其可靠性。AI 輔助開發適合原型與 MVP；處理金流、個人資料或身分驗證的正式產品，仍需要具備專業知識的人員審查與測試。

## 10. CI/CD 與敏捷開發

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [CI/CD 教學（本課）](tutorials/cicd.md)・[GitHub Actions 自動檢核（本課）](tutorials/vibe_check_ci.md) | 本課程的持續部署與自動檢核實作 | 入門 |
| [Red Hat：什麼是 CI/CD](https://www.redhat.com/zh/topics/devops/what-is-ci-cd) | 持續整合、持續交付與持續部署的差異 | 入門 |
| [敏捷軟體開發宣言](https://agilemanifesto.org/iso/zhcht/manifesto.html) | 2001 年提出的四項價值，繁體中文 | 入門 |
| [Martin Fowler：Continuous Integration](https://martinfowler.com/articles/continuousIntegration.html) | 持續整合實務的經典文章 | 深入 |
| [Atlassian：敏捷開發](https://www.atlassian.com/agile) | Scrum、看板等敏捷方法介紹 | 進階 |
| [GitHub Actions 文件](https://docs.github.com/zh/actions) | 工作流程、觸發條件與執行器的完整說明 | 深入 |

## 11. 資訊安全與個人資料保護

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [個人資料保護法（全國法規資料庫）](https://law.moj.gov.tw/LawClass/LawAll.aspx?pcode=I0050021) | 臺灣蒐集、處理與利用個人資料的法律規範。以表單收集 Email 前應了解告知義務 | 進階 |
| [歐盟一般資料保護規則（GDPR）原文](https://eur-lex.europa.eu/eli/reg/2016/679/oj) | 若產品服務歐盟使用者，需遵守的個資法規，也是各國立法的重要參考 | 深入 |
| [GitHub Docs：關於秘密掃描](https://docs.github.com/zh/code-security/secret-scanning/introduction/about-secret-scanning) | 為何不應將金鑰與密碼提交到 repo，以及 GitHub 的偵測機制 | 進階 |
| [OWASP Top 10](https://owasp.org/www-project-top-ten/) | 最常見的十大網站應用程式資安風險 | 深入 |
| [MDN：Web 安全](https://developer.mozilla.org/en-US/docs/Web/Security) | HTTPS、同源政策、內容安全政策等瀏覽器安全機制 | 深入 |

## 12. 產品發表與簡報

| 資源 | 說明 | 難度 |
| --- | --- | --- |
| [發表範本（本課）](pitch_template.md) | 1 分鐘 MVP 發表的結構 | 入門 |
| [Y Combinator Startup Library](https://www.ycombinator.com/library) | 搜尋「How to pitch your company」，說明如何在短時間內清楚介紹新創 | 進階 |
| [Guy Kawasaki：10/20/30 簡報法則](https://guykawasaki.com/the_102030_rule/) | 10 張投影片、20 分鐘、30 級字的簡報原則 | 入門 |
| [Canva](https://www.canva.com/) | 線上設計與簡報工具，本身也是以免費增值模式成長的 SaaS 案例 | 入門 |
