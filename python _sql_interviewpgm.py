# even numbers
# a=int(input("enter the minimum range value for a :"))
# b=int(input("enter the maximum range value for b:"))
# print("even numbers")
# for i in range(a,b+1):
#         if (i>1) and (i%2 == 0):
#             print(i,end=" ")
#         else:
#             continue
# ..................................................................
# odd numbers
# a=int(input("enter the minimum range value for a :"))
# b=int(input("enter the maximum range value for b:"))
# for i in range(a,b+1):
#     if(i>1) and (i%2==0):
#        continue
#     else:
#         print(i)
# #..........................................................
# prime numbers
# num=int(input("Enter range:"))
# print("Prime numbers:")
# for n in range(1,num):
#  for i in range(2,n):
#      if(n%i==0):
#          break
#  else:
#      print(n,end=" ")
#............................................................
# sort:ascending to descending
#z = [2,7,5,1,8,3,7]
# z=[2,5,7,5,3,4,5,2]
# for i in range(len(z)):
#     for j in range(i+1,len(z)):
#             if z[j]<z[i]:
#                 z[i],z[j]=z[j],z[i]
# print(z)
#.......... sort descending to ascending:
# z=[2,5,7,5,3,4,5,2]
# for i in range(len(z)):
#     for j in range(i+1,len(z)):
#             if z[j]>z[i]:
#                 z[i],z[j]=z[j],z[i]
# print(z)
# find max................................................
# v=[1,6,3,9,5,]
# max=v[0]
# for i in v:
#     if i>max:
#         max=i
# print(max)
# ......................sort using method asce and desc...........
# v=[5,7,3,0]
# print(sorted(v))
# print(sorted(v,reverse=True))
# .....remove duplicates and append in another list....................................
# z = [2, 5, 7, 5, 3, 4, 2,8]
# n = []
# for i in range(len(z)):
#     for j in range(i+1, len(z)):
#         if z[j] == z[i]:
#             n.append(z[i])
#             z.pop(j)
#             break
# print("Duplicates:", n)
# print("after removing duplicates:", z)
# print("sorted list after removing duplicates:",sorted(z))
#.............. find the second largest number:
# list1 = [10, 20, 20, 4, 45, 45, 45, 99, 99]
# print("given list",list1)
# unique_elements=list(set(list1))
# print("unique elements:",unique_elements)
# print("sorted elements in desc order:",sorted(unique_elements,reverse=True))
# list2=sorted(unique_elements,reverse=True)
# print("second max number from the list:",list2[1])
#............................................................
list2=[4,6,1,1,6]
s=set(list2)
print("this is unique set:",s)
l2=list(s)
print("this is uniques elements in a list:",l2)









