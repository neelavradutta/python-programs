s="abcabcbb"
lst=[]
l=[]
for i in range(len(s)):
    for j in range(i+1,len(s)+1):
            lst.append(s[i:j])

for i in lst:
    if len(i)==len(set(i)):
        l.append(i)

print(max(l,key=len))
            