s1="Python Exercises"
s2="yt"
a=0
b=0
for i in range(len(s1)):
    if s2[0]==s1[i]:
        a=i
        
for i in range(len(s1)):
    if s2[-1]==s1[i]:
        b=i
        
if len(s1[a:b+1])>=len(s2):
    print(a)
    
else:
    print("Not found")
        