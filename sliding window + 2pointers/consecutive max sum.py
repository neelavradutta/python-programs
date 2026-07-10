a=[-1,2,3,3,4,5,-1]
lst=[]
for i in range(len(a)-3):
    lst.append(a[i]+a[i+1]+a[i+2]+a[i+3])

print(max(lst))
    