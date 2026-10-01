nums = [2, 3, 2, 3, 4, 3, 2]

d={}
for i in range(len(nums)):
    if nums[i] in d:
        d[nums[i]]=d[nums[i]]+1
    else:
        d[nums[i]]=1

for i in range(len(nums)):
    if d[nums[i]]==max(d.values()):
        print(nums[i])
        break


