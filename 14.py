n=int(input())
str=list(input())[::-1]
a=[]
v=['a','e','i','o','u']
for k in str:
  if k not in v:
    a.append(k)
print(*a,sep='')
