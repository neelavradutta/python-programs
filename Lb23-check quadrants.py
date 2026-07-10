x=int(input("enter x quadrant "))
y=int(input("enter y quadrant "))


if x==0 and y==0:
    print("at center")
    
elif x>0 and y>0:
    print("first quadrant")
    
elif x>0 and y<0:
    print("second quadrant")
    
elif x<0 and y<0:
    print("third quadrant")
    
elif x==0 and (y>0 or y<0) :
    print("on Y axis")
    
elif y==0 and (x>0 or x<0) :
    print("on X axis")    
    
else:
    print("forth quadrant")
    
