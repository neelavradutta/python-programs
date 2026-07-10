hour=int(input("hour = "))
min=int(input("minute = "))

if hour<0 or hour>24 or min<0 or min>60:
    print("invalid")
else:
    a=abs(30*hour-11/2*min)
    if a>180:
        print("smaller angle is",(360-a))
    else:
        print("smaller angle is",a)
