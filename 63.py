n=int(input())
m=list(input().split())
o=list(input().split())
for i in m:
    if i in o:
        print(*i,end=' ')
