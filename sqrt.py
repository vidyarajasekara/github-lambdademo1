import math

number = 25
square_root = math.sqrt(number)

print("Square root of", number, "is:", square_root)
number = 9
square_root = number ** 0.5

print("Square root of", number, "is:", square_root)

n = int(input("Enter the integer to square: "))

output = n * n

print(output)

# .....................................................................

n = int(input("Enter the number of integers to square: "))

for i in range(1, n + 1):
    square = i ** 2

    print(square)

# .................................................................

    import pandas as pd

    # # Creating a Series from a list....series single column data
    # s = pd.Series([1, 2, 3, 4, 5]).....seriesdata type default foat64
    # print(s[0])  # Accessing the first element using integer-based indexing
    # print(s.iloc[0])  # Accessing the first element using iloc (integer location)
    # print(s['a'])
    #  print(s.loc[3])  ....location of 3