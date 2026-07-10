date="2020-05-15"
lst1=[]
s1=""
lst=date.split("-")
for i in range(len(lst)):
    a=bin(int(lst[i]))
    lst1.append(a[2:])
print("-".join(lst1))