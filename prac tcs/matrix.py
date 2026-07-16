m=int(input())
n=[]
for i in range(m):
    n.append(list(map(int,input().split())))

for i in range(m):
    for j in range(len(n)+1):
        print(n[i][j], end=" ")
    print()
    