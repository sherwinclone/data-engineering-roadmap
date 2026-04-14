# Batch Pipeline 批次處理管線

A complete batch ETL pipeline with data quality checks.
包含資料品質檢查的完整批次 ETL 管線。

## Goals 目標

- Build a multi-step pipeline 建構多步驟管線
- Implement Bronze → Silver → Gold layers 實作 Bronze → Silver → Gold 分層
- Add data validation between steps 在步驟間加入資料驗證

## Architecture 架構

```
CSV Files → Bronze (raw) → Silver (cleaned) → Gold (aggregated)
CSV 檔案 → Bronze（原始）→ Silver（清洗）→ Gold（聚合）
```

## Steps 步驟

1. Ingest CSV files into a Bronze table (raw, as-is)
   將 CSV 檔案載入 Bronze 表（原始資料）
2. Clean and deduplicate into Silver
   清洗與去重後寫入 Silver
3. Aggregate into Gold (business metrics)
   聚合為 Gold（商業指標）
4. Add row count checks between each step
   在每個步驟間加入 row count 檢查
5. Log execution details
   記錄執行細節

## Tech Stack 技術棧

- Python 3
- pandas or DuckDB
- PostgreSQL or DuckDB
- logging module
