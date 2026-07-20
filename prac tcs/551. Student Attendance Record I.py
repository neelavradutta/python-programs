s=input()
ac=0
for i in range(len(s)):
    if s[i]=="A":
        ac=ac+1

flag=0
for i in range(len(s)-2):
    if s[i]==s[i+1]==s[i+2]=="L" or ac>=2:
        flag=1
        break
    
if flag==0:
    print(True)
else:
    print(False)
    
        
    