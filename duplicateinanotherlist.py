# def cal(l1):
#     duplicates=[]
#     for i in l1:
#         if l1.count(i)>1 and i not in duplicates:
#             duplicates.append(i)
#     return duplicates
#
# l1=["1","4","a","a","1","5","6","7"]
# f= cal(l1)
# print(f)

def cal(l):
    count_list=[]
    dup_list=[]
    for i in l:
        if i not in count_list:
            count_list.append(i)
        else:
            dup_list.append(i)
    return dup_list

l=["1","9","5","3","4","4","9"]
result=cal(l)
print(result)




