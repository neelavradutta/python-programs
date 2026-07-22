n=int(input())
grid=[]
for i in range(n):
    grid.append(list(map(int,input().split())))
    
ch=0
c=0
for i in range(len(grid)):
    if grid[i].count(1)>c:
        c=grid[i].count(1)
        ch=i

print(ch)
            
    