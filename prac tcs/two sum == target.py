n=int(input())
r=list(map(int,input().split()))
target=int(input())
final=[]
flag=True
for i in range(len(r)):
    for j in range(len(r)):
        if r[i]+r[j]==target and i!=j:
            final.append(i)
            final.append(j)
            flag=False
            break
        
    if flag==False:
        break
    
print(final)
