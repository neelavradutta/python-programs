s1="abc"
count=0
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        sub=s1[i:j]
        if sub[0]==sub[-1:]:
            count=count+1
            print(sub)
            
print(count)
            
            