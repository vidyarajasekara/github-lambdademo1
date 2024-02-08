
# def f(a,b):
#     c=[]
#     for i in a:
#         if i in b and i not in c:
#             c.append(i)
#     return c
#
# a = [1,2,8,4,7,3]
# b = [2,3,5,0,6,1]
# res = f(a,b)
# print(res)

def cal(a,b):
    c=[]
    for i in a:
        if i in b and i not in c:
            c.append(i)
    return c

a=[7,3,9,1,4,]
b=[4,7,2,8.3]
result=cal(a,b)
print(result)