a=["Hello","Alaska","Dad","Peace"] 
final=[]
ar=[]
res=["qwertyuiop","asdfghjkl","zxcvbnm"]
for i in range(len(res)):
    b=sorted(res[i])
    ch=""
    for j in range(len(b)):
        ch=ch+b[j]
    ar.append(ch)

for i in range(len(a)):
    Flag=True
    temp=sorted(a[i].lower())
    ch=""
    for j in range(len(temp)):
        ch=ch+temp[j]

    for k in range(len(ar)):
        if ch in ar[k]:
            final.append(a[i])
            break
    


print(final)

