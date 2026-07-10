a=int(input("enter first side "))
b=int(input("enter second side "))
c=int(input("enter third side "))

if a+b>c and b+c>a and c+a>b:
    print("it is a triange")
else:
    print("its not a triangle ")