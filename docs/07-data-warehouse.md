# Data Warehouse 資料倉儲

Centralize data from many sources into a single, query-optimized system.

將散落各處的資料集中到一個查詢最佳化的系統。

## Architecture Comparison 架構比較

| | Data Warehouse 資料倉儲 | Data Lake 資料湖 | Data Lakehouse |
|---|----------------|-----------|----------------|
| Data format 資料格式 | Structured 結構化 | Any 任意 | Any 任意 |
| Schema | Schema-on-Write | Schema-on-Read | Both 兩者 |
| Examples 範例 | BigQuery, Redshift | S3, GCS | Databricks, Delta Lake |
| Best for 適合 | BI, SQL analytics SQL 分析 | ML, unstructured data 非結構化資料 | Both 兩者 |

## Medallion Architecture 獎章架構

```
Raw Data → Bronze (raw 原始) → Silver (cleaned 清洗) → Gold (business logic 商業邏輯)
```

- **Bronze**: Raw data, stored as-is from source systems 原封不動存入，保留原始資料
- **Silver**: Deduplicated, cleaned, typed, joined 去重、清洗、型別轉換、JOIN
- **Gold**: Aggregated, business metrics, ready for BI 聚合、商業指標、給 BI 看的最終表

### Why Layers? 為什麼要分層？
- Reprocessing 重新處理: if transformation logic changes, rerun from Bronze 邏輯改了從 Bronze 重跑
- Debugging 除錯: trace data issues back to the raw layer 追溯資料問題到原始層
- Separation of concerns 關注點分離: ingestion and transformation are independent 擷取和轉換互相獨立

## Key Tools 主要工具

### BigQuery
- Serverless, pay per query (scan volume) 無伺服器，依查詢量收費
- Partitioning and clustering for performance 分區和叢集以提升效能
- Supports standard SQL 支援標準 SQL
- Tip 提醒: LIMIT does not reduce cost — use partitions LIMIT 不會省錢，要用 partition

### Databricks
- Built on Apache Spark 基於 Apache Spark
- Delta Lake format: ACID transactions + time travel Delta Lake 格式：ACID 交易 + 時間旅行
- Unity Catalog for governance 用 Unity Catalog 做資料治理
- Good for large-scale processing + ML 適合大規模處理 + ML

### dbt (Data Build Tool)
- SQL-based transformation layer (the T in ELT) 基於 SQL 的轉換層（ELT 中的 T）
- Version control for SQL models SQL 模型的版本控制
- Built-in testing 內建測試: unique, not_null, accepted_values
- Auto-generated documentation and lineage 自動產生文件和資料血緣

#### Core Concepts 核心概念
- **Model**: one `.sql` file = one table or view 一個 `.sql` 檔 = 一張表或 view
- **Source**: defines raw data tables 定義原始資料表
- **Test**: schema tests + custom SQL tests 結構測試 + 自訂 SQL 測試
- **Ref**: reference other models to build a DAG 參照其他 model 建立 DAG

## Practice 練習

See 參見 [projects/batch-pipeline](../projects/batch-pipeline/).

1. Build a Bronze → Silver → Gold pipeline in BigQuery or DuckDB 在 BigQuery 或 DuckDB 建立三層管線
2. Use dbt to manage transformations and add tests 用 dbt 管理轉換並加入測試
3. Explore Delta Lake time travel 探索 Delta Lake 時間旅行

## Key Takeaway 重點

> A data warehouse is only as good as its modeling. Layer your data, test your assumptions, and document your transformations.
>
> 資料倉儲的好壞取決於建模。分層你的資料、測試你的假設、記錄你的轉換。
