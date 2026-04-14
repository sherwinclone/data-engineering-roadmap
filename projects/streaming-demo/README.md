# Streaming Demo 串流示範

A simple Kafka producer and consumer demo.
簡單的 Kafka producer 與 consumer 示範。

## Goals 目標

- Run Kafka locally with Docker 使用 Docker 在本地執行 Kafka
- Write a producer that generates events 撰寫產生事件的 producer
- Write a consumer that processes events 撰寫處理事件的 consumer

## Setup 安裝

```bash
# Start Kafka with Docker Compose
# 使用 Docker Compose 啟動 Kafka
docker compose up -d
```

## Steps 步驟

1. Start Kafka and create a topic 啟動 Kafka 並建立 topic
2. Run the producer to send events 執行 producer 發送事件
3. Run the consumer to process events 執行 consumer 處理事件
4. Observe real-time processing 觀察即時處理

## Tech Stack 技術棧

- Apache Kafka
- kafka-python or confluent-kafka
- Docker Compose
