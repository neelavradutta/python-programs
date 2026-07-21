m=int(input())
mat=[]
for i in range(m):
    mat.append(list(map(int,input().split())))

a=0
b=mat[0].count(1)
for i in range(m):
    c=0
    for j in range(len(mat[i])):
        if mat[i][j]==1:
            c=c+1
    if c>b:
        b=c
        a=i

print([a,b])
    
    