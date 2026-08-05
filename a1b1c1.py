s = "a1c1e1g"
s1=""
for i in range(len(s)):
    if s[i].isdigit():
        a=ord(s[i-1])
        shift=int(s[i])
        s1=s1+chr(a+shift)
        
    else:
        s1=s1+s[i]
print(s1)