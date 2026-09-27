nums = [1,2,10,5,7]
for i in range(len(nums)-1):
    temp = nums[:i] + nums[i+1:]
    print(temp)

temp = nums[:-1]
print(temp)
