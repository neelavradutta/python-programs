nums = [0,0,1,1,1,2,2,3,3,4]
if not nums:
    print(0)

k = 1

for i in range(1, len(nums)):
    if nums[i] != nums[i - 1]:
        nums[k] = nums[i]
        k += 1

print(k)