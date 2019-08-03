n=int(input())
n1=list(map(int,input().split()))
l=[]
m=[]
for i in n1:
    if i>n:
        l.append(i)
    else:
        m.append(i)
m.sort()
print(*m,end=' ')

 
