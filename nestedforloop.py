a, b, c1, c2 = 5, 7, 0, 0
for i in range(20, a, -1):
    c1 = c1+1
    for j in range(0, b):
        c2 = c2+1
        if i == j:
            print("how many times the loop run?")
            print(c1)
            print("\nsecond loop:"+str(c2))




# for i in range(20,5,-1):
#     print(i)
#
# for i in range(20, -1, 5):
#  print(i)