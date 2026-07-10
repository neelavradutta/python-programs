
for i in range(1,500+1):
    count=0
    temp=i
    while temp>0:
        a=temp%10
        count=count*10+a
        temp=temp//10
    if count==i:
        print(i)
        
