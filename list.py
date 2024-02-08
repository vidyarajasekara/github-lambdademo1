# list
mylist = ["strawberry","mango","orange"]
print(mylist)

# indexing
mylist = ["strawberry","mango","orange"]
print(mylist[2])

# negative indexing
mylist = ["strawberry","mango","orange"]
print(mylist[-1])

# range of indexes
mylist = ["strawberry","mango","orange"]
print(mylist[1:2])
print(mylist[:2])

# change the list item
mylist[1] = "dragonfruit"
print(mylist)
mylist2 = ["apple","pineapple","strawberry","mango","orange"]
#doubt
mylist2[2:4] = ["blueberries","raspberries"]
print(mylist2)
mylist2[0:3] = ["blue","red","yellow"]
print("mylist2:",mylist2)
# insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
list3 = ["aaa","bbb","ccc"]
# doubt
list3.insert(1,"xxx")
print(list3)
# append item
list3 = ["aaa","bbb","ccc"]
list3.append("ddd")
print(list3)
#Extend List
list4=["qqq","rrr","hhh","uuu"]
list5=["zzz","vvv","jjj"]
list4.extend(list5)
print(list4)
#remove
list4.remove("jjj")
print(list4)
#pop
list4.pop(3)
print(list4)

list4.pop()
print(list4)
#del
l1 = ["yyy","lll","ooo"]
del l1[0]
print(l1)
#clear
l2 = ["ggg","yyy","uuu"]
l2.clear()
print(l2)
# loop through a list
list1 = ["a","b","c","d","e"]
print(list1)
for i in list1:
     print(i)

# sort:
l4 = [0,1,3,2,9,5]
l4.sort()
print(l4)

l4 = [20,1,3,15,9,5]
l4.sort()
print(l4)
# descending
l4 = [20,1,3,15,7,5]
l4.sort(reverse=True)
print(l4)

# copylist
l5 = ["vvv","nnn","hhh"]
l6 = l5.copy()
print(l6)

l7=["ooo","ppp","uuu"]
l8=list(l7)
print(l8)

# adding two list
l9=l6+l8
print(l9)
# add two list one by one
l10 = ["w","e","r"]
l11 = ["1","2","3"]
for i in l11:
     l10.append(i)
     print(l10)

#6.list comprehension
lis1=["apple","banana","grapes"]
lis2=[]
for i in lis1:
     if "p" in i:
          lis2.append(i)
          print(lis2)

# 7.list comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# if else front and if condition at the back
lc = ["apple","banana","grapes"]
lc1 = [x for x in lc if "n" in x]
print(lc1)

# Assignment 1 - how to acheive it via for loop
# #output:['banana', 'cherry', 'kiwi', 'mango']
# #The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".
# #The condition is optional and can be omitted:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits]
# print(newlist)


def f(fruits):
     for x in fruits:
          if x !="apple":
               return True
     return False

fruits=["apple", "banana", "cherry", "kiwi", "mango"]
output = f(fruits)
print(output)















