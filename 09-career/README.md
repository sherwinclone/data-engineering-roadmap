# 09 - 職涯發展

> 技術學得夠多了，來聊聊怎麼找到好工作。

## 學習目標

- [ ] 了解台灣 DE 市場現況
- [ ] 知道面試常考什麼
- [ ] 能寫出有效的履歷

## 台灣市場觀察

### 職缺名稱（可能叫不同名字，但做類似的事）
- Data Engineer
- ETL Developer
- 資料工程師
- BI Engineer
- Analytics Engineer

### 常見技術要求
- Python + SQL（幾乎每家都要）
- 至少一個雲端平台
- Airflow 或類似排程工具
- Spark（大公司 / 資料量大的才會要）

### 薪資範圍（2024 參考，年薪）
- Junior（0-2 年）：60-80 萬
- Mid（2-5 年）：80-120 萬
- Senior（5+ 年）：120-180 萬
- 博弈 / 金融 / 外商通常高於平均

> 以上為粗估，實際依公司、技能、談判能力而異。

## 面試準備

### SQL 題（幾乎必考）
- Window Function 應用
- 自我 JOIN
- 遞迴 CTE
- 效能調校（看 EXPLAIN）

### 系統設計題（Mid 以上）
- 設計一條 ETL pipeline
- 如何處理 late arriving data
- 如何保證 exactly-once processing
- 資料倉儲分層設計

### 行為題
- 遇過最難的 data pipeline 問題？怎麼解的？
- 如何處理上游資料突然變 schema？
- 如何在資料品質和交付速度之間取捨？

## 履歷建議

### Do
- 量化成果：「處理日均 500 萬筆資料」「將查詢時間從 30 分鐘降到 2 分鐘」
- 寫你實際做的，不是團隊做的
- GitHub 有作品加很多分

### Don't
- 不要列一堆 logo（「精通 20 種工具」）
- 不要只寫職責，要寫成果
- 不要寫「熟悉大數據」這種空話

## 持續成長

### 推薦資源
- [Fundamentals of Data Engineering](https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/)（O'Reilly）
- [Data Engineering Zoomcamp](https://github.com/DataTalksClub/data-engineering-zoomcamp)（免費課程）
- [Seattle Data Guy](https://www.youtube.com/@SeattleDataGuy)（YouTube）

### 社群
- Data Engineering Taiwan（Facebook）
- DataTalks.Club（Slack）
- dbt Community（Slack）

## 最後

技術棧會一直變，但核心觀念不太變。把基礎打好，學新工具就是換一個 API 而已。
