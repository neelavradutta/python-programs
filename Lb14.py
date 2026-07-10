time=int(input("enter time "))


if time>=0 and time<=11:
    print("morning")
elif time>=12 and time<=17:
    print("afternoon")
elif time>=18 and time<=20:
    print("evening")
else:    
    print("good night")    
    
