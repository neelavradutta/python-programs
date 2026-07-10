a=int(input("enter a 3 digit number "))
num1=a//100
num2=(a//10)%10
num3=a%10


if num1!=num2 and num2!=num3 and num1!=num3:
    print("distinct")
else:
    print("not distinct")
