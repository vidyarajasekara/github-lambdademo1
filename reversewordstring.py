# s="hai welcome"
# s1=[]
# for i in s:
#     s1.append(i)
# print(s1)
# print("".join(s1))
# print(type(s1))
# s2=s1[::-1]
# print(s2)
# print("".join(s2))

# reversestring
# def cal(s1):
#     v=""
#     s2=[]
#     for i in s1:
#         v = i[::-1]
#         s2.append(v)
#
#     return s2
#
# s="kkl world"
# s1=s.split()
# print(type(s1))
# res=cal(s1)
# print(res)
# print(" ".join(res))


txt="hello world"
a=txt.split(" ")
txt1=[]
for word in a:
    rev_word=word[::-1]
    txt1.append(rev_word)
print(txt1)
print(" ".join(txt1))






