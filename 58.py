s=list(map(str,input().split()))
k=str(input())
c=0
for i in s:
    if k==i:
        c=c+1
print(c)
