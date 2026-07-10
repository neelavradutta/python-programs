a=int(input("enter a 3 digit number "))
num1=a//100
num2=(a//10)%10
num3=a%10


if num2>num1 and num2>num3:
    print("largest")
elif num1>num2 and num3>num2:
    print("smallest")
else:
    print("neither")