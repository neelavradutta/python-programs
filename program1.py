s1="hello world"
s2=""
for i in range(len(s1)-1):
    if s1[i]!=s1[i+1]:
        s2=s2+s1[i]
s2=s2+s1[-1:]        
print(s2)