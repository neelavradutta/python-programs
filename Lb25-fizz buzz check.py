n=int(input("enter the total numbers to be entered "))

str=[]

for i in range(n):
    r=input("enter the number ")
    str.append(r)
    
str.sort()

print(str)

if n%2==0:
    median = (str[n // 2 - 1] + str[n // 2]) / 2
    
else:
    median=str[n//2]
    
print(median)