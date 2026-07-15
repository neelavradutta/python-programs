s=input()
flag=True
a=0
for i in range(len(s)):
    if s[i] not in s[i+1:] and s[i] not in s[:i]:
        flag=False
        a=i
        break

if flag==True:
    print(-1)
else:
    print(a)
    
