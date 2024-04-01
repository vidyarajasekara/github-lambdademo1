def intersection(a,b):
    intersection_list = []
    for i in a:
        for j in b:
            if i==j:
                intersection_list.append(i)
    return intersection_list
a= [1, 2, 3, 4, 5]
b = [0, 1, 3, 7]
# intersection_list=[]
result=intersection(a,b)
print(result)
