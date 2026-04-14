# Spark

Apache Spark is the standard for large-scale distributed data processing.

Apache Spark 是大規模分散式資料處理的標準。

## When Do You Need Spark? 什麼時候需要 Spark？

- Data is too large for a single machine (pandas can't handle it) 資料太大單機處理不了（pandas 吃不下）
- You need distributed processing across a cluster 需要分散式跨叢集處理
- Processing takes too long on a single node 單機處理太慢
- Rough threshold 粗略門檻: when data exceeds ~10 GB, consider Spark 資料超過約 10 GB 就考慮用 Spark

## Core Concepts 核心概念

- **Driver**: the process that runs your main program 執行主程式的程序
- **Executor**: worker processes that run tasks 執行任務的工作程序
- **RDD**: Resilient Distributed Dataset (low-level API, rarely used directly) 低階 API，很少直接使用
- **DataFrame**: structured API (recommended) 結構化 API（推薦使用）
- **Transformation 轉換**: lazy operation — not executed until an action 延遲操作，直到 action 才執行
- **Action 動作**: triggers execution 觸發執行 (count, collect, write)
- **Partition 分區**: unit of parallelism 平行處理的單位

## PySpark Basics 基礎

```python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum

spark = SparkSession.builder.appName("example").getOrCreate()

df = spark.read.parquet("s3://bucket/data/")

result = (
    df.filter(col("status") == "completed")
    .groupBy("category")
    .agg(
        count("*").alias("total_orders"),
        sum("amount").alias("total_revenue")
    )
)

result.write.mode("overwrite").parquet("s3://bucket/output/")
```

## Performance Tips 效能提示

- **Partitioning 分區**: choose partition count based on data size (~128 MB per partition) 依資料大小選分區數
- **Avoid collect() 避免 collect()**: brings all data to the driver 會把所有資料拉到 driver
- **Broadcast joins 廣播 JOIN**: for joining a large table with a small lookup table 大表 JOIN 小表時使用
- **Cache wisely 聰明快取**: cache DataFrames you reuse, but don't over-cache 快取會重複使用的 DataFrame
- **Avoid UDFs when possible 盡量避免 UDF**: built-in functions are faster 內建函式更快（Catalyst 優化器）
- **Monitor the Spark UI 監控 Spark UI**: check for skewed partitions and shuffle overhead 檢查資料傾斜和 shuffle 開銷

## File Formats 檔案格式

| Format 格式 | Best For 適合 |
|--------|----------|
| Parquet | Columnar, default choice for analytics 列式，分析首選 |
| Delta | Parquet + ACID + time travel (Databricks) |
| ORC | Hadoop ecosystem Hadoop 生態系 |
| Avro | Row-based, good for streaming/Kafka 行式，適合串流 |
| CSV/JSON | Interchange only, not for production 交換用，不適合正式環境 |

## Running Spark 執行 Spark

| Environment 環境 | Notes 備註 |
|-------------|-------|
| Local 本地 | `SparkSession.builder.master("local[*]")` |
| Databricks | Managed, notebook-based, Delta Lake native 托管、Notebook、原生 Delta Lake |
| EMR (AWS) | Managed Hadoop/Spark clusters 托管叢集 |
| Dataproc (GCP) | Managed Hadoop/Spark clusters 托管叢集 |

## Practice 練習

See 參見 [projects/spark-demo](../projects/spark-demo/).

1. Read a large CSV, transform it, write as Parquet 讀取大 CSV、轉換、寫出 Parquet
2. Implement a group-by aggregation with window functions 用 window function 做分組聚合
3. Compare performance with different partition counts 比較不同分區數的效能
4. Use the Spark UI to identify a bottleneck 用 Spark UI 找出瓶頸

## Key Takeaway 重點

> Spark is powerful but not always necessary. Use it when data doesn't fit on one machine. Learn the DataFrame API and understand partitioning.
>
> Spark 很強大但不一定需要。資料放不進單機時才用。學好 DataFrame API、搞懂分區。
