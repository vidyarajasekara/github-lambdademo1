
# def call1(m):
#     sp=m.split(" ")
#     r = [word.capitalize() for word in sp]
#     return" ".join(r)
#
# m = input("enter the text")
# call=call1(m)
# print((call))

def cal(m):
    v=m.split(" ")
    v1=[i.capitalize() for i in v]
    return" ".join(v1)

m=input("enter the text:")
result=cal(m)
print(result)