deck = [1,1,1,2,2,2,3,3]
a=[]
deck=sorted(deck)
k=0
for i in range(len(deck)-1):
    if deck[i+1]!=deck[i]:
        a.append(deck[k:i+1])
        k=i+1

a.append(deck[k:])

print(a)