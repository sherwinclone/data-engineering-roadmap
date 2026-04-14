# 05 - 資料倉儲

> 把散落各處的資料集中、整理、讓人能查詢分析。

## 學習目標

- [ ] 理解 Data Warehouse vs Data Lake vs Data Lakehouse
- [ ] 能使用至少一種倉儲工具（BigQuery / Databricks）
- [ ] 理解 dbt 的角色與基本使用
- [ ] 知道分層架構（Bronze / Silver / Gold）

## 三種架構比較

| | Data Warehouse | Data Lake | Data Lakehouse |
|---|----------------|-----------|----------------|
| 資料格式 | 結構化 | 任意 | 任意 |
| Schema | Schema-on-Write | Schema-on-Read | 兩者皆可 |
| 代表 | BigQuery, Redshift | S3, GCS | Databricks, Delta Lake |
| 適合 | BI 報表、SQL 分析 | ML、非結構化資料 | 兩者兼顧 |

## 分層架構（Medallion Architecture）

```
Raw Data → Bronze（原始） → Silver（清洗） → Gold（商業邏輯）
```

- **Bronze**：原封不動存入，保留原始資料
- **Silver**：去重、清洗、型別轉換、JOIN
- **Gold**：聚合、商業指標、給 BI 看的最終表

## dbt（Data Build Tool）

### 為什麼需要 dbt？
- SQL 也需要版本控制、測試、文件
- ELT 中的 T（Transform）工具
- 定義 model 之間的依賴關係

### 核心概念
- Model：一個 `.sql` 檔 = 一張表/view
- Source：定義原始資料來源
- Test：schema test（unique, not_null）+ custom test
- Documentation：自動產生資料字典

## Databricks

- 基於 Apache Spark
- Delta Lake 格式：ACID + Time Travel
- Unity Catalog：資料治理
- 適合大規模資料處理 + ML

## 練習

1. 在 BigQuery 或 DuckDB 建立 Bronze → Silver → Gold 三層表
2. 用 dbt 管理轉換邏輯，加上測試
3. 理解 Delta Lake 的 Time Travel 功能
