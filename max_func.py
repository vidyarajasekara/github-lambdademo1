li=[5,1,2,4,3]
max_num=li[0]
for i in li[1:]:
  if max_num<i:
      max_num=i
  else:
      continue
print(max_num)