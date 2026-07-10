a=int(input("enter first side "))
b=int(input("enter second side "))
c=int(input("enter third side "))

if a+b>c and b+c>a and c+a>b:
    print("it is a triange")
    if a==b==c:
        print("to be precise, equilateral")
    elif a==b or b==c or c==a:
        print("to be precise, isosceles")
    else:
        print("to be precise, scalene")
        
else:
    print("its not a triangle ")