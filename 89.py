n,m=list(map(int,input().split()))
s=1
for i in range(m):
    s=s*n
    n=n-1
print(s)
