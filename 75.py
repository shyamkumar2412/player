ax=input()
a=[]
if len(ax)%2==0:
    for i in range(0,len(ax)):
        if i==len(ax)//2 or i==len(ax)//2-1:
            a.append('*')
        else:
            a.append(ax[i])
else:
    for i in range(0,len(ax)):
        if i==len(ax)//2:
            a.append('*')
        else:
            a.append(ax[i])
print(*a,sep='')
