# s = input("enter the string ")
# s1 = s.split()
# s2 = ""
# for i in s1:
#    s2 = s2 + i.capitalize()+" "
# print(s2)


s1=input("enter the text:")
s2=s1.split()
s3=""
print(type(s3))
# if u use capitalize in string entire thing will be upper case
# when u use in list capitalize the first letter in each word
for i in s2:
   s3=s3+i.capitalize()+" "
print(s3)
#
#
# def cal(m):
#    return m.title()
# m = input("enter the string")
# output = cal(m)
# print(output)
#
#
#
# m = input("enter the string")
# output = m.title()
# print(output)
#


s = input("enter the text to change each word first letter to uppercase:")
print(s.title())
# if u use capitalize in string directly entire thing will be upper case
# when u use in split string it will capitalize the first letter in each word
for i in s:
   print(i.capitalize(),end="")








