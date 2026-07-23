nums=list(map(int,input().split()))
flag=0

if len(nums)==1:
    flag=1

else:
    for i in range(len(nums)-1):
        if (nums[i]%2==0 and nums[i+1]%2!=0) or (nums[i]%2!=0 and nums[i+1]%2==0):
            flag=1
        else:
            flag=0
            break

if flag==0:
    print(False)
else:
    print(True)

        
        

