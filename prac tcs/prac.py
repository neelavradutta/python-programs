s=input()
goal=input()

s=list(s)
goal=list(goal)
flag=0
for i in range(len(s)):
    if s!=goal:
        s.append(s.pop(0))
    else:
        flag=1
        break

if flag==1:
    print(True)
else:
    print(False)
