s = "abc"
n=0
for i in range(len(s)):
    a=123-ord(s[i])
    n=n+a*(i+1)
print(n)