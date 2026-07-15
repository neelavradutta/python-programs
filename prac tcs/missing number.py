n = [0, 1]
missing=[]
for i in range(sorted(n)[0],sorted(n)[-1]):
    if i not in n:
        missing.append(i)
if len(missing)>1:
    print(missing)
else:
    print("empty or",n[-1]+1)
        