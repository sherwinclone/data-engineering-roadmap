# Cloud 雲端平台

Modern data engineering runs on cloud platforms. Learn at least one well.

現代數據工程在雲端平台上運作。至少熟悉一家。

## GCP (Google Cloud Platform)

### Key Services for Data Engineers DE 常用服務
| Service 服務 | Purpose 用途 |
|---------|---------|
| BigQuery | Serverless data warehouse 無伺服器資料倉儲 |
| Cloud Storage (GCS) | Object storage (data lake) 物件儲存（資料湖） |
| Cloud Functions | Lightweight event-driven compute 輕量事件驅動運算 |
| Pub/Sub | Message queue 訊息佇列 |
| Composer | Managed Airflow 托管 Airflow |
| Dataproc | Managed Spark / Hadoop 托管 Spark / Hadoop |
| Dataflow | Managed Apache Beam |

### Starting Point 入門建議
BigQuery + GCS + Cloud Functions covers ~80% of use cases.
BigQuery + GCS + Cloud Functions 能覆蓋約 80% 的場景。

## AWS (Amazon Web Services)

### Key Services for Data Engineers DE 常用服務
| Service 服務 | Purpose 用途 |
|---------|---------|
| S3 | Object storage 物件儲存 |
| Redshift | Data warehouse 資料倉儲 |
| Glue | ETL service ETL 服務 |
| Lambda | Serverless compute 無伺服器運算 |
| Kinesis | Streaming data 串流資料 |
| MWAA | Managed Airflow 托管 Airflow |
| EMR | Managed Spark / Hadoop 托管 Spark / Hadoop |

## Azure

### Key Services for Data Engineers DE 常用服務
| Service 服務 | Purpose 用途 |
|---------|---------|
| Azure Data Lake Storage | Object storage 物件儲存 |
| Synapse Analytics | Data warehouse + Spark |
| Data Factory | ETL / orchestration 編排 |
| Azure Functions | Serverless compute 無伺服器運算 |
| Event Hubs | Streaming 串流 |
| Databricks on Azure | Managed Spark 托管 Spark |

## Cloud Concepts 雲端觀念

### Infrastructure as Code 基礎設施即程式碼
- Terraform: cloud-agnostic, most popular 跨雲，最主流
- Pulumi: code-based 程式碼導向 (Python, TypeScript)
- Cloud-specific 各雲專用: CloudFormation (AWS), Deployment Manager (GCP)

### Cost Management 費用控管
- Set budget alerts 設定預算警報
- Shut down dev environments when not in use 開發環境不用就關
- Use free tiers for learning 用免費方案練習
- BigQuery: partition tables — LIMIT doesn't reduce scan cost BigQuery 要分區，LIMIT 不會省錢
- Spot/preemptible instances for batch jobs Batch 作業用搶佔式機器

### Security Basics 安全基礎
- IAM: least privilege principle 最小權限原則
- Service accounts for applications 應用程式用服務帳號
- Secrets management 密鑰管理: Secret Manager, not environment variables in code 不要把密鑰寫在程式碼裡
- VPC and network controls for production 正式環境用 VPC 和網路管控

## Practice 練習

1. Create a free-tier cloud account (GCP or AWS) 建立雲端免費帳號
2. Upload a CSV to GCS/S3 and query it with BigQuery/Athena 上傳 CSV 到 GCS/S3 並查詢
3. Write a Cloud Function / Lambda that runs an ETL task on a schedule 寫一個定時執行的 Cloud Function / Lambda
4. Set up a budget alert 設定預算警報

## Key Takeaway 重點

> Pick one cloud and learn it well. The concepts transfer between providers — the services are different, but the patterns are the same.
>
> 選一家雲端好好學。概念可以互通——服務名不同，但模式相同。
