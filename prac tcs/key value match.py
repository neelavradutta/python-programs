n=int(input())
items=[]
for i in range(n):
    items.append(input().split())

ruleKey=input()
ruleValue=input()

count=0
temp=0
key=["type", "color", "name"]
for i in range(len(key)):
    if ruleKey==key[i]:
        temp=i

for i in range(len(items)):
    for j in range(len(items[i])):
        if ruleValue==items[i][j] and j==temp:
            count=count+1

print(count)
    