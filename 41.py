n,k=list(map(int,input().split()))
while n>1:
    n=n%k
if n==0:
    print('yes')
else:
    print('no')
