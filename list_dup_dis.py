a = [1,2,5,2,6,7,5,1,8,9]
b = []
c = []
for item in a:
    if a.count(item)>1:
        if item not in b:
            b.append(item)
    elif a.count(item) == 1:
         if item not in c:
            c.append(item)
print("duplicate elements in a list are:",b)
print("distinct elements in a list are:",c)