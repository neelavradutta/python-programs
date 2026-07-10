n=int(input("enter n = "))
for i in range(1,n+1):
    a=int(bin(i)[2:])
    count=0
    while a>0:        
        unit=a%10
        if unit==1:
            count=count+1
        a=a//10
    if count%2==0:
        print(i)


    