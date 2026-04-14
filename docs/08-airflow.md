# Airflow

Apache Airflow is the most widely used workflow orchestration tool for data pipelines.

Apache Airflow 是最廣泛使用的資料管線工作流程編排工具。

## Why Not Just Cron? 為什麼不用 Cron 就好？

- Cron can schedule, but can't manage dependencies between tasks Cron 能排程，但不能管理任務間的相依性
- Cron has no retry mechanism, no alerting, no backfill Cron 沒有重試機制、沒有告警、沒有 backfill
- Cron doesn't show you what failed or why Cron 不會告訴你哪裡失敗、為什麼失敗

## Core Concepts 核心概念

- **DAG** (Directed Acyclic Graph 有向無環圖): defines the workflow — tasks and their order 定義工作流程——任務和執行順序
- **Task**: a single unit of work in a DAG DAG 中的一個工作單元
- **Operator**: the type of task 任務類型 (BashOperator, PythonOperator, etc.)
- **Sensor**: waits for a condition to be met before proceeding 等待條件滿足後才繼續
- **XCom**: pass small data between tasks 在任務間傳遞小量資料
- **Connection**: stored credentials for external systems 儲存外部系統的憑證
- **Variable**: stored configuration values 儲存設定值

## Best Practices 最佳實踐

### DAG Design DAG 設計
- Keep business logic out of the DAG file — the DAG only orchestrates 不要在 DAG 檔裡寫商業邏輯，DAG 只負責編排
- Use TaskGroups to organize complex DAGs 用 TaskGroup 組織複雜 DAG
- Store credentials in Connections, not hardcoded 憑證存在 Connection，不要寫死
- Set meaningful `default_args`: owner, retries, retry_delay 設定有意義的 `default_args`

### Common Pitfalls 常見踩坑
- DAG files are parsed by the scheduler every ~30 seconds — keep imports fast DAG 檔每 30 秒被解析一次，import 不要太慢
- Default SequentialExecutor only runs one task at a time 預設 SequentialExecutor 一次只跑一個 task
- Airflow uses UTC internally — handle timezone conversions explicitly Airflow 內部用 UTC，時區要自己處理
- XCom is for small data (a few KB), not dataframes XCom 用於小資料（幾 KB），不是 dataframe

### Backfill 回補
One of Airflow's killer features Airflow 的殺手級功能:
```bash
airflow dags backfill -s 2024-01-01 -e 2024-01-31 my_dag
```
Reprocess historical data without changing code. 不改程式碼就能重新處理歷史資料。

## Alternatives 替代方案

| Tool 工具 | Key Difference 主要差異 |
|------|---------------|
| Prefect | Python-native, simpler than Airflow 比 Airflow 簡潔 |
| Dagster | Asset-centric, strong typing 以資產為中心，強型別 |
| Mage | Low barrier, good for small teams 低門檻，適合小團隊 |
| Kestra | Declarative, YAML-based 宣告式，YAML 定義 |

## Practice 練習

See 參見 [projects/airflow-demo](../projects/airflow-demo/).

1. Run Airflow locally with Docker Compose 用 Docker Compose 在本地跑 Airflow
2. Write a DAG that extracts, transforms, and loads data 寫一個 ETL DAG
3. Add retry + alerting (Slack or email) 加上重試和告警
4. Practice backfilling a date range 練習 backfill 一段日期

## Key Takeaway 重點

> Airflow orchestrates — it tells tasks when and in what order to run. Keep the DAG thin and the logic in separate modules.
>
> Airflow 負責編排——告訴任務何時、以何順序執行。DAG 保持精簡，邏輯寫在別的模組。
