s1="dsf5SDr65f"

cap=False
low=False
digi=False

for i in range(len(s1)):
    if s1[i].isupper():
        cap=True
        
    if s1[i].islower():
        low=True
        
    if s1[i].isdigit():
        digi=True
        
        
        
if cap==True and low==True and digi==True and len(s1)>0:    
    print("Valid")
        
else:
    print("invalid")