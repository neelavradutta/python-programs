nums=list(map(int,input().split()))
key=int(input())
k=int(input())

c=[]
for i in range(len(nums)):
    if nums[i]==key:
        for j in range(len(nums)):
            if abs(j-i)<=k:
                if j not in c:
                    c.append(j)

print(sorted(c))
        
        