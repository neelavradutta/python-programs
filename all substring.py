s1="abc"
sub=[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        sub.append(s1[i:j])
print(sub)
            

            
            