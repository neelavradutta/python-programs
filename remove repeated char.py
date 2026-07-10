s1="255.024.01.01"
lst=[]
s2=s1.split(".")

for i in s2:
    lst.append(str(int(i)))
    
print(".".join(lst))    
