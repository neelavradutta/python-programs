s1="Python"
lst=[]
s2=""
for i in range(len(s1)):
    s2=s2+str(ord(s1[i]))+","
    
print(s2[:-1])
    