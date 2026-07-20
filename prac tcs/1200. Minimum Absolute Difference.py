arr=list(map(int,input().split()))
arr=sorted(arr)
d=float('inf')
for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1])<d:
        d=abs(arr[i]-arr[i+1])

a=[]
for i in range(len(arr)-1):
    if abs(arr[i]-arr[i+1])==d:
        a.append([arr[i],arr[i+1]])
        
print(a)
