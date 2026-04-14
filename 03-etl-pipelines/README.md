# 03 - ETL Pipeline

> 數據工程師的日常：把資料從 A 搬到 B，途中清洗轉換。

## 學習目標

- [ ] 理解 ETL vs ELT 的差異與趨勢
- [ ] 能用 Python 寫一條完整的 ETL pipeline
- [ ] 理解 Batch vs Streaming 的取捨
- [ ] 知道常見的資料品質問題與處理方式

## ETL vs ELT

| | ETL | ELT |
|---|-----|-----|
| Transform 在哪 | 中間層（ETL 工具） | 目標端（資料倉儲內） |
| 適合 | 傳統企業、資料量中等 | 雲端倉儲、大資料量 |
| 代表工具 | Informatica, Talend | dbt, Spark SQL |
| 趨勢 | 逐漸減少 | 主流 |

## Batch vs Streaming

| | Batch | Streaming |
|---|-------|-----------|
| 延遲 | 分鐘～小時 | 秒～毫秒 |
| 複雜度 | 低 | 高 |
| 適合 | 報表、日結、歷史分析 | 即時監控、風控、推薦 |
| 工具 | Spark, Airflow | Kafka, Flink, Spark Streaming |

### 實務建議
> 能用 Batch 解決的就不要用 Streaming。Streaming 的維運成本遠高於 Batch。

## Pipeline 設計原則

- **冪等性（Idempotent）**：重跑不會產生重複資料
- **可觀測性**：每一步有 log、有 metrics
- **失敗處理**：retry 機制、dead letter queue
- **資料驗證**：schema check、row count check、null check

## 常見資料品質問題

- 重複資料（deduplication）
- NULL / 缺值處理
- 時區問題（UTC vs local）
- 編碼問題（UTF-8 vs Big5）
- Schema 變更（上游偷改欄位）

## 練習

1. 寫一條 Python ETL：從 API 取資料 → 清洗 → 寫入 PostgreSQL
2. 加上 retry 機制與 logging
3. 確保 pipeline 具有冪等性（重跑不會重複）
