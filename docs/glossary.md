# 名詞解釋

本表收錄課程中出現的專業術語，依「商業、架構、網頁、版本控制、部署、AI」六類整理。每個名詞提供英文全名、精確定義，以及本課程中的對應實例，可作為閱讀講義與準備成果發表時的參考。

課堂上以「美食街」比喻 SaaS 平台：商場（雲端平台）提供場地、水電與保全，店家（軟體新創）只需專注於菜單與服務。比喻有助於建立直覺，但本表的定義以技術與商業上的精確意義為準。

[← 回課程首頁](../README.md)　｜　[延伸學習資源](resources.md)

## 目錄

1. [商業](#1-商業)
2. [架構](#2-架構)
3. [網頁](#3-網頁)
4. [版本控制](#4-版本控制)
5. [部署](#5-部署)
6. [AI](#6-ai)

---

## 1. 商業

| 名詞 | 英文／全名 | 定義 | 延伸閱讀 |
| --- | --- | --- | --- |
| **SaaS** | Software as a Service／軟體即服務 | 由供應商在雲端集中維運軟體，使用者透過網路（通常是瀏覽器）存取，並以訂閱方式付費的軟體交付模式。使用者不需安裝、升級或維護伺服器。例如 Google Workspace、Canva、Notion | [Azure：什麼是 SaaS](https://azure.microsoft.com/zh-tw/resources/cloud-computing-dictionary/what-is-saas) |
| **訂閱制** | Subscription model | 使用者定期（每月或每年）付費以持續取得服務使用權，而非一次性購買。是 SaaS 最常見的收費方式，特點是營收可預測、客戶終身價值取決於留存率 | [Stripe：什麼是 MRR](https://stripe.com/resources/more/what-is-monthly-recurring-revenue) |
| **Freemium** | Free＋Premium／免費增值 | 基本功能免費提供以擴大使用者基礎，進階功能或更高額度需付費的定價策略。GitHub Copilot Free 與 Pro、Netlify 免費與付費方案皆為此類 | — |
| **MRR** | Monthly Recurring Revenue／月經常性收入 | 每月可預期、重複發生的訂閱收入總和，不含一次性收入。年化後稱為 ARR（Annual Recurring Revenue）。是衡量 SaaS 規模與成長的核心指標 | [Stripe：什麼是 MRR](https://stripe.com/resources/more/what-is-monthly-recurring-revenue) |
| **流失率** | Churn rate | 一段期間內取消訂閱的客戶（或營收）占期初的比例。流失率高時，即使持續獲得新客戶，營收也難以成長 | [a16z：16 Startup Metrics](https://a16z.com/16-startup-metrics/) |
| **CAC／LTV** | Customer Acquisition Cost／Customer Lifetime Value | CAC：取得一位付費客戶的平均成本（行銷、業務費用）。LTV：一位客戶在整個使用期間貢獻的預期毛利。LTV 明顯高於 CAC，商業模式才可持續 | [a16z：16 Startup Metrics](https://a16z.com/16-startup-metrics/) |
| **精實創業** | Lean Startup | Eric Ries 提出的創業方法論：將產品構想視為待驗證的假設，以「建造—測量—學習（Build–Measure–Learn）」循環快速取得市場回饋，降低在錯誤方向上投入資源的風險 | [The Lean Startup：原則](https://theleanstartup.com/principles) |
| **MVP** | Minimum Viable Product／最小可行產品 | 以最少的開發投入，足以驗證核心假設（例如「使用者願意留下聯絡方式」）的產品版本。重點在於學習，而非功能完整 | [YC：How to Build an MVP](https://www.ycombinator.com/library/Io-how-to-build-an-mvp) |
| **形象首頁** | Landing page／登陸頁 | 為單一目的（例如收集候補名單）設計的獨立網頁，通常包含價值主張、功能說明與行動呼籲。本課程第 1 週的產出 | [Unbounce：What is a landing page](https://unbounce.com/landing-page-articles/what-is-a-landing-page/) |
| **價值主張** | Value proposition | 以一句話說明產品為誰解決什麼問題，以及與替代方案相比的優勢 | — |
| **CTA** | Call to Action／行動呼籲 | 引導使用者採取特定行動的介面元素，例如「加入早鳥名單」按鈕。其點擊或轉換比例是衡量首頁效果的指標 | — |
| **候補名單** | Waitlist | 產品正式上線前，收集潛在使用者聯絡方式的名單。名單人數與來源可作為市場需求的初步證據 | — |
| **轉換率** | Conversion rate | 完成目標行動（例如送出表單）的訪客占總訪客的比例 | — |
| **A/B 測試** | A/B testing | 將使用者隨機分為兩組，分別呈現兩個版本（例如不同的 CTA 文字），比較其轉換率，以數據判斷哪個版本較佳的實驗方法 | — |

## 2. 架構

| 名詞 | 英文／全名 | 定義 | 延伸閱讀 |
| --- | --- | --- | --- |
| **IaaS** | Infrastructure as a Service／基礎設施即服務 | 雲端供應商提供虛擬機器、儲存與網路等基礎運算資源，作業系統以上的軟體由使用者自行安裝與維運。例如 AWS EC2、Google Compute Engine | [Red Hat：IaaS、PaaS、SaaS](https://www.redhat.com/zh/topics/cloud-computing/iaas-vs-paas-vs-saas) |
| **PaaS** | Platform as a Service／平台即服務 | 供應商提供應用程式的執行與部署平台，使用者只需提供程式碼，伺服器、作業系統與擴展由平台負責。Netlify 屬於此類 | [Red Hat：IaaS、PaaS、SaaS](https://www.redhat.com/zh/topics/cloud-computing/iaas-vs-paas-vs-saas) |
| **BaaS** | Backend as a Service／後端即服務 | 以雲端服務形式提供常見的後端功能，例如資料庫、身分驗證、檔案儲存與表單收集，前端透過 API 直接使用。本課程的 Netlify Forms 屬於此類；Firebase、Supabase 為功能更完整的例子 | [Backend as a service（Wikipedia）](https://en.wikipedia.org/wiki/Backend_as_a_service) |
| **無伺服器** | Serverless | 開發者不需佈建或管理伺服器，由雲端平台依請求自動配置運算資源並按用量計費的架構。「無伺服器」指的是開發者看不到伺服器，而非真的沒有伺服器 | [Cloudflare：什麼是無伺服器](https://www.cloudflare.com/zh-tw/learning/serverless/what-is-serverless/) |
| **前端** | Frontend | 在使用者裝置（瀏覽器）上執行、負責呈現畫面與處理互動的部分，主要由 HTML、CSS、JavaScript 構成 | [MDN：網頁入門](https://developer.mozilla.org/zh-TW/docs/Learn_web_development/Getting_started/Your_first_website) |
| **後端** | Backend | 在伺服器上執行、負責資料儲存、商業邏輯、身分驗證等使用者看不到的部分 | [MDN：伺服器端程式設計](https://developer.mozilla.org/zh-TW/docs/Learn_web_development/Extensions/Server-side/First_steps/Introduction) |
| **API** | Application Programming Interface／應用程式介面 | 軟體元件之間約定好的溝通方式，規定可以提出哪些請求、要附帶哪些資料、會得到什麼回應。網頁 API 通常透過 HTTP 傳送 JSON 格式的資料 | [MDN：API](https://developer.mozilla.org/zh-TW/docs/Glossary/API) |
| **資料庫** | Database | 以結構化方式長期儲存與查詢資料的系統，例如會員資料、訂單。與 LocalStorage 不同，資料庫位於伺服器端，可供所有使用者與裝置共用 | [MDN：Database](https://developer.mozilla.org/en-US/docs/Glossary/Database) |
| **CDN** | Content Delivery Network／內容傳遞網路 | 由分布在世界各地的伺服器節點組成的網路，將網站的靜態檔案複製到各節點，由距離使用者較近的節點回應，以降低延遲並分散流量 | [MDN：CDN](https://developer.mozilla.org/zh-TW/docs/Glossary/CDN) |
| **負載平衡** | Load balancing | 將進入的請求分配到多台伺服器，避免單一伺服器過載，並在某台故障時將流量導向其他伺服器 | [Cloudflare：什麼是負載平衡](https://www.cloudflare.com/zh-tw/learning/performance/what-is-load-balancing/) |
| **快取** | Cache | 將經常使用或計算成本高的資料暫存在存取速度較快的位置（記憶體、CDN 節點、瀏覽器），以縮短回應時間。代價是資料可能不是最新版本 | [MDN：Cache](https://developer.mozilla.org/en-US/docs/Glossary/Cache) |
| **訊息佇列** | Message queue | 讓系統元件以非同步方式傳遞工作的中介機制：產生工作的一方將訊息放入佇列，處理的一方依序取出執行，可平緩流量高峰、解除元件之間的直接相依 | [社群媒體架構（本課講義）](../lectures/wk01_1007_saas-storefront/social_media_architecture.md) |
| **微服務** | Microservices | 將大型應用拆分為多個獨立部署、各自負責單一業務功能的小型服務，透過 API 溝通的架構風格。相對於將所有功能放在同一程式中的單體式（monolithic）架構 | [Red Hat：什麼是微服務](https://www.redhat.com/zh/topics/microservices/what-are-microservices) |
| **推播通知** | Push notification | 由伺服器主動發送到使用者裝置的通知。行動裝置上須經由 Apple（APNs）或 Google（FCM）的推播服務轉送 | [社群媒體架構（本課講義）](../lectures/wk01_1007_saas-storefront/social_media_architecture.md) |
| **可擴展性** | Scalability | 系統在使用量增加時，透過增加資源維持效能的能力。垂直擴展是升級單台機器；水平擴展是增加機器數量 | [System Design Primer](https://github.com/donnemartin/system-design-primer) |

## 3. 網頁

| 名詞 | 英文／全名 | 定義 | 延伸閱讀 |
| --- | --- | --- | --- |
| **HTML** | HyperText Markup Language／超文本標記語言 | 以標籤（例如 `<h1>`、`<form>`）描述網頁內容與結構的標記語言，定義網頁上「有哪些元素」 | [MDN：HTML](https://developer.mozilla.org/zh-TW/docs/Web/HTML) |
| **CSS** | Cascading Style Sheets／階層式樣式表 | 描述 HTML 元素外觀與版面配置的語言，例如顏色、字型、間距與排版 | [MDN：CSS](https://developer.mozilla.org/zh-TW/docs/Web/CSS) |
| **JavaScript** | JavaScript（JS） | 在瀏覽器中執行的程式語言，負責網頁的互動行為，例如攔截表單送出、讀寫 LocalStorage、切換畫面 | [MDN：JavaScript](https://developer.mozilla.org/zh-TW/docs/Web/JavaScript) |
| **HTTP／HTTPS** | HyperText Transfer Protocol（Secure） | 瀏覽器與伺服器之間傳輸網頁資料的通訊協定。HTTPS 以 TLS 加密傳輸內容，防止竊聽與竄改 | [MDN：HTTP 概觀](https://developer.mozilla.org/zh-TW/docs/Web/HTTP/Overview) |
| **DNS** | Domain Name System／網域名稱系統 | 將人類可讀的網域名稱（例如 `example.com`）轉換為伺服器 IP 位址的分散式系統 | [MDN：什麼是網域名稱](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_domain_name) |
| **靜態網站** | Static site | 伺服器只傳送預先準備好的檔案（HTML、CSS、JS、圖片），不在每次請求時執行程式產生內容的網站。本課程的網站屬於此類 | [MDN：網際網路如何運作](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/How_does_the_Internet_work) |
| **RWD** | Responsive Web Design／響應式網頁設計 | 讓同一份網頁依裝置螢幕寬度自動調整版面的設計方法，主要技術為 viewport 設定、彈性版面與 CSS 媒體查詢（media query） | [MDN：響應式設計](https://developer.mozilla.org/en-US/docs/Learn_web_development/Core/CSS_layout/Responsive_Design) |
| **Viewport** | Viewport／可視區域 | 瀏覽器中實際顯示網頁的區域。行動版網頁須在 `<head>` 加入 `<meta name="viewport" content="width=device-width, initial-scale=1">`，否則手機會以桌面寬度縮小顯示 | [MDN：Viewport](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Elements/meta/name/viewport) |
| **字元編碼（UTF-8）** | Character encoding | 將文字對應為位元組的規則。UTF-8 可表示全世界的文字，是網頁的標準編碼。未宣告時中文可能顯示為亂碼 | [MDN：Character encoding](https://developer.mozilla.org/en-US/docs/Glossary/Character_encoding) |
| **LocalStorage** | Web Storage API：localStorage | 瀏覽器提供的鍵值（key–value）儲存空間，依網域分開，關閉瀏覽器後仍保留。只存在該瀏覽器中，不會同步到其他裝置或伺服器，且可被同網域的 JavaScript 讀取，因此不適合存放敏感資料 | [MDN：localStorage](https://developer.mozilla.org/zh-TW/docs/Web/API/Window/localStorage) |
| **AJAX／fetch** | Asynchronous JavaScript and XML／Fetch API | 以 JavaScript 在背景向伺服器傳送或取得資料、不需重新載入整個頁面的技術。現代瀏覽器以 `fetch()` 實作。本課程用於在原頁面送出表單並切換畫面 | [MDN：Fetch API](https://developer.mozilla.org/zh-TW/docs/Web/API/Fetch_API) |
| **DevTools** | Browser developer tools／瀏覽器開發者工具 | 瀏覽器內建的檢查與除錯工具，可查看 HTML 結構、CSS、JavaScript 錯誤（Console）、網路請求與儲存資料 | [MDN：瀏覽器開發者工具](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Tools_and_setup/What_are_browser_developer_tools) |
| **Honeypot** | Honeypot field／誘捕欄位 | 表單中對人類隱藏、但自動化程式會填寫的欄位。若該欄位有值，即判定為垃圾提交。Netlify Forms 支援此機制 | [Netlify Forms](https://docs.netlify.com/manage/forms/setup/) |

## 4. 版本控制

| 名詞 | 英文／全名 | 定義 | 延伸閱讀 |
| --- | --- | --- | --- |
| **版本控制系統** | Version Control System（VCS） | 記錄檔案變更歷史，使多人能協作、比較差異與回復先前版本的系統 | [Pro Git 第 1 章](https://git-scm.com/book/zh-tw/v2) |
| **Git** | Git | 2005 年由 Linus Torvalds 建立的開放原始碼分散式版本控制系統。每個複本都包含完整歷史，可離線操作 | [Git 官方網站](https://git-scm.com/) |
| **GitHub** | GitHub | 以 Git 為基礎的雲端代管與協作平台，提供 repo 代管、Issue、Pull Request、Actions 等功能 | [GitHub Docs](https://docs.github.com/zh) |
| **Repository（repo）** | Repository／儲存庫 | 一個專案的所有檔案及其完整版本歷史。本機 repo 的歷史存放在隱藏資料夾 `.git` 中 | [關於儲存庫](https://docs.github.com/zh/repositories/creating-and-managing-repositories/about-repositories) |
| **工作目錄** | Working tree | 你在檔案總管中看到、正在編輯的專案檔案 | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **暫存區** | Staging area／index | 存放「將納入下一個 commit」之變更的區域，讓使用者挑選要提交的內容 | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **Commit** | Commit／提交 | 專案在某一時間點的快照，包含作者、時間、訊息與父 commit，並以內容計算出的雜湊值（hash）唯一識別 | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **分支** | Branch | 指向某個 commit 的可移動名稱標籤；在分支上 commit 時會自動前移。新 repo 的預設分支通常為 `main` | [Pro Git：分支簡介](https://git-scm.com/book/zh-tw/v2) |
| **Remote／origin** | Remote | 同一 repo 位於其他位置的複本，例如 GitHub 上的 repo。clone 時預設命名為 `origin` | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **Clone** | Clone／複製 | 將遠端 repo（含完整歷史）下載到本機，並自動設定 `origin` | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **Push** | Push／推送 | 將本機的新 commit 上傳到遠端 repo | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **Fetch／Pull** | Fetch／Pull | Fetch：下載遠端的新 commit，但不改動工作目錄。Pull：fetch 後再整合進目前分支 | [Git 與 GitHub 入門](tutorials/git_intro.md) |
| **Sync** | Sync Changes／同步變更 | VS Code 的便利操作，依序執行 pull 與 push | [VS Code：Git 入門](https://code.visualstudio.com/docs/sourcecontrol/intro-to-git) |
| **合併衝突** | Merge conflict | 兩個版本修改了同一檔案的同一段內容，Git 無法自動決定保留哪一方時產生的狀態，需人工決定最終內容 | [GitHub Docs：關於合併衝突](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/about-merge-conflicts) |
| **.gitignore** | .gitignore | 列出 Git 不應追蹤之檔案樣式的設定檔，常用於排除系統檔、建置產物與含機密的設定檔 | [Git 官方文件：gitignore](https://git-scm.com/docs/gitignore) |
| **Pull Request（PR）** | Pull Request | 在 GitHub 上提出「將某分支的變更合併到另一分支」的請求，供他人審查、討論並執行自動檢查 | [GitHub Docs：關於 Pull Request](https://docs.github.com/zh/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) |

## 5. 部署

| 名詞 | 英文／全名 | 定義 | 延伸閱讀 |
| --- | --- | --- | --- |
| **部署** | Deploy | 將軟體從開發環境發布到正式執行環境，使使用者可以存取的過程 | [Netlify Docs](https://docs.netlify.com/) |
| **託管** | Hosting | 由服務商提供伺服器與網路，讓網站能持續對外提供服務 | [MDN：什麼是 Web 伺服器](https://developer.mozilla.org/en-US/docs/Learn_web_development/Howto/Web_mechanics/What_is_a_web_server) |
| **建置** | Build | 將原始碼轉換為可部署產物的步驟，例如編譯、打包、壓縮。純 HTML 網站不需要建置 | [GitHub 與 Netlify 部署](tutorials/github_netlify_deploy.md) |
| **發布目錄** | Publish directory | 部署平台要對外發布的資料夾，其中的 `index.html` 為網站首頁 | [GitHub 與 Netlify 部署](tutorials/github_netlify_deploy.md) |
| **Webhook** | Webhook | 事件發生時，由一個系統主動向另一個系統預先登記的網址發送 HTTP 請求的通知機制。GitHub 在收到 push 時以 webhook 通知 Netlify | [GitHub Docs：關於 webhook](https://docs.github.com/zh/webhooks/about-webhooks) |
| **OAuth** | Open Authorization | 讓使用者授權第三方應用程式以有限權限存取其帳號資源，而不需交出密碼的授權標準。VS Code 與 Netlify 連接 GitHub 時皆使用 | [OAuth 2.0](https://oauth.net/2/) |
| **CI** | Continuous Integration／持續整合 | 開發者頻繁將變更整合到共同的程式碼庫，並在每次整合時自動執行建置與測試，以盡早發現問題的實務 | [Red Hat：什麼是 CI/CD](https://www.redhat.com/zh/topics/devops/what-is-ci-cd) |
| **CD** | Continuous Delivery／Deployment／持續交付／持續部署 | 持續交付：程式碼隨時處於可部署狀態。持續部署：通過檢查的變更自動發布到正式環境。本課程中每次 Sync 即自動更新網站，屬持續部署 | [Red Hat：什麼是 CI/CD](https://www.redhat.com/zh/topics/devops/what-is-ci-cd) |
| **GitHub Actions** | GitHub Actions | GitHub 內建的自動化平台，依 `.github/workflows/` 中的 YAML 工作流程檔，在事件觸發時於雲端執行器上執行工作 | [GitHub Actions 文件](https://docs.github.com/zh/actions) |
| **原子化部署** | Atomic deploy | 新版本的所有檔案完整上傳後才一次切換為正式版本，避免使用者看到新舊混合的網站；也使回復舊版成為可能 | [Netlify Docs](https://docs.netlify.com/) |
| **回復** | Rollback | 將正式環境切換回先前的版本。Netlify 可在 Deploys 頁面發布先前的部署 | [CI/CD 教學](tutorials/cicd.md) |
| **TLS 憑證** | TLS certificate | 證明網站身分、並用於建立 HTTPS 加密連線的數位憑證。Netlify 會自動為網站申請與更新 | [MDN：HTTPS](https://developer.mozilla.org/en-US/docs/Glossary/HTTPS) |

## 6. AI

| 名詞 | 英文／全名 | 定義 | 延伸閱讀 |
| --- | --- | --- | --- |
| **大型語言模型** | Large Language Model（LLM） | 以大量文字資料訓練、能根據上下文預測後續文字的神經網路模型。可用於對話、摘要與程式碼產生，但輸出為統計上合理的內容，不保證正確 | [Wikipedia：Large language model](https://en.wikipedia.org/wiki/Large_language_model) |
| **提示詞** | Prompt | 提供給 AI 模型的指示與資料。明確描述目標、限制與驗收條件，通常能得到較符合需求的結果 | [VS Code：提示詞撰寫技巧](https://code.visualstudio.com/docs/copilot/chat/prompt-crafting) |
| **上下文** | Context | 模型產生回應時可參考的全部資訊，包括提示詞、對話紀錄與附加的檔案內容。上下文長度有上限 | [VS Code：Copilot 總覽](https://code.visualstudio.com/docs/copilot/overview) |
| **幻覺** | Hallucination | 模型產生看似合理但與事實不符的內容，例如引用不存在的函式、套件或文件 | [Wikipedia：Hallucination (AI)](https://en.wikipedia.org/wiki/Hallucination_%28artificial_intelligence%29) |
| **Vibe Coding** | Vibe coding | Andrej Karpathy 於 2025 年提出的說法，指以自然語言描述需求、主要由 AI 產生程式碼，開發者著重於檢視結果並給予回饋的開發方式。適合原型與 MVP，但對正式產品的品質與安全性仍有爭議 | [Wikipedia：Vibe coding](https://en.wikipedia.org/wiki/Vibe_coding) |
| **GitHub Copilot** | GitHub Copilot | GitHub 推出的 AI 程式設計助理，整合於 VS Code 等編輯器，提供程式碼補全與對話式修改 | [VS Code：Copilot 總覽](https://code.visualstudio.com/docs/copilot/overview) |
| **Ask 模式** | Ask mode | Copilot Chat 中只回答問題、不修改檔案的模式，適合理解概念與詢問錯誤原因 | [VS Code：Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat) |
| **Agent 模式** | Agent mode | Copilot Chat 中可自主規劃步驟、建立與修改多個檔案並提議執行終端機指令的模式。使用時須檢視差異後再保留變更 | [VS Code：Copilot Chat](https://code.visualstudio.com/docs/copilot/chat/copilot-chat) |
| **VS Code** | Visual Studio Code | Microsoft 開發的免費、開放原始碼程式碼編輯器，可透過延伸模組擴充功能 | [VS Code](https://code.visualstudio.com/) |
| **配對程式設計** | Pair programming | 兩人共用一個工作環境：駕駛（driver）負責操作，導航員（navigator）負責檢視與規劃，並定期交換角色。本課程中 AI 也可視為一種協作者，但人仍須承擔審查責任 | [Wikipedia：Pair programming](https://en.wikipedia.org/wiki/Pair_programming) |
