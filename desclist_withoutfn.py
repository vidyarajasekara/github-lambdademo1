# li=[5,1,2,4,3]
# # print(sorted(li,reverse=True))
# # ..............without builtinfn.descending.......................
# m=max(li)
# print(m)
# li1=[]
# li1.append(m)
# for i in range(1,len(li)):
#     m-=1
#     if m in li:
#         li1.append(m)
#     else:
#         break
# print(li1)
# ................max function without build_in.................
li=[5,1,2,4,3]
max_num=li[0]
for i in li[1:]:
  if max_num<i:
      max_num=i
  else:
      continue
print(max_num)




