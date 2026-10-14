# Pickle Charm Shop 一頁版步驟清單

做完一步就打勾。詳細說明見 [實作指南](pickle_charm_lab.md)，提示詞見 [提示詞](pickle_charm_prompts.md)。

## Part 0 準備
- [ ] 1 Fork `cychiang-ntpu/pickle-charm-shop` 到自己帳號
- [ ] 2 VS Code 原始檔控制 → 複製存放庫 → 選自己的 fork → 開啟
- [ ] 3 終端機 `git config --global --list` 有名字與 Email；Copilot 面板可開

## Part 1 Netlify 上線
- [ ] 4 Netlify → Add new project → Import → GitHub → `pickle-charm-shop` → Build 設定留空 → 取名 → Deploy → Published
- [ ] 5 手機打開網址；網址貼到群組（檢核點 3）
- [ ] 6 Netlify → Forms → Enable form detection

## Part 2 註冊與登入
- [ ] 7 Copilot（Agent）貼提示詞 1 → 保留
- [ ] 8 `Ctrl+F` 找到 `data-netlify`、`form-name`；本機預覽可開對話框
- [ ] 9 提交 `新增註冊與登入` → 同步變更
- [ ] 10 Deploys 變 Published → 手機註冊 → 重新整理仍顯示歡迎 → 登出
- [ ] 11 Netlify → Forms → signup 看到資料（檢核點 4、5）
- [ ] 交換駕駛／導航員

## Part 3 真正的下訂單
- [ ] 12 Copilot（Agent）貼提示詞 2 → 保留
- [ ] 13 本機：加入兩種商品 → 開購物車 → 改數量 → 總金額正確
- [ ] 14 提交 `新增購物車與下訂單` → 同步變更 → Published
- [ ] 15 手機下單 → 看到「訂單已送出」與摘要
- [ ] 16 Netlify → Forms → order 看到 name、phone、address、items、total
- [ ] 交換駕駛／導航員

## Part 4 通知與自動更新
- [ ] 17 Forms → Submission notifications → Add notification → Email → form 選 order → 再下一筆 → 收到信
- [ ] 18 Copilot 改按鈕文字 → 提交 → 同步 → 不碰 Netlify → 手機看到新版（檢核點 6）

## Part 5 收尾
- [ ] 19 到兩位同學的商店下單；看自己收到幾筆
- [ ] 20 出場券；公用電腦：登出 GitHub、Netlify、VS Code
