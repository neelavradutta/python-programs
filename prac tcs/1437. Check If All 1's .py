n=11
Flag=True
for i in range(2,n):
    if n%i==0:
        Flag=False
        break
if Flag==True:
    print("prime")
else:
    print("Non prime")


    
