n,x=list(map(int,input().split()))
n=list(input().split())
s=0
for i in n:
    s=int(s)+int(i)
print(s)
if s==x:
    print('yes')
else:
    print('no')
