nums=list(map(int,input().split()))
op=0
a=[]
b=[]
for i in range(len(nums)):
    for j in range(i+1,len(nums)+1):
        if len(nums[i:j])%2!=0:
            a.append(sum(nums[i:j]))

print(sum(a))
        

    
        
    
        