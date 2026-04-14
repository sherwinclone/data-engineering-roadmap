# ETL / ELT

Moving data from A to B, transforming it along the way. This is the daily work of a data engineer.

把資料從 A 搬到 B，途中清洗轉換。這是數據工程師的日常工作。

## ETL vs ELT

| | ETL | ELT |
|---|-----|-----|
| Transform where 轉換在哪 | In the pipeline (middle layer) 在管線中（中間層） | In the target (warehouse) 在目標端（倉儲內） |
| Good for 適合 | Traditional, medium data volumes 傳統、中等資料量 | Cloud warehouses, large volumes 雲端倉儲、大資料量 |
| Tools 工具 | Informatica, Talend, custom Python | dbt, Spark SQL, warehouse SQL |
| Trend 趨勢 | Declining 減少中 | Mainstream 主流 |

Modern data stacks favor ELT: load raw data first, transform in the warehouse using SQL.

現代資料棧偏好 ELT：先載入原始資料，在倉儲內用 SQL 轉換。

## Batch vs Streaming 批次 vs 串流

| | Batch 批次 | Streaming 串流 |
|---|-------|-----------|
| Latency 延遲 | Minutes to hours 分鐘到小時 | Seconds to milliseconds 秒到毫秒 |
| Complexity 複雜度 | Lower 較低 | Higher 較高 |
| Use cases 使用場景 | Reports, daily aggregations 報表、日結 | Real-time monitoring, fraud detection 即時監控、風控 |
| Tools 工具 | Spark, Airflow, cron | Kafka, Flink, Spark Streaming |

> If batch can solve it, use batch. Streaming ops cost is much higher.
>
> 能用 Batch 解決的就不要用 Streaming。Streaming 的維運成本遠高於 Batch。

## Pipeline Design Principles 管線設計原則

### Idempotency 冪等性
Running the pipeline twice should produce the same result. No duplicate data.

管線跑兩次應該產生相同結果，不會有重複資料。

Strategies 策略:
- DELETE + INSERT (by partition/date 依分區/日期)
- MERGE / UPSERT with a unique key 用唯一鍵
- Write to a temp table, then swap 寫入暫存表再交換

### Observability 可觀測性
- Log every step: start, row counts, errors, duration 記錄每一步：開始、筆數、錯誤、耗時
- Emit metrics that can trigger alerts 發出可觸發告警的指標
- Make it easy to debug failures 讓除錯容易

### Error Handling 錯誤處理
- Retry with exponential backoff 指數退避重試
- Dead letter queue for unprocessable records 無法處理的記錄放入死信佇列
- Alert on repeated failures, not on every retry 重複失敗才告警，不是每次重試都告警

### Data Validation 資料驗證
- Schema checks: expected columns and types Schema 檢查：預期的欄位和型別
- Row count checks: compare source vs target 筆數檢查：比較來源與目標
- Null checks: critical fields should not be null 空值檢查：關鍵欄位不應為 null
- Freshness checks: is the data from today? 新鮮度檢查：資料是今天的嗎？

## Common Data Quality Issues 常見資料品質問題

- Duplicate records 重複資料
- NULL / missing values 空值/缺值
- Timezone mismatches 時區不一致 (UTC vs local)
- Character encoding 字元編碼 (UTF-8 vs legacy encodings)
- Schema drift 結構漂移 (upstream changes columns without notice 上游偷改欄位)

## Practice 練習

See 參見 [projects/beginner-etl](../projects/beginner-etl/) and 和 [projects/batch-pipeline](../projects/batch-pipeline/).

## Key Takeaway 重點

> A good pipeline is idempotent, observable, and handles failure gracefully. Fancy tooling is secondary to these properties.
>
> 好的管線是冪等的、可觀測的、能優雅地處理失敗。花俏的工具是次要的。
