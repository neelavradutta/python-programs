s1="The quick brown fox"
s2="jumps over the lazy dog"
miss1=""
miss2=""
lst=[]
for i in s2:
        if i not in s1:
            miss1=miss1+i 
            
        else:
            pass
for i in s1:
        if i not in s2:
            miss2=miss2+i 
            
        else:
            pass        

print(s1+miss1)
print(s2+miss2)

