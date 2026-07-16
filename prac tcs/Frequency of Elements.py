elements=[1,2,2,3,1]
d={}
for i in range(len(elements)):
    count=0
    for j in range(len(elements)):
        if elements[i]==elements[j]:
            count=count+1
    d[elements[i]]=count

print(d)