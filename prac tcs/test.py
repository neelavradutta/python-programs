nums = [1,2,2,3,1,4,2]
a=[]
for i in range(len(nums)):
    a.append(nums.count(nums[i]))


q=[]
for i in range(len(nums)):
    if nums.count(nums[i])==max(a):
        q.append(nums[i])
    

print(list(set(q)))

final=[]
for i in range(len(q)):
    d=[]
    for j in range(len(nums)):
        if q[i]==nums[j]:
            d.append(j)
    final.append(len(nums[min(d):max(d)+1]))

print(min(final))


