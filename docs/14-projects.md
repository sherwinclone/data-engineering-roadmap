# Projects 實作專案

Hands-on projects are the best way to learn and the best way to prove your skills.

動手做專案是最好的學習方式，也是最好的能力證明。

## Project Index 專案索引

| Project 專案 | Level 難度 | What You'll Learn 你會學到 |
|---------|-------|-------------------|
| [Beginner ETL 入門 ETL](../projects/beginner-etl/) | Beginner 入門 | Basic ETL: extract from API, transform, load to database 基本 ETL |
| [Batch Pipeline 批次管線](../projects/batch-pipeline/) | Intermediate 中階 | Full batch pipeline with data quality checks 完整批次管線含品質檢查 |
| [Airflow Demo](../projects/airflow-demo/) | Intermediate 中階 | Workflow orchestration with Airflow 用 Airflow 編排工作流程 |
| [Spark Demo](../projects/spark-demo/) | Intermediate 中階 | Distributed data processing with Spark 用 Spark 分散式處理 |
| [Streaming Demo 串流示範](../projects/streaming-demo/) | Advanced 進階 | Real-time processing with Kafka 用 Kafka 即時處理 |

## Additional Project Ideas 更多專案點子

### Beginner 入門
- CSV to database loader with validation CSV 載入資料庫（含驗證）
- Public API data collector (weather, stock prices) 公開 API 資料蒐集器（天氣、股價）
- Log file parser and aggregator Log 檔案解析與聚合

### Intermediate 中階
- Daily sales ETL with SCD Type 2 dimensions 每日銷售 ETL 搭配 SCD Type 2
- Clickstream log processing pipeline 點擊流日誌處理管線
- Star schema data warehouse for an e-commerce dataset 電商星型架構資料倉儲
- dbt project with tests and documentation 含測試和文件的 dbt 專案

### Advanced 進階
- Real-time event processing with Kafka + Spark Streaming 即時事件處理
- Data lake with Bronze/Silver/Gold layers on cloud storage 雲端儲存上的三層資料湖
- End-to-end pipeline: ingestion → warehouse → dashboard 端到端管線
- Data quality monitoring system with alerting 含告警的資料品質監控系統

## Building a Portfolio 建立作品集

### What Hiring Managers Look For 面試官看什麼
- Working code, not just READMEs 能跑的程式碼，不只是 README
- Clear documentation 清楚的文件: what it does, how to run it, architecture diagram 做什麼、怎麼跑、架構圖
- Realistic data problems 真實的資料問題 (not just toy examples 不只是玩具範例)
- Evidence of engineering discipline 工程紀律的證據: tests, logging, error handling 測試、日誌、錯誤處理

### Tips 建議
- Use Docker so anyone can run your project 用 Docker 讓任何人都能跑
- Include a `Makefile` or clear setup instructions 附上 `Makefile` 或清楚的安裝說明
- Write a good README with architecture diagrams 寫好 README 並附架構圖
- Show your thought process 展示思考過程: why you made certain decisions 為什麼做某些決定

## Key Takeaway 重點

> Build things. A working project teaches more than reading ten tutorials. Document it well and put it on GitHub.
>
> 動手做。一個能跑的專案勝過讀十篇教學文。好好寫文件，放上 GitHub。
