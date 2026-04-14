# Interview Prep 面試準備

What to expect and how to prepare for data engineering interviews.

數據工程師面試的準備方向。

## Common Interview Topics 常見面試主題

### SQL (Almost Always Asked 幾乎必考)
- Window functions 視窗函式: ROW_NUMBER, RANK, LAG, LEAD
- Self joins 自我 JOIN
- Recursive CTEs 遞迴 CTE
- Query optimization 查詢優化 (read EXPLAIN output 讀 EXPLAIN 輸出)
- Deduplication strategies 去重策略

### System Design 系統設計 (Mid-level and Above 中階以上)
- Design an ETL pipeline for a given scenario 設計一條 ETL 管線
- How to handle late-arriving data 如何處理遲到資料
- How to guarantee exactly-once processing 如何保證 exactly-once 處理
- Data warehouse layer design 資料倉儲分層設計
- Scaling a pipeline from 1M to 1B rows 管線從 100 萬筆擴展到 10 億筆

### Python
- Data processing scripts 資料處理腳本
- Error handling and retry logic 錯誤處理與重試邏輯
- Testing strategies 測試策略
- API integration patterns API 整合模式

### Behavioral Questions 行為題
- Describe the hardest data pipeline problem you solved 描述你解過最難的管線問題
- How do you handle upstream schema changes? 上游 schema 變更怎麼處理？
- How do you balance data quality vs delivery speed? 資料品質和交付速度如何取捨？
- Tell me about a time a pipeline failed in production 分享一次管線在正式環境失敗的經歷

## Resume Tips 履歷建議

### Do 該做的
- Quantify results 量化成果: "Processed 5M rows daily" 「每日處理 500 萬筆」, "Reduced query time from 30min to 2min" 「查詢時間從 30 分鐘降到 2 分鐘」
- Describe what **you** did, not what the team did 寫**你**做的，不是團隊做的
- Highlight tools you actually used 強調你真正用過的工具
- Link to GitHub projects 附上 GitHub 作品連結

### Don't 不該做的
- List 20 tool logos without context 列出 20 個 logo 沒有上下文
- Write only job responsibilities without outcomes 只寫職責不寫成果
- Use vague phrases like "familiar with big data" 用模糊字眼如「熟悉大數據」
- Lie about experience levels 謊報經驗程度

## Study Resources 學習資源

### Books 書籍
| Book 書名 | Level 程度 |
|------|-------|
| Fundamentals of Data Engineering (O'Reilly) | Beginner-Intermediate 入門到中階 |
| Designing Data-Intensive Applications | Intermediate-Advanced 中階到進階 |
| The Data Warehouse Toolkit (Kimball) | Intermediate 中階 |

### Free Courses 免費課程
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)

### Certifications 證照 (Optional, but Can Help 非必要，但有加分)
- GCP Professional Data Engineer
- Databricks Certified Data Engineer
- AWS Data Analytics Specialty

### Communities 社群
- Data Engineering Taiwan (Facebook)
- DataTalks.Club (Slack)
- dbt Community (Slack)

## Key Takeaway 重點

> SQL is always tested. System design matters at mid-level+. A strong portfolio with working projects speaks louder than certifications.
>
> SQL 一定會考。中階以上看系統設計。能跑的作品集比證照更有說服力。
