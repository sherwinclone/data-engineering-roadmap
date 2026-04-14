# 06 - 串流處理

> 當 Batch 不夠快，你需要 Streaming。

## 學習目標

- [ ] 理解 Message Queue 與 Event Streaming 的差異
- [ ] 能操作 Kafka 的基本功能
- [ ] 理解 Spark Structured Streaming 的運作方式
- [ ] 知道何時該用 Streaming、何時不該

## 什麼時候需要 Streaming？

- 即時風控 / 詐騙偵測
- 即時 Dashboard / 監控
- 事件驅動架構（Event-Driven）
- 延遲要求在秒級以內

> 再次強調：能 Batch 就 Batch。Streaming 的除錯、維運、狀態管理都比 Batch 複雜很多。

## Kafka

### 核心概念
- **Producer**：發送訊息
- **Consumer**：接收訊息
- **Topic**：訊息分類
- **Partition**：平行處理單位
- **Consumer Group**：負載均衡
- **Offset**：消費進度

### 重要觀念
- At-least-once vs At-most-once vs Exactly-once
- Partition 數量決定最大並行度
- Retention 設定：資料保留多久
- Schema Registry：管理訊息格式（Avro / Protobuf）

## Spark Structured Streaming

- 基於 Spark SQL 引擎
- 微批次（micro-batch）或連續處理
- 支援 Watermark 處理 late data
- 與 Batch Spark 程式碼高度相似

## Flink（進階）

- 真正的逐筆處理（非微批次）
- 狀態管理能力強
- 適合複雜事件處理（CEP）
- 學習曲線較陡

## 練習

1. 用 Docker 架 Kafka，寫 Producer 和 Consumer
2. 模擬即時資料流：產生假資料 → Kafka → Consumer 聚合 → 輸出
3. 用 Spark Structured Streaming 讀取 Kafka topic 做 window aggregation
