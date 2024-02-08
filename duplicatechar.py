# s = input("enter the string")
# s1 = ""
# for i in s:
#     if i not in s1:
#         s1 = s1+i
# print(s1)

# t="sachchith"
# d={}
# for i in t:
#     if i not in d:
#         d[i]=1
#     else:
#         d[i]+=1
# #
# if all(value<2 for value in d.values()):
#     print(d)

# doubt
# t = "sachchith"
# d = {}
#
# # Counting occurrences of each character
# for i in t:
#     if i not in d:
#         d[i] = 1
#     else:
#         d[i] += 1
# print(d)
# # Checking if all values are less than 2
# r=d.values()
# res=(key for key value>=2 for value in r)


t="viidya"
dup_t1=[]
char_encounter=[]
for char in t:
    if char not in char_encounter:
        char_encounter.append(char)
    else:
        dup_t1.append(char)
print(dup_t1)

