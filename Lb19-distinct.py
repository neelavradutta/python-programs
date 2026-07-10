a=int(input("enter a 4 digit number "))


num1=a//1000
num2=(a//100)%10
num3=(a//10)%10
num4=a%10



if num1==num4:
    print("equal")
else:
    print("not equal")
