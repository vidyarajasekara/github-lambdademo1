# str1="abbbaaaaaaccdaaab"
# # o/p=ab3a6c2da3b
# i=0
# count=0
# res=[]
# while i<len(str1):
#     count=1
#     while i+1<len(str1) and str1[i]==str1[i+1]:
#         count+=1
#         i+=1
#     if count==1:
#      res.append(str1[i])
#      i+=1
#     elif count>1:
#      res.append(str1[i]+str(count))
#      i+=1
# res1="".join(res)
# print(res1)




def func(str1="abbbaaaaaaccdaaab"):
    i = 0
    count = 0
    res = []
    while i < len(str1):
        count = 1
        while i + 1 < len(str1) and str1[i] == str1[i + 1]:
            count += 1
            i += 1
        if count == 1:
            res.append(str1[i])
            i += 1
        elif count > 1:
            res.append(str1[i] + str(count))
            i += 1
    res1 = "".join(res)
    return res1
# str1="abbbaaaaaaccdaaab"
result=func()
print(result)



