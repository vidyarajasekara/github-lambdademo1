# s = "vidya"
# s1 = "aeiou"
# count = 0
# count1 = 0
# for char in s:
#     if char in s1:
#         count += 1
# print(count)
#
# print(count)
# for char in s:
#     if char not in s1:
#         count1 += 1
#
# print(count1)


# ......................................................

l=[3,0,1]
# find the missing number array sum and range sum minus
l1=[0,1,2,3]
count=0
count1=0
for i in l:
    count+=i
print(count)
for i in l1:
    count1+=i
print(count1)
diff=count1-count
print("the missing number is ",diff)


