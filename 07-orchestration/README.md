# 07 - 排程與編排

> Pipeline 寫完只是開始，讓它每天穩定跑起來才是挑戰。

## 學習目標

- [ ] 理解 Orchestration 在資料工程中的角色
- [ ] 能使用 Airflow 建立 DAG
- [ ] 理解排程失敗的處理策略
- [ ] 知道 Airflow 以外的選擇

## 為什麼需要 Orchestrator？

- crontab 能排程，但不能管依賴、不能重跑、不能監控
- 資料 pipeline 之間有先後順序（DAG）
- 需要 retry、alerting、backfill 功能

## Apache Airflow

### 核心概念
- **DAG**：有向無環圖，定義任務流程
- **Task**：DAG 中的一個步驟
- **Operator**：任務類型（BashOperator, PythonOperator, etc.）
- **Sensor**：等待條件滿足
- **XCom**：任務間傳遞小量資料

### 實務經驗
- 不要在 DAG 裡寫商業邏輯，DAG 只負責編排
- 善用 TaskGroup 組織複雜 DAG
- Connection 和 Variable 存在 Airflow，不要 hardcode
- Backfill 是殺手功能：`airflow dags backfill -s 2024-01-01 -e 2024-01-31`

### 常見踩坑
- DAG 檔案在 scheduler 每 30 秒解析一次，不要寫太慢的 import
- 預設 Sequential Executor 只能跑一個 task
- 時區問題：Airflow 內部用 UTC

## 其他選擇

| 工具 | 特色 |
|------|------|
| Prefect | Python native，比 Airflow 簡潔 |
| Dagster | 以資產（Asset）為中心，強型別 |
| Mage | 低門檻，適合小團隊 |
| Kestra | 宣告式，YAML 定義 |

## 練習

1. 用 Docker 架 Airflow，寫一個簡單的 ETL DAG
2. 設定失敗 retry + Slack/Email 通知
3. 練習 Backfill：重跑過去 7 天的資料
