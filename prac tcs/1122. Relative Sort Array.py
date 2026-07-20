arr1=list(map(int,input().split()))
arr2=list(map(int,input().split()))
c=[]
d=[]
for i in range(len(arr2)):
    for j in range(len(arr1)):
        if arr1[j]==arr2[i]:
            c.append(arr1[j])

for i in range(len(arr1)):
    if arr1[i] not in c:
        d.append(arr1[i])
            
print(*(c+sorted(d)))