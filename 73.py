n,k=list(map(int,input().split()))
n1=list(map(int,input().split()))
c=0
l=[]
for i in n1:
    c=c+1
    if k==i:
        print(c)
    else:
        l.append(i)

