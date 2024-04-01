# num1 = 5
# num2 = 10
# sum = num1+num2
# print("num1","and","num2",sum)
import spark
# n1 = 1
# n2 = 2
# sum = n1+n2
# print("sum of n1 and n2 is:",sum)

#
# a = "vidya"
# a1=a[::-1]
# print(a1)
#
# #
# # def cal(a):
# #   a.split()
# #   b=[]
# #   j=4
# #   for i in a:
# #     b.append(a[j])
# #     j-=1
# #     c="".join(b)
# #   return c
# #
# # a="vidya"
# # result=cal(a)
# # print(result)
# #

# from pyspark.sql import SparkSession
# from pyspark.sql.functions import col
# # driver
#
# spark = SparkSession.builder.appName("test").getOrCreate()
#
# data = [('Alice', 50000),
#         ('Bob', 60000),
#         ('Charlie', 45000),
#         ('David', 70000),
#         ('Eva', 55000),
#         ('Frank', 60000)]
# # cluster
# columns = ["Name", "Salary"]
# df1 = spark.createDataFrame(data,columns)
#
# # mind calculation DAG  --logical
# maximum = df1.agg({"Salary": "max"})
#
# # real worker executor start
# print("Maximum Salary:")
# maximum.show()