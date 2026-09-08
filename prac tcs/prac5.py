a=[1,2,1]
c=[]
for i in range(len(a)-1,-1,-1):
    c.append(a[i])
if a==c:
    print("pal")
else:
    print("non pal")