a=145
temp=a
total=0


while a>0:
    l=a%10
    c=1
    for i in range(l,0,-1):
        c=c*i
        
    total=total+c
    a=a//10
if temp==total:
    print("strong")
else:
    print("not strong")
        