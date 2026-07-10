

for i in range(1,100+1):
    
    if i<10:
        if i%2==0:
            print(i)
        else:
            pass
    
    else:
        count=0
        temp=i
        while temp>0:
            a=temp%10
            count=count+a
            temp=temp//10
            
        if count%2==0:
            print(i)
            
        else:
            pass
    
        
    