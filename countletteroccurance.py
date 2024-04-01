# a = "vidyarajasekaran"
# b = {}
# for i in a:
#    count=b.get(i,0)
#    count+=1
#    b[i]=count
# print(b)



# list,set,dict
# a="vidyarajasekaran"
# # converting string to list
# b=list(a)
# print(b)
# # converting list to set
# c=set(b)
# print(c)
# # converting set to list
# d=list(c)
# print(d)
# # dict to store key and value pair
# e={}
# for i in d:
#     # assigning key value to 0 in dict
#     e[i] = 0
#     for j in b:
#         if i == j:
#             e[i] = e[i]+1
# print(e)


# using count() method
# a="vidyarajasekaran"
# for i in a:
#     print(f'{i} occurance is :',{a.count(i)})


v="shivysenthamaraikannan"
for i in v:
    print(f'{i} occurance is:',{v.count(i)})


# # doubt:not working list allow duplicates
# a = "vidyarajasekaran"
# b = list(a)
# print(b)
# for i in b:
#     count = 0
#     for j in b:
#         if i == j:
#             count += 1
#     b[b.index(i)]= count
# print(b)
#
#

