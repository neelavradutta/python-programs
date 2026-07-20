import math
gifts=list(map(int,input().split()))
k=int(input())

for i in range(k):
    ind=gifts.index(max(gifts))
    gifts[ind]=math.floor(math.sqrt(max(gifts)))

print(sum(gifts))
    