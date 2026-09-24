a=[]
b=[]
nums = [[1,2,3,6],[5,6,7,7],[9,10,11,8],[4,8,2,3]]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        a.append(nums[i][i])
        break

print(nums[::-1])
nums=nums[::-1]
for i in range(len(nums)):
    for j in range(len(nums[i])):
        b.append(nums[i][i])
        break

print(a)
print(b[::-1])
