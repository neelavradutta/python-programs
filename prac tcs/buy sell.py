N=int(input())
arr=list(map(int,input().split()))
buy=min(arr)
buypos=arr.index(buy)

for i in range(1,N):
    if 