n=int(input("enter the nth index "))
s1="Python"

if len(s1)<0:
    print("string is empty")
    
else:
    
    for i in range(len(s1)):
        if i==n:
            print(s1[:i]+s1[i+1:])
            break          
  
    

