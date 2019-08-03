n=int(input())
n1=list(map(int,input().split()))
l=[]
m=[]
c=0
s=0
for i in n1:
    if i%2!=0:
        c=c+1
        l.append(i)
    else:
        s=s+1
        m.append(i)
if c<s:
    print(*l,end=' ')
else:
    print(*m,end=' ')
