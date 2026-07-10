s1="string"

if len(s1)<3:
    print(s1)
    
else:
    if s1[-3:]=="ing":
        print(s1+"ly")
    else:
        print(s1+"ing")