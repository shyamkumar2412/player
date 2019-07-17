l,r=list(map(int,input().split()))
c=0
for i in range(1,(r**2)+1):
    s=i*i
    for j in range(l,r+1):
        if s>=l and s<=r+1:
            c=c+1
            break
print(c)


