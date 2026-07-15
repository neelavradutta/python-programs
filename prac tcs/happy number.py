n=int(input())
while n!=1 and n!=4:
    sum=0
    while n>0:
        a=n%10
        sum=sum+a**2
        n=n//10
    n=sum
    
if n==1:
    print("Happy")
else:
    print("non Happy")