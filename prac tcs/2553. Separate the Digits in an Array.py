nums = list(map(int, input().split()))

c=[]
for i in range(len(nums)):
    a=str(nums[i])
    for i in range(len(a)):
        c.append(int(a[i]))
        
print(*c)
