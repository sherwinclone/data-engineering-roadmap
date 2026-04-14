# Overview 總覽

## What Does a Data Engineer Do? 數據工程師在做什麼？

A Data Engineer is responsible for building and maintaining the infrastructure that allows data to flow reliably from source systems to destinations where it can be analyzed and used.

數據工程師負責建置和維護資料基礎設施，讓資料能可靠地從來源系統流向分析和使用端。

### Core Responsibilities 核心職責

- **Data Pipelines 資料管線**: Design, build, and maintain ETL/ELT pipelines 設計、建置和維護 ETL/ELT 管線
- **Data Modeling 資料建模**: Design schemas for data warehouses and data lakes 設計資料倉儲和資料湖的 schema
- **Infrastructure 基礎設施**: Set up and manage databases, message queues, and orchestration tools 架設和管理資料庫、訊息佇列和排程工具
- **Data Quality 資料品質**: Ensure data is accurate, complete, and timely 確保資料的正確性、完整性和時效性
- **Performance 效能**: Optimize queries, storage, and processing for cost and speed 優化查詢、儲存和處理的成本與速度

### Data Engineer vs Related Roles 數據工程師 vs 相關角色

| Role 角色 | Focus 專注 |
|------|-------|
| Data Engineer 數據工程師 | Build and maintain data infrastructure and pipelines 建置與維護資料基礎設施和管線 |
| Data Analyst 資料分析師 | Analyze data, create reports and dashboards 分析資料、建立報表和儀表板 |
| Data Scientist 資料科學家 | Build models, run experiments, statistical analysis 建構模型、執行實驗、統計分析 |
| Analytics Engineer 分析工程師 | Transform data in the warehouse (dbt, SQL-focused) 在倉儲中轉換資料 |
| ML Engineer 機器學習工程師 | Deploy and serve machine learning models 部署和服務機器學習模型 |

## The Data Engineering Lifecycle 資料工程生命週期

```
Source Systems → Ingestion → Storage → Transformation → Serving → Analytics/ML
來源系統 → 擷取 → 儲存 → 轉換 → 供應 → 分析/ML
```

Each stage involves different tools and design decisions. This roadmap walks through them in a practical order.

每個階段涉及不同的工具和設計決策，本路線圖會以實務順序逐一介紹。

## How to Use This Roadmap 如何使用本路線圖

1. Follow the suggested learning order in the README 依照 README 的建議學習順序
2. Read each topic doc for concepts and tools 閱讀每個主題文件了解概念與工具
3. Complete the hands-on projects in the `projects/` folder 完成 `projects/` 資料夾中的實作專案
4. Use the templates to track your study progress 使用模板追蹤學習進度
5. Build your own portfolio projects for job applications 建立自己的作品集用於求職

## Prerequisites 先備條件

Before starting, you should have:
開始之前，你應該具備：

- Basic comfort with a programming language (Python recommended) 基本的程式語言能力（推薦 Python）
- Ability to write simple SQL queries 能寫簡單的 SQL 查詢
- Access to a terminal (macOS/Linux preferred) 能使用終端機（推薦 macOS/Linux）
- A GitHub account 一個 GitHub 帳號
