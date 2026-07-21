nums=list(map(int,input().split()))
k=int(input())

d=[]
flag=True
c=0
for i in range(len(nums)):
    if (nums[i] not in d) and (nums[i]>k):
        d.append(nums[i])
        c=c+1
    elif nums[i]<k:
        flag=False
        break
if flag==False:
    print(-1)
else:
    print(c)