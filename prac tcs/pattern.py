nums = [1, 2, 2, 3, 1, 4, 2]
dict={}
for i in range(len(nums)):
    if nums[i] in dict:
        dict[nums[i]]=dict[nums[i]]+1
    else:
        dict[nums[i]]=1
    

print(dict)