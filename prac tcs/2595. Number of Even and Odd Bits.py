n=int(input())
a=bin(n)[2:][::-1]
ov=0
ev=0
for i in range(len(a)):
    if a[i]=="1":
        if i%2==0:
            ev=ev+1
        else:
            ov=ov+1
    
print([ev,ov])