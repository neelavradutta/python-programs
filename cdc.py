n=10
a=0
b=1
s=[a,b]
while n>=a+b:
    c=a+b
    s.append(c)
    if s==target:
        print(True)
    a=b
    b=c
    

print(s)