n,k=list(input().split())
n1=input().split()
l=[]
m=[]
for i in n1:
    if i<k:
        l.append(i)
    else:
        m.append(i)
l.sort()
print(*l,end=' ')


