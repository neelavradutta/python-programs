N,target=map(int,input().split())
arr=list(map(int,input().split()))

a=0
b=0
flag=0
for i in range(len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i]+arr[j]==target and i!=j:
            flag=1
            a=i
            b=j
            break

    if flag==1:
        print(a+1,b+1)
        break

    