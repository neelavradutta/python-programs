nums =[31,25,72,79,74]
nums=sorted(nums)
d=[]
for i in range(len(nums)):
    temp=nums[i]
    c=[]
    while temp>0:
        a=temp%10
        c.append(a)
        temp=temp//10
    d.append(max(c))

final=[]
while len(d)>0:
    if d.count(d[0])>1:
        final.append(d[0])
        d.pop(0)
    else:
        d.pop(0)


final=list(set(final))

w=[]
for i in range(len(final)):
    q=[]
    for j in range(len(nums)):
        if final[i] in str(nums[j]):
            q.append(nums[j])
    q=sorted(q)
    w.append(q[-1]+q[-2])

if len(w)==0:
    print(-1)
else:
    print(max(w))

    
