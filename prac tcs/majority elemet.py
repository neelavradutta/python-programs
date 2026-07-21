N=int(input())
arr=list(map(int,input().split()))

for i in range(len(arr)):
    c=0
    for j in range(len(arr)):
        if arr[i] == arr[j]:
            c = c + 1
    if c > (N // 2):
        print(arr[i])
        break
 
            