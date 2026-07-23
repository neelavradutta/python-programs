nums=list(map(int,input().split()))
flag=0
for x in range(len(nums)+1):
    count=0
    for i in range(len(nums)):
        if nums[i]>=x:
            count=count+1 
    if count==x:
        flag=1
        break
    
if flag==1:
    print(x)
else:
    print(-1)
        
        
        