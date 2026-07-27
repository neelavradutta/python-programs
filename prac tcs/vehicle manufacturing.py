#vehicle  manufacturing

v=4
w=10
final=[]
flag=True
for c in range(v+1):
    b=v-c
    if c*4 + b*2 == w:
        final.append(c)
        final.append(b)
        flag=False
        break

if flag==True:
    print(-1)
else:
    print(*final)