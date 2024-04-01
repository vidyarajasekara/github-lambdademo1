# def fun():
#     # print("hello")
#     return "hello1"
#     # print("everyone")
# result=fun()
# print(result)
# .....................................................................
# def fun(name):
#     print(f"my name is,{name}")
#     # return (f"my name is,{name}")
# result=fun("shivy")
# print(result)
# ....................................................
# def fun(a,b):
#     return a+b
# result=fun(5,10)
# print(result)
# ................................................................
# def fun(value=100):
#     print("this is worth rs {}".format(value))
#     return "this is worth rs {}".format(value)
# result=fun()
# print(result)
# fun()
# ...................................................
# global_var=25
# def cal():
#     local_var=50
#     # print(global_var+local_var)
#     return global_var+local_var
# # cal()
# res=cal()
# print(res)
# ......................................................................
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         return n*fact(n-1)
# res=fact(5)
# print(res)
# .....................................................................
# cal=lambda x,y:x/y
# result=cal(100,5)
# print(result)
# # .............................................
def fun1(f,x):
    return f(x)
def f(x):
    return x**3
res=fun1(f,3)
print(res)