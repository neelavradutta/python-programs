N=int(input())
ar=list(map(int,input().split()))
a=[]
for i in range(len(ar)):
 for j in range(i+1,len(ar)+1):
  a.append(sum(ar[i:j]))

print(max(a))