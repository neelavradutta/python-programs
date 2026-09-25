s = "abcd"
d=s[0]
s=s.replace(s[0],s[2])
s=s.replace(s[2],d)
print(s)