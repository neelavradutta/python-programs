s=9
l=0
n=6518615
while n>0:
    a=n%10
    if a>l:
        l=a
    elif a<s:
        s=a
    else:
        pass
        
    n=n//10
    
print("smallest =",s,"largest =",l)