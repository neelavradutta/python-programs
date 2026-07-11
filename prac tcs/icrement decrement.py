operation=input().split()
x=0

for i in range(len(operation)):
    if operation[i]=="++X" or operation[i]=="X++":
        x=x+1
    else:
        x=x-1

print(x)
        