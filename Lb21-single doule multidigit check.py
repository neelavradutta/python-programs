a=int(input("enter a number "))


if a%7==0 and a%10==7:
    print("both")
elif a%7==0:
    print("multiple of 7")
    
elif a%10==7:
   print("last digit 7")
else:
    print("nothing")
    
 