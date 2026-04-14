# Beginner ETL 入門 ETL 專案

Extract data from a public API, transform it, and load it into a database.
從公開 API 擷取資料、轉換、載入資料庫。

## Goals 目標

- Understand the basic ETL flow 理解基本 ETL 流程
- Practice Python file I/O and API calls 練習 Python 檔案操作與 API 呼叫
- Write idempotent load logic 撰寫冪等的載入邏輯

## Steps 步驟

1. Choose a public API (e.g., weather, exchange rates)
   選擇一個公開 API（如天氣、匯率）
2. Write a Python script to fetch data
   撰寫 Python 腳本抓取資料
3. Transform: clean nulls, parse dates, rename columns
   轉換：清理空值、解析日期、重新命名欄位
4. Load into PostgreSQL (use Docker)
   載入 PostgreSQL（使用 Docker）
5. Make it idempotent: re-running should not create duplicates
   確保冪等性：重複執行不會產生重複資料

## Tech Stack 技術棧

- Python 3
- requests
- psycopg2 or SQLAlchemy
- PostgreSQL (Docker)
