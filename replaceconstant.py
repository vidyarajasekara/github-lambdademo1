from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Create a SparkSession
spark = SparkSession.builder \
    .appName("ReplaceNullsWithConstant") \
    .getOrCreate()

# Create a sample DataFrame
data = [("John", 30),
        ("Anna", None),
        ("Smith", 25),
        (None, 28)]

columns = ["Name", "Age"]
df = spark.createDataFrame(data, columns)

# Specify the constant value
constant_value = "Unknown"

df_filled = df.fillna(constant_value)

df_filled.show()