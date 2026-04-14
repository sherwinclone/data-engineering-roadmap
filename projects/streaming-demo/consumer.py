"""
Kafka Consumer Demo Kafka Consumer 示範

Consume messages from a Kafka topic and print them.
從 Kafka topic 消費訊息並印出。
"""

# from kafka import KafkaConsumer
# import json

# consumer = KafkaConsumer(
#     "demo-events",
#     bootstrap_servers=["localhost:9092"],
#     auto_offset_reset="earliest",
#     value_deserializer=lambda m: json.loads(m.decode("utf-8")),
# )

# print("Listening for messages... 等待訊息中...")
# for message in consumer:
#     print(f"Received 收到: {message.value}")

print("Install kafka-python and uncomment the code above to run.")
print("請安裝 kafka-python 並取消上方程式碼的註解以執行。")
