"""
Spark Demo Job Spark 示範作業

Read CSV, transform, write as Parquet.
讀取 CSV、轉換、輸出為 Parquet。
"""

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, sum as spark_sum

spark = SparkSession.builder.appName("spark-demo").master("local[*]").getOrCreate()

# Read 讀取
# df = spark.read.option("header", True).option("inferSchema", True).csv("data/input.csv")

# Transform 轉換
# result = (
#     df.filter(col("status") == "completed")
#     .groupBy("category")
#     .agg(
#         count("*").alias("total_orders"),
#         spark_sum("amount").alias("total_revenue"),
#     )
# )

# Write 寫入
# result.write.mode("overwrite").parquet("output/result.parquet")

# spark.stop()

print("Uncomment the code above and provide input data to run.")
print("請取消上方程式碼的註解並提供輸入資料以執行。")
