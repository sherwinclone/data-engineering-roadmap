# 01 - 資料庫

> 資料工程師的核心：知道資料放哪裡、怎麼放、怎麼取最快。

## 學習目標

- [ ] 理解 RDBMS vs NoSQL vs OLAP 的差異與使用場景
- [ ] 能操作至少一種 RDBMS（推薦 PostgreSQL）
- [ ] 理解 Index、Partition、Query Plan
- [ ] 知道什麼場景該用什麼資料庫

## RDBMS（關聯式資料庫）

### 常見選擇
| 資料庫 | 適用場景 |
|--------|----------|
| PostgreSQL | 通用首選，功能最完整 |
| MySQL | Web 應用常見，生態系大 |
| SQL Server | 企業環境，搭配 .NET |

### 必學觀念
- ACID 特性
- Transaction 與 Isolation Level
- Index 種類：B-Tree, Hash, GIN
- Query Plan（EXPLAIN ANALYZE）
- Connection Pooling

## NoSQL

### 常見選擇
| 類型 | 代表 | 適用場景 |
|------|------|----------|
| Document | MongoDB | 彈性 schema、快速迭代 |
| Key-Value | Redis | 快取、Session |
| Wide Column | Cassandra | 大量寫入、時序資料 |
| Graph | Neo4j | 關係網路、推薦系統 |

### 何時用 NoSQL？
- Schema 經常變動
- 需要水平擴展
- 讀寫模式固定（query pattern 明確）
- 不需要複雜 JOIN

## OLAP（分析型資料庫）

### 常見選擇
| 資料庫 | 特色 |
|--------|------|
| ClickHouse | 極快的聚合查詢，適合即時分析 |
| BigQuery | Serverless，GCP 生態系 |
| Redshift | AWS 生態系 |
| DuckDB | 本地分析利器，嵌入式 OLAP |

### OLTP vs OLAP
- OLTP：交易型，Row-based，寫入多
- OLAP：分析型，Column-based，讀取多

## 練習

1. 用 Docker 架一個 PostgreSQL，建立 schema 並載入範例資料
2. 對同一張表比較有無 Index 的查詢效能差異
3. 用 ClickHouse 或 DuckDB 做一次聚合查詢，感受 OLAP 速度
