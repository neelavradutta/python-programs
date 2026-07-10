
a=int(input("enter first side "))
b=int(input("enter second side "))
c=int(input("enter third side "))

if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
    print("yes")
else:
    print("no")