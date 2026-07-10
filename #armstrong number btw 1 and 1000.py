#armstrong number btw 1 and 1000

for i in range(1,1000+1):
    temp=i
    sum=0
    while temp>0:   
        a=temp%10
        sum=sum+(a**3)
        temp=temp//10
    if sum==i:
        print(i)
    else:
        pass