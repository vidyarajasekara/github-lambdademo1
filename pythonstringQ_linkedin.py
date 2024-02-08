#1. reverse string
# a="vidya"
# # using slicing
# print(a[::-1])
#
#
# a="vidya"
# b=a.split()
# print(b)
# print(type(b))
# print(b[0])
# print(len(b[0]))
# i=len(b[0])
# j=1
# print(type(b[0]))
# for a in b[0]:
#     # row column
#     print(b[0][i-j],end="")
#     j+=1


# 2.string palindrome
# a="madam"
# b=a.split()
# i=len(b[0])
# print(i)
# j=1
# c=""
# for x in b[0]:
#     c+=(b[0][i-j])
#     j+=1
# print(c)
# if a==c:
#      print("palindrome")
# else:
#      print("not palinrome")


# # doubt
# a="madam"
# b=a.split()
# i=len(b[0])
# print(i)
# j=1
# c=""
# for x in range(i-1,0,-1):
#     c+=b[0][x]
#     j+=1
# print(c)
# if a==c:
#      print("palindrome")
# else:
#      print("not palinrome")
#
# #slicing
# s="madam"
# s1=s[::-1]
# if s==s1:
#     print("palindrome")
# else:
#     print("not a palindrome")

#3.count the vowels in string
# a="applebee"
# a1=list(a)
# b="aeiou"
# b1=list(b)
# for i in b1:
#     count=0
#     for j in a1:
#         if i==j:
#             count+=1
#     print(f"{i} count is",count)

# #doubt
# def count_vowels(input_string):
# vowels = "aeiouAEIOU"
# return sum(1 for char in input_string if char in vowels)

#4.doubt find the most frequent character in string
# s="mummy"
# s1=list(s)
# dict1={}
# for i in s1:
#     count=0
#     for j in s1:
#         if i==j:
#             count+=1
#             dict1[i]=count
# print(dict1)
# key = max(dict1, key=lambda k: dict1[k])
# max_count = dict1[key]
# print("Key with the maximum count:", key)
# print("Maximum count:", max_count)


# s1="daddy"
# s2=list(s1)
# count_fc=[]
# count=[]
# for i in s2:
#     if i not in count:
#         count.append(i)
#     else:
#         count_fc.append(i)
# print("the most occurance char from the string is:",count_fc[0])



# 5.remove all the duplicates from string
# s="hello goodmorning"
# s1=s.replace(" ","")
# print(s1)
# print(type(s1))
# s3=list(s1)
# print(s3)
# j=0
# dict1={}
# for i in s3:
#     c=s3.count(s3[j])
#     print(f" '{s3[j]}' count is",c)
#     if c == 1 and s3[j] not in dict1:
#         dict1[s3[j]]= c
#     j+=1
# print(dict1.keys())
# print("".join(dict1.keys()))



# s="happy morning"
# s1=s.replace(" ","")
# print(s1)
# s2=list(s1)
# dict1={}
# j=0
# for i in s2:
#     c=s2.count(s2[j])
#     if c == 1 and c not in dict1:
#         dict1[s2[j]]=c
#     j+=1
# print(dict1.keys())
# print("".join(dict1.keys()))




# #6.check the string contains only digits
# s="5537889"
# print(s.isdigit())
# s1="yy66889"
# print(s1.isdigit())


#7.count the occurance of each word in a string
# s="hai hai hello"
# s1=s.split()
# print(s1)
# j=0
# for i in s1:
#     c=s1.count(s1[j])
#     print(f" '{i}' count is",c)
#     j+=1


#.8 capitalize first letter in each word in a sentence:
# s = "hai hai hello"
# s1 = s.title()
# print(s1)
#
# s2=s.split()
# for i in s2:
#    print(i.capitalize()+" ",end="")

#9.write a python program to find the longest word in a sentence:
# s="welcome to python world"
# s1=s.split()
# dict2={}
# x=0
# for i in s1:
#     r=len(s1[x])
#     print(f"'{s1[x]}' length is :",len(s1[x]))
#     dict2.update({s1[x]:r})
#     x+=1
# print(dict2)
# m = max(dict2,key=dict2.get)
# print(m)

s1="happy newyear"
s2=s1.split(" ")
dict1={}
j=0
for i in s2:
    l=len(s2[j])
    dict1[s2[j]]=l
    j+=1
m=max(dict1,key=dict1.get)
print(m)
print(dict1)
dict1.update({"hobby":5})
print(dict1)






#10.write a python program to check if two strings are anagrams:

# def are_anagrams(str1, str2):
#     # Remove spaces and convert to lowercase for case-insensitive comparison
#     str1 = str1.replace(" ", "").lower()
#     str2 = str2.replace(" ", "").lower()
#
#     # Check if the sorted characters of both strings are the same
#     # return sorted(str1) == sorted(str2)
#
# # Example usage:
# word1 = "Listen"
# word2 = "Silent"
#
# if are_anagrams(word1, word2):
#     print(f"{word1} and {word2} are anagrams.")
# else:
#     print(f"{word1} and {word2} are not anagrams.")
#
#





















