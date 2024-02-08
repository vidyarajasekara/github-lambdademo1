list=[x for x in range(1,11)]
print(list)

list=[x*3 for x in range(1,11)]
print(list)

list = [x**2 for x in range(1,11)]
print(list)

list = [x for x in range(1,11) if x % 2 == 0]
print(list)

list = [x for x in range(100) if x % 2 == 0 if x % 2 == 0]
print(list)

list = [x if x % 2 == 0 else 0 for x in range(100)]
print(list)

list = ["even" if x % 2 == 0 else "odd" for x in range(100)]
print(list)

list=[char.upper() for char in "maDAm"]
print(list)

