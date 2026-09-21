forts = [1,0,0,-1,0,0,0,0,1]
a=[]
for i in range(len(forts)-1, 0, -1):
    if forts[i] == -1 and 1 in forts[:i]:
        for j in range(i-1, -1, -1):
            if forts[j] == 1:
                a.append(i-j-1)

print(a)