s1="Red Green White"

lst2=[]
lst=s1.split()

for j in range(len(lst)):
    s2=""
    for i in range(len(lst[j])-1):
        if lst[j][i]!=lst[j][i+1]:
            s2=s2+lst[j][i]
    s2=s2+lst[j][-1]
    lst2.append(s2)        
        

print(" ".join(lst2))