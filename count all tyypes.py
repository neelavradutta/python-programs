s1="edssss.........??f25#%t48fSFSFGL8f"
a=0
b=0
c=0
d=0
for i in range(len(s1)):
    if s1[i].isupper()==True:
        a=a+1
    elif s1[i].islower()==True:
        b=b+1
    elif s1[i].isdigit()==True:
        c=c+1
    else:
        d=d+1    
        
print("Upper case char -",a)
print("Lower case char -",b)
print("Digit char -",c)
print("Special char -",d)