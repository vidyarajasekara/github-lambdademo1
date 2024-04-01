import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from pyspark.sql.window import Window
from pyspark.sql.functions import *
from pyspark.sql.types import *
from pyspark.sql import functions as f
from pyspark.sql.types import StringType, IntegerType
from pyspark.sql.functions import col
from pyspark.sql.functions import udf
from pyspark.sql.functions import expr
from pyspark.sql.types import StructType, StructField, StringType, IntegerType, LongType
from pyspark import *


# Create spark session
# spark = SparkSession.builder \
#     .master("local[1]") \
#     .appName("SparkByExamples.com") \
#     .getOrCreate()
#
spark = SparkSession.builder.appName(
    'Read CSV File into DataFrame') \
    .config("spark.sql.legacy.timeParserPolicy", "LEGACY") \
    .config("spark.sql.caseSensitive", "True") \
    .getOrCreate()

path=r"C:\rawdata\data1.json"
df = spark.read.json(path)
df.show()
print(df.columns)
print(len(df.columns))

df1=df.withColumn("as_date",from_unixtime(unix_timestamp(col("ITEM_DATE"),'dd-MMM-yy hh:mm:ss aa'),'yyyy-MM-dd HH:mm:ss aa'))
df1.show()

def getInterval(time):
    start = int(time.split(":")[0])
    return str(start)+"-"+str(start+1)
getIntervalUdf = udf(getInterval,StringType())

df2=df1.withColumn("date",from_unixtime(unix_timestamp(col('as_date'),'yyyy-MM-dd HH:mm:ss aa'),'yyyy-MM-dd'))\
    .withColumn("time",from_unixtime(unix_timestamp(col('as_date'),'yyyy-MM-dd HH:mm:ss aa'),'HH:mm:ss aa'))\
    .withColumn("Interval",getIntervalUdf("time"))\
    .withColumn("account_id", col('ACCOUNT_ID').cast(IntegerType()))
df2.show()

item_df1 = df2.groupBy('date','account_id','Interval').agg(count('*').alias('msg_per_hr'))
item_df1.show()

filtered_df1 = item_df1.where("account_id = 412679696")
filtered_df1 = item_df1.where(col("account_id").isin([412679696, 418822087]))
filtered_df1.show()

df3 = item_df1.withColumn("year", year(col('date').cast("timestamp")))\
    .withColumn('month', month(col('date').cast('timestamp')))\
    .withColumn("day", dayofmonth(col('date').cast('timestamp')))\
    .withColumn("hour", split(col('Interval'),'-')[0].cast(IntegerType()))\
    .withColumn("hour_interval", col('Interval'))\
    .withColumn("dayname", date_format(df2.date, "EEEE"))

df3.show(truncate=False)
