s = ")ebc#da@f("
rev="abcdefghijklmnopqrtuvwxyz"
c=[]
d=[]
for i in range(len(s)):
    if s[i] in rev:
        c.append([i])
    else:
        d.append(s[i])
    
print(c[::-1].join(d[::-1]))