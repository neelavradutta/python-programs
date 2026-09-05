
nums =[-71,-71,93,-71,40]
nums=list(set(sorted(nums)))
if len(nums)<3:
    print(0)
else:
    print(len(nums[1:(len(nums)-1)]))