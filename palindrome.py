# expression st[::-1] string slicing with a step of -1
# def palindrome(st):
#  rev_st = st[::-1]
#  if st == rev_st:
#      return True
#  else:
#         return False
# st = input("enter the message" )
# if palindrome(st):
#     print("its a palindrome")
# else:
#     print("its not a palindrome")

def palindrome(txt):
    txt.upper()
    rev_string=txt[::-1]
    if txt==rev_string:
        return True
    else:
        return False

txt=input("enter the string to check whether its a palindrome or not")
if palindrome(txt):
    print("its a palindrome")
else:
    print("its not a palindrome")


