nums = list(map(int, input().split()))
a=[]
for i in range(len(nums)):
    if nums[i]==1:
        c=1
        for j in range(i+1,len(nums)):
            if nums[j]!=1:
                break
            else:
                c=c+1
        a.append(c)    

print(max(a))