a=[1,2,3,4,1,2,3,5]
for i in a:
 for j in a:
     if a[i] == a[j]:
         a.remove(i)
     else:
         continue
print(a)
