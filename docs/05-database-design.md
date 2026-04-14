# Database Design 資料庫設計

Knowing how to choose and design databases is a core data engineering skill.

知道如何選擇和設計資料庫是數據工程的核心技能。

## Database Types 資料庫類型

### OLTP (Transactional 交易型)
| Database 資料庫 | Use Case 使用場景 |
|----------|----------|
| PostgreSQL | General purpose, feature-rich 通用首選，功能最完整 |
| MySQL | Web applications, large ecosystem 網頁應用，生態系大 |
| SQL Server | Enterprise, .NET stack 企業環境 |

### OLAP (Analytical 分析型)
| Database 資料庫 | Use Case 使用場景 |
|----------|----------|
| BigQuery | Serverless, GCP ecosystem GCP 生態系 |
| ClickHouse | Fast aggregations, real-time analytics 極快聚合查詢，即時分析 |
| Redshift | AWS ecosystem AWS 生態系 |
| DuckDB | Local analytics, embedded OLAP 本地分析，嵌入式 OLAP |

### NoSQL
| Type 類型 | Example 範例 | Use Case 使用場景 |
|------|---------|----------|
| Document 文件 | MongoDB | Flexible schema 彈性 schema |
| Key-Value 鍵值 | Redis | Caching, sessions 快取、Session |
| Wide Column 寬欄 | Cassandra | High write throughput 大量寫入 |
| Graph 圖 | Neo4j | Relationship networks 關係網路 |

### OLTP vs OLAP
- OLTP: row-based, write-heavy, transactional 行式、寫入多、交易型
- OLAP: column-based, read-heavy, analytical 列式、讀取多、分析型

## Data Modeling 資料建模

### Normalization 正規化 (OLTP)
- 1NF → 2NF → 3NF → BCNF
- Goal: reduce redundancy, maintain consistency 目標：減少冗餘、維持一致性
- Typical for transactional systems 交易系統常用

### Dimensional Modeling 維度建模 (OLAP)

#### Star Schema 星型架構
- **Fact tables 事實表**: measurements, metrics, foreign keys 度量值、指標、外鍵
- **Dimension tables 維度表**: descriptive attributes 描述性屬性 (who, what, when, where)
- Simple to query, good performance 查詢直覺、效能好

#### Snowflake Schema 雪花架構
- Dimensions are further normalized 維度再正規化
- Saves storage, but more joins 節省空間，但 JOIN 變多

#### Design Steps 設計步驟
1. Choose the grain 決定粒度 (what does one row represent? 一筆 row 代表什麼？)
2. Identify dimensions 找出維度
3. Identify facts 找出事實
4. Decide on fact table type 決定事實表類型: transaction / periodic snapshot / accumulating

### Slowly Changing Dimensions (SCD) 緩慢變動維度

| Type 類型 | Approach 做法 | When to Use 適用場景 |
|------|----------|-------------|
| Type 0 | Never update 不更新 | Fixed attributes 固定屬性 (birth date 生日) |
| Type 1 | Overwrite 直接覆蓋 | No history needed 不需要歷史 |
| Type 2 | Add new row + validity period 新增一筆 + 有效期間 | Track full history 追蹤完整歷史 |
| Type 3 | Add column for previous value 加欄位存前一個值 | Only need before/after 只需前後對比 |

## Key Concepts 重要觀念

- **ACID**: Atomicity, Consistency, Isolation, Durability 原子性、一致性、隔離性、持久性
- **Indexes 索引**: B-Tree, Hash — know when to use them 知道何時使用
- **Partitioning 分區**: split tables by date or key for performance 依日期或 key 分割表以提升效能
- **Connection pooling 連線池**: reuse database connections 重複使用資料庫連線

## Practice 練習

1. Design a star schema for an e-commerce scenario 為電商場景設計星型架構
2. Implement SCD Type 2 for a customer dimension 為客戶維度實作 SCD Type 2
3. Compare query performance with and without indexes 比較有無索引的查詢效能

## Key Takeaway 重點

> Choose the right database for the workload. Design schemas with query patterns in mind, not just data structure.
>
> 根據工作負載選擇適合的資料庫。設計 schema 時考慮查詢模式，不只是資料結構。
