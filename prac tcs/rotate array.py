k=int(input())
a=list(map(int,input().split()))
for i in range(k):
    a.insert(0,a.pop())

print(a)