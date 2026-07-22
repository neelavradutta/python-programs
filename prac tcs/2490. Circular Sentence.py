s=input()

flag=0
if s[0]!=s[-1]:
    flag=1

for i in range(len(s)):
    if s[i]==" ":
        if s[i-1]!=s[i+1]:
            flag=1
            break
    
if flag==0:
    print(True)
else:
    print(False)
    