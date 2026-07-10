x=input()
c=[]
word=input().split()
for i in range(len(word)):
    if x in word[i]:
        c.append(i)

print(c)