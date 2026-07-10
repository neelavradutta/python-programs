nums = [1,0,0,3,12]

i = 0

for j in range(len(nums)):

    if nums[j] != 0:

        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

        i += 1

print(nums)