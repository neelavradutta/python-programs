s1="wr3esource"

cap=False
low=False
digi=False


s=0
for i in range(len(s1)):
    if s1[i].isupper():
        cap=True
        
    if s1[i].islower():
        low=True
        
    if s1[i].isdigit():
        digi=True
        
        
        
if cap==True and low==True and digi==True:    
    print("Valid")
        
else:
    print("invalid")