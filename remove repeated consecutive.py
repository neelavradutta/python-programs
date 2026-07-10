s1='aabbcceffgh'
s2=""
s3=""
for i in range(len(s1)):
    if s1.count(s1[i])==1:
        s2=s2+s1[i]
        
    else:
        if s1[i] not in s3:
            s3=s3+s1[i]  
        
print(s2,s3)