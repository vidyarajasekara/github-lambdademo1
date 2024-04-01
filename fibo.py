
def fib(num, n1, n2, n3):
    print(n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")
    return n3  # Added return statement to return the last Fibonacci number

num = int(input("enter the number to find fibonacci series num:"))  # Convert input to int
n1 = int(input("enter the value for n1:"))  # Convert input to int
n2 = int(input("enter the value for n2:"))  # Convert input to int
n3 = 0
result = fib(num, n1, n2, n3)
print("\nThe last number in the Fibonacci series is:", result)

#
# # .............................................
# def fib(num,n1,n2,n3):
#     print(n1,n2,end=" ")
#     for i in range(2,num):
#         n3=n1+n2
#         n1=n2
#         n2=n3
#         print(n3,end=" ")
#     return n3
# num=input("enter the number to find fibonacci series num:")
# n1=input("enter the value for n1:")
# n2=input("enter the value for n2:")
# n3=0
# result=fib(num, n1, n2,n3)
# print(result)
# # .....................................................
#
# num=10
# n1,n2=0,1
# print("fibnacci series:",n1,n2,end=" ")
# for i in range(2,num):
#     n3=n1+n2
#     n1=n2
#     n2=n3
#     print(n3,end=" ")