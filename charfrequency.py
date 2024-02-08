#
# x = input("enter the string here:")
# frequency={}
# for y in x:
#     if y in frequency:
#         frequency[y]+=1
#     else:
#         frequency[y]=1
# print(frequency)


txt="hai welcome"
d={}
for i in txt:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)