# 00 - 先備知識

> 這些是數據工程師的地基，沒打穩後面都會卡。

## 學習目標

- [ ] Python：能寫腳本處理檔案、呼叫 API、操作資料結構
- [ ] SQL：能寫 JOIN、子查詢、Window Function、效能調校
- [ ] Linux：基本指令操作、cron、權限管理、SSH
- [ ] Git：branch、merge、rebase、PR 流程

## Python

### 必學
- 資料型別：list, dict, set, tuple
- 檔案操作：讀寫 CSV/JSON
- 套件管理：pip, venv
- 常用套件：requests, pandas（基礎即可）

### DE 特別需要的
- Generator / Iterator（處理大檔案不爆記憶體）
- Context Manager（`with` 語法，資源管理）
- logging 模組（不要再用 print debug 了）
- argparse / click（寫 CLI 工具）

## SQL

### 必學
- CRUD 操作
- JOIN 種類與使用時機
- GROUP BY + 聚合函式
- WHERE vs HAVING

### 進階（面試常考）
- Window Function：ROW_NUMBER, RANK, LAG, LEAD
- CTE（Common Table Expression）
- EXPLAIN 看執行計畫
- Index 設計原則

## Linux

### 必學指令
```bash
ls, cd, pwd, mkdir, rm, cp, mv    # 檔案操作
cat, head, tail, grep, wc         # 檔案查看
chmod, chown                       # 權限
ps, top, kill                      # 程序管理
crontab -e                        # 排程
ssh, scp                          # 遠端操作
```

## Git

### 必學
```bash
git init / clone
git add / commit / push / pull
git branch / checkout / merge
git log / diff / stash
```

### 工作中常用
- PR (Pull Request) 流程
- Conflict 解決
- `.gitignore` 設定
- Commit message 規範

## 練習

1. 寫一個 Python 腳本，讀取 CSV 檔案，用 SQL 查詢篩選後輸出結果
2. 在 Linux 上設定一個 cron job，每天執行你的腳本
3. 把以上成果用 Git 管理，推到 GitHub
