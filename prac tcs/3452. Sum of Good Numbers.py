nums = list(map(int, input().split()))
k = int(input())

s = 0

for i in range(len(nums)):
    if (0 <= i-k < len(nums)) and (0 <= i+k < len(nums)):
        if nums[i] > nums[i-k] and nums[i] > nums[i+k]:
            s += nums[i]

    elif (i-k < 0) and (i+k >= len(nums)):
        s += nums[i]

print(s)