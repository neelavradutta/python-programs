sting=[]
n=int(input("enter the length"))

for i in range(n):
    str=input("enter the element")
    sting.append(str)

string2=sting.copy()
sting.reverse()
if(sting == string2):
    print("the number is pallindrome")
else:
    print("not pallindrome")

