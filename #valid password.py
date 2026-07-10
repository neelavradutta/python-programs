#valid password
s="fdhf%S5 145^d"
digi=False
lo=False
up=False
spe=False
for i in range(len(s)):
    if s[i].isdigit()==True:
        digi=True 
    elif s[i].islower()==True:
        lo=True 
    
    elif s[i].isupper()==True:
        up=True 
    else:
        spe=True       
        
if digi==True and  lo==True and  up==True and  spe==True:          
    print("Valid")
else:
    print("Not valid")