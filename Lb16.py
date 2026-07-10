n=input("enter number b/w 1 to 12 ")



dict={'1':'31','2':'28','3':'31','4':'30','5':'31','6':'30','7':'31','8':'31','9':'30','10':'31','11':'30','12':'31'}

if n in dict:
    print(dict[n]) 
else:
    print("invalid")