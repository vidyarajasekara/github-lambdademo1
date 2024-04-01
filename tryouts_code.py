import pandas as pd
import requests as r
import time
import re


# def sequence_1(n):
#     for i in range(n+1):
#         print(f"{i}{'*'*i}")
# n=5
# res=sequence_1(5)
# .....................................
# def sequence_2(n):
#     sequence=[f"{i}{'*'*i}" for i in range(n+1)]
#     # print(sequence)
#     print('\n'.join(sequence))
# n=5
# res=sequence_2(5)
# # ..............................................
# def generate_sequence(n):
#     for i in range(n+1):
#         yield f"{i}{'*'*i}"
# n=5
# res=generate_sequence(5)
# print(res)
# l=list(res)
# print("\n".join(l))
# .....................................
# def generate_1(n):
#     result=generate_sequence(n)
#     for item in result:
#         print(item)
#
# res=generate_1(5)
# ..................................................
def square_generator(limit):
    n = 0
    while n < limit:
        yield n ** 2
        n += 1

# Using the generator
for x in square_generator(5):
    print(x)