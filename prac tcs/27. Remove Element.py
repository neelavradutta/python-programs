nums=list(map(int,input().split()))
val=int(input())
c=0
for i in range(len(nums)):
    if nums[i]!=val:
        nums[c]=nums[i]
        c=c+1
             
print(c)
            


    
