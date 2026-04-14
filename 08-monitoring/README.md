# 08 - 監控與資料品質

> Pipeline 跑起來不代表正確。你需要知道它什麼時候壞了。

## 學習目標

- [ ] 理解資料品質的維度與檢查方式
- [ ] 能建立基本的 pipeline 監控與告警
- [ ] 知道 ELK Stack 的角色
- [ ] 理解 Data Observability 的概念

## 資料品質維度

| 維度 | 檢查什麼 |
|------|----------|
| Completeness | 有沒有缺值、缺 row |
| Uniqueness | 有沒有重複 |
| Timeliness | 資料有沒有準時到 |
| Accuracy | 數值合不合理 |
| Consistency | 跨表/跨系統是否一致 |

## 資料品質工具

| 工具 | 特色 |
|------|------|
| Great Expectations | Python，規則定義 + 文件產生 |
| dbt tests | 內建 unique, not_null, accepted_values |
| Soda | YAML 定義檢查規則 |
| Elementary | dbt native 的 data observability |

## Pipeline 監控

### 該監控什麼？
- 任務是否成功執行
- 執行時間是否異常（突然變慢 = 有問題）
- Row count 是否合理（突然歸零 = 上游壞了）
- 資料新鮮度（最新資料的時間戳）

### 告警策略
- 不要什麼都告警（alert fatigue）
- 分級：P0（資料掉了）→ P1（延遲）→ P2（品質下降）
- 告警要 actionable：看到通知就知道該做什麼

## ELK Stack

- **Elasticsearch**：搜尋與分析引擎
- **Logstash**：資料收集與轉換
- **Kibana**：視覺化介面

### DE 怎麼用 ELK？
- 收集 pipeline 的 log
- 建立 Dashboard 監控執行狀況
- 設定異常告警

## 練習

1. 用 Great Expectations 為一張表定義品質檢查規則
2. 在 Airflow DAG 裡加入 row count check
3. 設定當 pipeline 失敗時發送通知（Slack / Telegram）
