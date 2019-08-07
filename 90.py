n,m=list(map(int,input().split()))
l=[]
s=1
x=1
for i in range(m):
    s=s*n
    n=n-1
for i in range(1,m+1):
    x=x*i
print(s//x)
    
