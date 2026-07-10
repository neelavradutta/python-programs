

str='545fd%^&'
str1=list(str)

a=0
print(str1)
if len(str)>=8:
    for i in range(len(str1)):
        if str1[i].isdigit()==True:
            a=1
            break
        
               
    
if a==1:
    print("strong")
else:
    print("weak")