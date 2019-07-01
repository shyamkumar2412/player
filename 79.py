a,b=list(map(int,input().split()))
c=a*b
if c!=0:
    for i in range(0,c):
        b=i*i
        if b==c:
            print('yes')
            break
    else:
        print('no')
else:
    print('yes')
