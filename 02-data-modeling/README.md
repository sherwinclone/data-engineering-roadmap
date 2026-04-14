# 02 - 資料建模

> 資料建模決定了你的資料倉儲好不好用、查詢快不快。

## 學習目標

- [ ] 理解 Normalization 與 Denormalization 的取捨
- [ ] 能設計 Star Schema / Snowflake Schema
- [ ] 理解 SCD（Slowly Changing Dimension）的各種類型
- [ ] 知道 Data Vault 的基本概念

## Normalization

- 1NF → 2NF → 3NF → BCNF
- OLTP 系統通常正規化到 3NF
- 目的：減少資料冗餘、維護一致性

## Dimensional Modeling（維度建模）

### Star Schema
- Fact Table（事實表）：度量值、外鍵
- Dimension Table（維度表）：描述性屬性
- 查詢直覺、效能好，OLAP 首選

### Snowflake Schema
- Dimension 再正規化
- 節省空間，但 JOIN 變多

### 設計原則
- Grain（粒度）先決定：一筆 row 代表什麼？
- Fact 分類：Transaction / Periodic Snapshot / Accumulating
- Conformed Dimension：跨 Fact 共用的維度

## SCD（Slowly Changing Dimension）

| 類型 | 做法 | 適用場景 |
|------|------|----------|
| Type 0 | 不更新 | 固定屬性（生日） |
| Type 1 | 直接覆蓋 | 不需要歷史（修正錯誤） |
| Type 2 | 新增一筆 + 有效期間 | 需要追蹤歷史變化 |
| Type 3 | 加欄位存前一個值 | 只需要前後對比 |

## Data Vault（進階）

- Hub：業務主鍵
- Link：關聯
- Satellite：屬性與歷史
- 適合大型企業、多來源整合

## 練習

1. 為一個電商場景設計 Star Schema（訂單 Fact + 客戶/產品/時間 Dimension）
2. 實作 SCD Type 2：模擬客戶地址變更，保留歷史
