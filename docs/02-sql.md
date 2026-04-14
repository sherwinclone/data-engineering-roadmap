# SQL

SQL is the most important skill for a Data Engineer. You will use it every day.

SQL 是數據工程師最重要的技能，每天都會用到。

## What to Learn 學習內容

### Fundamentals 基礎
- SELECT, FROM, WHERE, ORDER BY, LIMIT
- INSERT, UPDATE, DELETE
- JOINs: INNER, LEFT, RIGHT, FULL OUTER, CROSS
- GROUP BY, HAVING
- Aggregate functions 聚合函式: COUNT, SUM, AVG, MIN, MAX
- DISTINCT, UNION, INTERSECT, EXCEPT

### Intermediate 中階
- Subqueries and correlated subqueries 子查詢與相關子查詢
- Common Table Expressions (CTE) 通用表格運算式
- CASE WHEN expressions
- Date/time functions and timezone handling 日期/時間函式與時區處理
- String functions 字串函式
- NULL handling 空值處理: COALESCE, NULLIF, IS NULL

### Advanced 進階
- Window functions 視窗函式: ROW_NUMBER, RANK, DENSE_RANK, LAG, LEAD, NTILE
- Window frames 視窗範圍: ROWS BETWEEN, RANGE BETWEEN
- Recursive CTEs 遞迴 CTE
- PIVOT / UNPIVOT
- Query performance 查詢效能: EXPLAIN / EXPLAIN ANALYZE
- Index design and usage patterns 索引設計與使用模式

## Performance Essentials 效能要點

### Indexing 索引
- B-Tree indexes (default, most common) B-Tree 索引（預設，最常用）
- When to create indexes: columns in WHERE, JOIN, ORDER BY 何時建索引：WHERE、JOIN、ORDER BY 中的欄位
- Composite indexes: column order matters 複合索引：欄位順序很重要
- Don't over-index: each index slows down writes 不要過度建索引：每個索引都會拖慢寫入

### Query Optimization 查詢優化
- Read the execution plan before optimizing 優化前先看執行計畫
- Avoid SELECT * in production queries 正式查詢避免 SELECT *
- Filter early, join late 先篩選，後 JOIN
- Use appropriate data types 使用適當的資料型別
- Partition large tables by date or key 大表依日期或 key 分區

## Practice Resources 練習資源

- [LeetCode SQL](https://leetcode.com/problemset/database/)
- [HackerRank SQL](https://www.hackerrank.com/domains/sql)
- [SQLZoo](https://sqlzoo.net/)
- [Mode SQL Tutorial](https://mode.com/sql-tutorial/)

## Key Takeaway 重點

> Write SQL every day. Read execution plans. Understand why a query is slow before adding indexes.
>
> 每天寫 SQL。讀執行計畫。在加索引之前，先搞懂查詢為什麼慢。
