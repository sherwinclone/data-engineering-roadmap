# Data Quality 資料品質

A pipeline that runs successfully but produces wrong data is worse than one that fails loudly.

跑成功但產出錯誤資料的管線，比大聲失敗的管線更糟。

## Quality Dimensions 品質維度

| Dimension 維度 | What to Check 檢查什麼 |
|-----------|---------------|
| Completeness 完整性 | Missing values, missing rows 缺值、缺 row |
| Uniqueness 唯一性 | Duplicate records 重複資料 |
| Timeliness 時效性 | Is the data fresh enough? 資料夠新嗎？ |
| Accuracy 正確性 | Are values reasonable? 數值合理嗎？ |
| Consistency 一致性 | Do values match across tables/systems? 跨表/跨系統是否一致？ |

## Testing Strategies 測試策略

### Schema Tests 結構測試
- Expected columns exist 預期的欄位存在
- Data types are correct 資料型別正確
- NOT NULL constraints on critical fields 關鍵欄位有 NOT NULL 約束

### Volume Tests 量體測試
- Row count within expected range 筆數在預期範圍內
- Compare source count vs target count 比較來源與目標筆數
- Alert on sudden drops (zero rows = something broke) 突然歸零就是壞了

### Value Tests 值測試
- No negative values where impossible 不可能的地方沒有負值 (e.g., age, price)
- Values within expected ranges 值在預期範圍內
- Referential integrity 參照完整性: foreign keys exist in parent table 外鍵存在於父表

### Freshness Tests 新鮮度測試
- Latest timestamp in the table is recent enough 表中最新時間戳夠近
- Partition for today exists 今天的分區存在

## Tools 工具

| Tool 工具 | Approach 方式 |
|------|----------|
| Great Expectations | Python-based, rich rule definitions, auto docs Python 為基底，豐富的規則定義 |
| dbt tests | Built-in 內建: unique, not_null, accepted_values, relationships |
| Soda | YAML-based check definitions YAML 定義檢查規則 |
| Elementary | dbt-native data observability dbt 原生資料可觀測性 |
| Monte Carlo | Commercial data observability platform 商業資料可觀測性平台 |

## Building a Data Quality Framework 建立資料品質框架

1. Start with the most critical tables 從最重要的表開始
2. Add basic checks: not null, unique keys, row counts 加入基本檢查
3. Set up alerting for failures 設定失敗告警
4. Gradually expand coverage 逐步擴大覆蓋
5. Document expectations and ownership 記錄預期標準和負責人

## Practice 練習

1. Define quality checks for a sample table using Great Expectations or dbt tests 用 Great Expectations 或 dbt tests 定義品質檢查
2. Add a row count validation step to an existing pipeline 在既有管線加入筆數驗證
3. Set up alerts for quality failures 設定品質失敗告警

## Key Takeaway 重點

> Test your data like you test your code. Start simple, focus on critical tables, and make failures visible.
>
> 像測試程式碼一樣測試資料。從簡單開始，聚焦關鍵表，讓失敗看得見。
