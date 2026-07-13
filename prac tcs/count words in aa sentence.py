d=[]
c=[]
n=int(input())
for i in range(n):
    d.append(input())

for i in range(len(d)):
    c.append(len(d[i].split()))

print(max(c))
    
