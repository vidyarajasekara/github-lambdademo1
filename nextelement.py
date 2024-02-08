# li = [None, 2, 3,None,None, 5,None]
# for index,value in enumerate(li):
#     if value is None and index+1<len(li):
#         next=li[index+1]
#         if isinstance(next,int):
#             li[index]=next
#         else:
#             if value is None and index + 1 < len(li):
#                 next = li[index + 2]
#                 if isinstance(next, int):
#                     li[index] = next
# print(li)

#
# txt="the price is {:.2f} dollars"
# price=40
# print(txt.format(price))



x="hello"
if not type(x) is int:
    raise TypeError("only integers are allowed")




