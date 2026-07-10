s1="Python Exercises Practice Solution Exercises"
lst=s1.split()
l1=[]
for i in range(len(lst)):
    if lst[i] not in l1:
        l1.append(lst[i])
    

print(l1)


