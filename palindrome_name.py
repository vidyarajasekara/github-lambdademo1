s="vidya"
print("given string:",s)
c=len(s)-1
rev=""
for i in s:
    rev=rev+s[c]
    c=c-1
print("reversed string:",rev)
if s==rev:
    print("its a palindrome")
else:
    print("its not a palindrome")