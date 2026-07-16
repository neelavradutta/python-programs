n=int(input())
a=list(map(int,input().split()))
l,r=map(int,input().split())
print(max(a[l:r+1]))