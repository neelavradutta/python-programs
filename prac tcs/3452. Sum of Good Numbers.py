nums = list(map(int, input().split()))
k = int(input())

s = 0

for i in range(len(nums)):
    if (i-k < 0 or nums[i] > nums[i-k]) and (i+k >= len(nums) or nums[i] > nums[i+k]):
        s += nums[i]

print(s)