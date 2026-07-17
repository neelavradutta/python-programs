N=int(input())
nums=list(map(int,input().split()))
answer=[]
flag=True
for i in range(len(nums)):
    p=1
    for j in range(len(nums)):
        if i!=j:
            p=p*nums[j]
            
    answer.append(p)

print(*answer)