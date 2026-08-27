nums = [10,20,30,5,10,50]
a=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        a.append(nums[i:j])

print(a)