# num1 = 5
# num2 = 10
# sum = num1+num2
# print("num1","and","num2",sum)


n1 = 1
n2 = 2
sum = n1+n2
print("sum of n1 and n2 is:",sum)


a = "vidya"
# a1=a[::-1]
# print(a1)


def cal(a):
  a.split()
  b=[]
  j=4
  for i in a:
    b.append(a[j])
    j-=1
    c="".join(b)
  return c

a="vidya"
result=cal(a)
print(result)