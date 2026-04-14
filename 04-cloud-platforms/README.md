# 04 - 雲端平台

> 現代 DE 幾乎都在雲端工作，至少熟悉一家。

## 學習目標

- [ ] 理解雲端服務的基本概念（IaaS / PaaS / SaaS）
- [ ] 熟悉至少一個雲端平台的資料相關服務
- [ ] 能在雲端上部署一條 ETL pipeline

## GCP（Google Cloud Platform）

### DE 常用服務
| 服務 | 用途 |
|------|------|
| BigQuery | 資料倉儲，Serverless SQL |
| Cloud Storage (GCS) | 物件儲存（Data Lake） |
| Cloud Functions | 輕量事件驅動運算 |
| Dataflow | Apache Beam 托管服務 |
| Pub/Sub | 訊息佇列 |
| Composer | 托管 Airflow |
| Dataproc | 托管 Spark / Hadoop |

### 入門建議
先學 BigQuery + GCS + Cloud Functions，能覆蓋 80% 場景。

## AWS

### DE 常用服務
| 服務 | 用途 |
|------|------|
| S3 | 物件儲存 |
| Redshift | 資料倉儲 |
| Glue | ETL 服務 |
| Lambda | Serverless 運算 |
| Kinesis | 串流資料處理 |
| MWAA | 托管 Airflow |
| EMR | 托管 Spark / Hadoop |

## 台灣市場觀察

- GCP 與 AWS 使用率接近，依產業而異
- 金融業偏 AWS，新創偏 GCP
- Azure 在大企業有市佔
- 面試通常要求「至少熟悉一家」

## 費用控管

- 設定 Budget Alert
- 用完即關（dev 環境不要 24/7 跑）
- 善用 Free Tier 練習
- BigQuery：注意 scan 量，用 `LIMIT` 不會省錢，要用 partition

## 練習

1. 建立 GCP 或 AWS 免費帳號
2. 上傳 CSV 到 GCS/S3，用 BigQuery/Athena 查詢
3. 寫一個 Cloud Function / Lambda，定時從 API 拉資料存到雲端
