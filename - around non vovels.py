s1="white"
s2=""
for i in range(len(s1)):
    if s1[i] not in "aeiou":
        s2=s2+("-"+s1[i]+"-")
        
    else:
        s2=s2+s1[i]
print(s2)