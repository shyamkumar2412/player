n=int(input())
count=0
n=input().split()
for i in n:
    for j in n:
        if i<j:
            count=count+1
print(count)
