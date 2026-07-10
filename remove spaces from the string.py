s1="w3resource .  com  "
s2=""
for i in range(len(s1)):
    if s1[i]!=" ":
        s2=s2+s1[i]

cnt=s1.count(" ")        
print(cnt)        
print(" "*cnt + s2)
    
