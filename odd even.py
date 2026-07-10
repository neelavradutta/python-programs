print("enter a number1")
num1=int(input())
print("enter a number2")
num2=int(input())
print("enter a number3")
num3=int(input())

if(num1>num2 and num1>num3):
    print("the greatest number is "+str(num1))
elif(num2>num1 and num2>num3):
    print("the greatest number is "+str(num2))
else:
    print("the greatest number is "+str(num3))    