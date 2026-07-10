
date=int(input("enter date "))
month=int(input("enter month "))

maxdays=0

if date<1 or month>12 or month<1:
    print("invalid")
    
else:
    if month=={1,3,5,7,8,10,12}:
        maxdays=31
    elif month=={4,6,9,11}:
        maxdays=30
    else:
        maxdays=28
        
if(date>maxdays):
    print("invalid")
else:
    print("valid")
    
    
  
