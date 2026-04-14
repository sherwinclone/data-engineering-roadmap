# Airflow Demo Airflow 示範

A simple Airflow DAG that orchestrates an ETL workflow.
使用 Airflow DAG 來編排 ETL 工作流程。

## Goals 目標

- Run Airflow locally with Docker Compose
  使用 Docker Compose 在本地執行 Airflow
- Write a DAG with multiple tasks
  撰寫包含多個 task 的 DAG
- Practice retry, alerting, and backfill
  練習 retry、告警與 backfill

## Setup 安裝

```bash
# Download the official docker-compose.yaml
# 下載官方 docker-compose.yaml
curl -LfO 'https://airflow.apache.org/docs/apache-airflow/stable/docker-compose.yaml'

# Initialize
# 初始化
docker compose up airflow-init
docker compose up -d
```

## Project Structure 專案結構

```
airflow-demo/
├── README.md
└── dags/
    └── example_etl_dag.py
```

## Tech Stack 技術棧

- Apache Airflow 2.x
- Docker Compose
- Python
