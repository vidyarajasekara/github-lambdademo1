# my_tuple=(1,2,3)
# x,y,z,*rest=my_tuple
# print(x,y,z,rest)


# int1=10
# int2=6
# if int!=int2:
#     int2=++int1
#     print(int1-int2)

# my_tuple=(1,2,3,4,5)
# x,y,z,*rest=my_tuple
# print(x,y,z,rest)
#


s="aabbbc"
s1=set()
for i in s:
    if i not in s1:
     x=s.count(i)
     print(f"{i} the count in the string is:", x)
     s1.add(i)

#
#
# s1="hello"
# print(s1[::-1])

