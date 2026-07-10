k=5
a=[-1,2,3,3,4,5,-1]
lst=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        if sum(a[i:j])<=k:
            lst.append(sum(a[i:j]))
        else:
            break   
print(lst)