n1=int(input())
n=list(map(int,input().split()))
l=[]
m=[]
for i in n:
    if i>n1:
        l.append(i)
    else:
        m.append(i)
m.sort()
print(*m,end=' ')

 
