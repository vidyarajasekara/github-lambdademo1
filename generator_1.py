def generator_list(n):
    a=0
    while a<n:
        yield a ** 2
        a+=1
for i in generator_list(5):
    print(i)



