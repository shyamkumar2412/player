n=int(input())
for i in range(1,n):
    d=i
    r=int(n/d)
    if r%2!=0:
        print(d)
        break
