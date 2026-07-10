s1="Red White"
s2="White Red"
count=0
for i in range(len(s1)):
    if s1[i:i+3]==s2[i:i+3]:
        count=count+1
        
print(count)