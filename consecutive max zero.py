s1="112000fd000fgfg0000000dfd0000212000000123000020002"
curr=0
maxc=0
for i in range(len(s1)):
    if s1[i]=="0":
        curr=curr+1
        maxc=max(curr,maxc)
        
    else:
        curr=0
        
print(maxc)
            
    
