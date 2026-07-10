d1=31
m1=4
d2=44
m2=4

if m1<1 or m2<1 or m1>12 or m2>12 or d1<1 or d1>31 or d2<1 or d2>31 or (d1>28 and m1==2) or (d2>28 and m2==2) or (m1 in [4,6,9,11] and 
 d1>30) or (m2 in [4,6,9,11] and d2>30):
    print("invalid")

else:
    if m1>m2:
        print("date 2 comes first")
    elif m1==m2:
        if d1>d2:
            print("date 2 comes first")
            
        elif d1==d2:
            print("same date")
            
        else:
            print("date 1 comes first")
        
    else:
        print("date 1 comes first")
        
    
    
