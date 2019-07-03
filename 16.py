n=int(input())
a=input().split()
z=[]
for i in a:
  if i not in z:
    z.append(i)
for i in z:
  if a.count(i)==1:
    print(i)
