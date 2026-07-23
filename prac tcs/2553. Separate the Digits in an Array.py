nums = list(map(int, input().split()))

a=[]
for i in range(len(nums)):
    rev=0
    while nums[i]>0:
        g=nums[i]%10
        rev=rev*10+g
        nums[i]=nums[i]//10
        
    while rev>0:
        c=rev%10
        a.append(c)
        rev=rev//10
    
print(*a)