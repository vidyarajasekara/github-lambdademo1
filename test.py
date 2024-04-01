# a=["a","e","i","o","u"]
# b=["e","o","s"]
# count=0
# for i in a:
#     for j in b:
#         if i==j:
#             count+=1
#
# print(count)
# ..........
# sqrt
# import math
# a=100
# result=math.sqrt(a)
# print(result)
# # square ** exponential operation
# a=5
# result=a**2
# print(result)
# b=10
# result=b**3
# print(result)

# ..................................
from pyspark.sql import SparkSession
data={"name":["alice","bob","charlie","diana"],
      "age":[25,40,35,28],
      "gender":["female","male","male","female"]}
# i=data["name"].index("charlie")
# a=data["age"][i]
# print("charlie age is ",a)
for index,gen in enumerate(data["gender"]):
     if gen == "female":
          i=data["name"][index]
          print("female names are:",i)


# b= data["gender"].index("female")
# print(b)


# ...................................

# myfamily={
#     "child1":{"name":"shivy","age":3},
#     "child2":{"name":"sachchith","age":10}}
# child2_age=myfamily["child2"]["age"]
# print(child2_age)
# # .....................................
# from pyspark.sql import SparkSession
# spark= SparkSession.builder.appName("demo").getOrCreate()
# client_data = {
#     "client_id": 12345,
#     "name": "John Doe",
#     "email": "john.doe@example.com",
#     "phone": "123-456-7890",
#     "address": {
#         "street": "123 Main St",
#         "city": "fremont",
#         "state": "CA",
#         "zipcode": "12345"
#     },
#     "orders": [
#         {"order_id": 1, "product": "Widget A", "quantity": 2, "price": 10.99},
#         {"order_id": 2, "product": "Widget B", "quantity": 1, "price": 24.99},
#         {"order_id": 3, "product": "Widget C", "quantity": 3, "price": 15.99}
#     ]
# }
# print("name is:",client_data["name"])
# print("address is:",client_data["address"]["city"])
# print("email is:",client_data["email"])
# for order in client_data["orders"]:
#    print(order["order_id"])
#

# .........................................
from pyspark.sql import SparkSession
spark= SparkSession.builder.appName("demo").getOrCreate()
# path=spark.read.csv(r"C:\rawdata\clientdata.csv")
rawdata =spark.read.format("csv")\
           .option("header", "true")\
           .load(r"C:\rawdata\clientdata.csv")
rawdata.show()
name=rawdata.select("name")
print(name)
# ........................................
# from pyspark.sql import SparkSession
# from pyspark.sql.types import StructType, StringType, IntegerType, FloatType, StructField
#
# spark = SparkSession.builder.appName("Client Raw Data").getOrCreate()
# schema = StructType([
#     StructField("_c0", IntegerType(), True),
#     StructField("_c1", StringType(), True),
#     StructField("_c2", StringType(), True),
#     StructField("_c3", StringType(), True),
#     StructField("_c4", StringType(), True),
#     StructField("_c5", StringType(), True),
#     StructField("_c6", StringType(), True),
#     StructField("_c7", StringType(), True),
#     StructField("_c8", IntegerType(), True),
#     StructField("_c9", StringType(), True),
#     StructField("_c10", IntegerType(), True),
#     StructField("_c11", FloatType(), True)
# ])
#
# data = [
#     (12345, "John", "john.doe@example.com", "183-414-7890", "122 Main St", "fremont", "CA", "94535", 1, "Widget A", 2, 10.99),
#     (12346, "Doe", "doe@example.com", "123-456-7145", "123 Main St", "sanjose", "CA", "94536", 2, "Widget B", 1, 24.99),
#     (12347, "Jo", "jo.doe@example.com", "111-456-7890", "124 Main St", "sfo", "CA", "94537", 3, "Widget C", 3, 15.99)
# ]
# df = spark.createDataFrame(data, schema=schema)
# df.show()
# spark.stop()
# ................................................................................
# FR873FR744FR513FR”, remove all the Alphabets and keep the numeric value alone.
# txt="FR873FR744FR513FR"
# char=[]
# for x in txt:
#     if x.isnumeric():
#         char.append(x)
#     else:
#         continue
# print(char)
# print("".join(char))
