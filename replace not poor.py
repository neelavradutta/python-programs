s = "The lyrics is poor 1not !"
s1=""
notp=s.find("not")
poorp=s.find("poor")

if notp!=-1 and poorp!=-1 and notp<poorp:
    s1=s[:notp]+"good"+s[poorp+4:]
    
else:
    s1=s
print(s1)