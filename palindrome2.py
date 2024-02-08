#
# a = "a man a plan a canal panama"
# b = a.split(" ")
# # split is a string function but once u apply split txt will change into list
# print(type(b))
# # c modified given input
# c = "".join(b)
# print(c)
# # d reversed input
# d = c[::-1]
# print(d)
# if c == d:
#      print(f"{a} is a palindrome")
# else:
#      print(f"{a} is not a palindrome")

a = "a man a plan a canal panama"
b=a.split(" ")
c="".join(b)
print(c)
rev_str=c[::-1]
if c== rev_str:
     print(f"{a} its a palindrome")
else:
     print(f"{a} its not a palindrome")











