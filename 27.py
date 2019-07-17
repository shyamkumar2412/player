n=str(input())
for i in n:
    if i.isupper()==True:
        print(i.lower(),end='')
    elif i.islower()==True:
        print(i.upper(),end='')

