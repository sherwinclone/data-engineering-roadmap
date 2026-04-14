# Streaming 串流處理

When batch isn't fast enough, you need streaming. But only when you truly need it.

當 Batch 不夠快，你需要 Streaming。但只在你真正需要的時候。

## When to Use Streaming 什麼時候需要串流

- Real-time fraud detection / risk monitoring 即時風控 / 詐騙偵測
- Live dashboards and alerting 即時儀表板與告警
- Event-driven architectures 事件驅動架構
- Latency requirements under seconds 延遲要求在秒級以內

> If batch can solve the problem, use batch. Streaming is significantly harder to debug, maintain, and operate.
>
> 能 Batch 就 Batch。Streaming 的除錯、維運、狀態管理都比 Batch 複雜很多。

## Kafka

Apache Kafka is the most widely used event streaming platform.

Apache Kafka 是最廣泛使用的事件串流平台。

### Core Concepts 核心概念
- **Producer**: sends messages to a topic 發送訊息到 topic
- **Consumer**: reads messages from a topic 從 topic 讀取訊息
- **Topic**: a category/feed of messages 訊息分類
- **Partition**: unit of parallelism within a topic 平行處理單位
- **Consumer Group**: distributes partitions across consumers for load balancing 負載均衡
- **Offset**: tracks consumer progress within a partition 消費進度

### Delivery Guarantees 傳遞保證
| Guarantee 保證 | Meaning 意義 | Trade-off 取捨 |
|-----------|---------|-----------|
| At-most-once 最多一次 | May lose messages 可能丟失訊息 | Fastest 最快 |
| At-least-once 至少一次 | May duplicate messages 可能重複訊息 | Most common 最常用 |
| Exactly-once 恰好一次 | No loss, no duplicates 不丟失、不重複 | Hardest 最難 |

### Important Concepts 重要觀念
- Partition count = max parallelism for consumers 分區數 = 最大消費並行度
- Retention 保留: how long messages are kept 訊息保留多久 (default 7 days 預設 7 天)
- Schema Registry: manage message formats 管理訊息格式 (Avro, Protobuf)
- Compaction 壓縮: keep only the latest value per key 每個 key 只保留最新值

## Spark Structured Streaming

- Built on Spark SQL engine 基於 Spark SQL 引擎
- Micro-batch or continuous processing 微批次或連續處理
- Watermarks handle late-arriving data Watermark 處理遲到資料
- API is very similar to batch Spark code API 與 batch Spark 程式碼高度相似

```python
df = (
    spark.readStream
    .format("kafka")
    .option("subscribe", "events")
    .load()
)

result = df.groupBy(window("timestamp", "5 minutes")).count()

result.writeStream.format("console").start()
```

## Flink (Advanced 進階)

- True record-by-record processing (not micro-batch) 真正逐筆處理（非微批次）
- Strong state management 強大的狀態管理
- Complex Event Processing (CEP) 複雜事件處理
- Steeper learning curve 學習曲線較陡

## Practice 練習

See 參見 [projects/streaming-demo](../projects/streaming-demo/).

1. Run Kafka locally with Docker 用 Docker 在本地跑 Kafka
2. Write a producer that generates fake events 寫一個產生假資料的 producer
3. Write a consumer that aggregates events in real time 寫一個即時聚合的 consumer
4. Try Spark Structured Streaming with a Kafka source 試試 Spark Structured Streaming 搭配 Kafka

## Key Takeaway 重點

> Streaming adds operational complexity. Make sure you actually need real-time before choosing it. Most pipelines work fine with batch.
>
> Streaming 增加維運複雜度。確定真的需要即時再選它。大部分管線用 Batch 就夠了。
