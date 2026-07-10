s1="w3resource .  com  "
s2=""
max=0
for i in range(len(s1)):
    a=s1.count(s1[i])
    if a>max:
        max=a
        s2=s1[i] 

print(max)
print(s2)       
