arr=[1,2,3,2,3,1,3,1]
oc=[]
for i in range(len(arr)):
    count=0
    for j in range(len(arr)):
        if arr[i]==arr[j]:
            count=count+1
            
    if count%2!=0 and arr[i] not in oc:
        oc.append(arr[i])
print(oc)