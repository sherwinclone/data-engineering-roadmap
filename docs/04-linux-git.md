# Linux & Git

Most data infrastructure runs on Linux. Git is how you manage code. Both are non-negotiable.

大多數資料基礎設施跑在 Linux 上。Git 是管理程式碼的方式。兩者都是必備技能。

## Linux / Command Line 命令列

### Essential Commands 必學指令
```bash
# File operations 檔案操作
ls, cd, pwd, mkdir, rm, cp, mv, touch

# File viewing 檔案查看
cat, head, tail, less, wc

# Search 搜尋
grep, find, which

# Permissions 權限
chmod, chown

# Process management 程序管理
ps, top, htop, kill

# Networking 網路
curl, wget, ssh, scp

# Disk and system 磁碟與系統
df, du, free, uname
```

### Shell Skills Shell 技能
- Pipes and redirection 管線與重導向: `|`, `>`, `>>`, `<`
- Environment variables 環境變數: `export`, `.bashrc`, `.zshrc`
- Cron jobs 排程: `crontab -e`
- Basic shell scripting 基本 Shell 腳本
- Package managers 套件管理: apt, yum, brew

### Key Concepts 重要觀念
- File permissions 檔案權限 (rwx, 755, 644)
- Processes and signals 程序與訊號
- SSH key authentication SSH 金鑰驗證
- PATH and how the shell finds commands PATH 與 Shell 如何找到指令

## Git

### Essential Commands 必學指令
```bash
git init / clone
git status / diff / log
git add / commit / push / pull
git branch / checkout / switch
git merge / rebase
git stash
git reset / revert
```

### Workflow 工作流程
1. Create a feature branch 建立功能分支
2. Make changes and commit with clear messages 修改並提交清楚的 commit message
3. Push and open a pull request 推送並開 PR
4. Code review 程式碼審查
5. Merge to main 合併到 main

### Commit Messages 提交訊息
Use a consistent format 使用一致的格式:
```
type: short description

# Examples 範例:
feat: add daily ETL pipeline for sales data
fix: handle null values in user dimension
refactor: simplify date parsing logic
docs: add setup instructions
```

### .gitignore
Always exclude 必須排除:
- `.env` files (credentials 憑證)
- `__pycache__/`, `*.pyc`
- `.venv/`, `node_modules/`
- IDE files IDE 設定: `.idea/`, `.vscode/`
- Data files 資料檔案: `*.csv`, `*.parquet` (unless small samples 除非是小型範例)

## Practice 練習

1. Set up SSH keys for GitHub 設定 GitHub SSH 金鑰
2. Create a repo, make branches, open a PR 建立 repo、開分支、開 PR
3. Write a cron job that runs a script daily 寫一個每日執行腳本的 cron job
4. SSH into a remote server and run commands SSH 進遠端伺服器並執行指令

## Key Takeaway 重點

> You don't need to be a sysadmin. But you need to be comfortable in a terminal and able to manage code with Git.
>
> 你不需要成為系統管理員，但你需要能自在地使用終端機並用 Git 管理程式碼。
