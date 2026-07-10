s1=input("enter word ")
n=int(input("enter the nth index "))


if len(s1)<0 or len(s1)<n or n<0 or s1=="":
    print("string is empty")
    
else:
    
    for i in range(len(s1)):
        if i==n:
            print(s1[:i]+s1[i+1:])
            break          
  
    

