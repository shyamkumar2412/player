a,b=list(map(int,input().split()))
l=[]
s=1
x=1
for i in range(b):
    s=s*a
    a=a-1
for i in range(1,b+1):
    x=x*i
print(s//x)
    
