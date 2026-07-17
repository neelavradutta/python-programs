m,t=map(int,input().split())
n=[]
for i in range(m):
    n.append(list(map(int,input().split())))

a=0
for i in range(m):
    count=0
    for j in range(t):
        if n[i][j]==1:
           count=count+1
    if count>a:
        a=count
        b=i

        
print(b)
    