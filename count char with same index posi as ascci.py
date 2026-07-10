s1="xbcefg"
s2="abcdefgfijklmnopqrstuvwxyz"
count=0
for i in range(min(len(s1),len(s2))):
        if s1[i]==s2[i]:
            count=count+1
            
print(count)
            


