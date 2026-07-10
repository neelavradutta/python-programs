s1="snjkhfiukjdfnclek;"
max=0
s2=""
for i in range(len(s1)):
    a=s1.count(s1[i])
    if a>max:
        max=a
        s2=s1[i]
    else:
        pass

print(max,s2)
       
