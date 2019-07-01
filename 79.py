a,b=list(map(int,input().split()))
c=a*b
for i in range(1,c):
    b=i*i
    if b==c:
        print('yes')
        break
else:
    print('no')
