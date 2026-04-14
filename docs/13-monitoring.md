# Monitoring 監控

You need to know when things break — before your stakeholders tell you.

你需要在利害關係人告訴你之前，就知道東西壞了。

## What to Monitor 監控什麼

### Pipeline Health 管線健康度
- Task success/failure status 任務成功/失敗狀態
- Execution duration (sudden slowness = problem) 執行時間（突然變慢 = 有問題）
- SLA compliance (did it finish on time?) SLA 達標（有沒有準時完成？）

### Data Health 資料健康度
- Row counts: sudden drops or spikes 筆數：突然下降或暴增
- Data freshness: latest timestamp 資料新鮮度：最新時間戳
- Schema changes: unexpected columns 結構變更：意外的欄位
- Quality check results 品質檢查結果

### Infrastructure 基礎設施
- CPU, memory, disk usage CPU、記憶體、磁碟使用率
- Database connection pool utilization 資料庫連線池使用率
- Queue depth (Kafka consumer lag) 佇列深度（Kafka 消費延遲）
- Cloud spending 雲端花費

## Alerting Strategy 告警策略

### Severity Levels 嚴重等級
| Level 等級 | Example 範例 | Action 行動 |
|-------|---------|--------|
| P0 - Critical 嚴重 | Data pipeline down 管線掛了 | Immediate response 立即回應 |
| P1 - High 高 | Data delayed 資料延遲 | Respond within hours 數小時內回應 |
| P2 - Medium 中 | Quality degradation 品質下降 | Investigate next business day 下個工作日調查 |
| P3 - Low 低 | Non-critical warnings 非關鍵警告 | Review weekly 每週檢視 |

### Alerting Principles 告警原則
- Every alert should be **actionable** 每個告警都要能**採取行動**
- Avoid alert fatigue 避免告警疲勞: too many alerts = all alerts get ignored 太多告警 = 所有告警都被忽略
- Include context 附帶上下文: what failed, when, and where to look 什麼壞了、什麼時候、要看哪裡
- Route alerts to the right channel 告警送到對的頻道: Slack for P1-P2, PagerDuty for P0

## Logging 日誌

### ELK Stack
- **Elasticsearch**: search and analytics engine 搜尋與分析引擎
- **Logstash**: data collection and transformation 資料收集與轉換
- **Kibana**: visualization and dashboards 視覺化與儀表板

### Logging Best Practices 日誌最佳實踐
- Use structured logging (JSON) 使用結構化日誌
- Include correlation IDs to trace requests across systems 加入關聯 ID 以追蹤跨系統請求
- Log at appropriate levels 在適當層級記錄: DEBUG, INFO, WARNING, ERROR
- Don't log sensitive data 不要記錄敏感資料 (credentials, PII)

## Dashboards 儀表板

Build dashboards for 建立儀表板用於:
- Pipeline run history (success rate, duration trends) 管線執行歷史（成功率、耗時趨勢）
- Data freshness across key tables 關鍵表的資料新鮮度
- Infrastructure metrics 基礎設施指標
- Cost tracking 費用追蹤

Tools 工具: Grafana, Kibana, CloudWatch, Datadog

## Practice 練習

1. Add structured logging to an existing pipeline 在既有管線加入結構化日誌
2. Build a simple monitoring dashboard 建立簡單的監控儀表板
3. Set up failure notifications 設定失敗通知 (Slack, email, or Telegram)

## Key Takeaway 重點

> Monitor both pipeline health and data health. Good alerting means you find problems before your users do.
>
> 同時監控管線健康度和資料健康度。好的告警意味著你比使用者更早發現問題。
