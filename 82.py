n=int(input())
a=list(map(int,input().split()))
if len(a)>1:
    for i in range(len(a)-1):
        print(a[i] & a[i+1]) 
else:
    print(*a)
