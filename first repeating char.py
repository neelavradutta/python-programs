s1="abcxxy"
s2=[]
for i in range(len(s1)):
    if s1[i] in s1[i+1:]:
        print(s1[i],i)
        break
    
    else:
        pass

        