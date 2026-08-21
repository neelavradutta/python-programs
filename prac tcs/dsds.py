s = "10203004"
queries = [[0,7],[1,3],[4,6]]

final=[]
for i in range(len(queries)):
    temp=s[queries[i][0]:(queries[i][1])+1]
    temp=temp.replace("0","")
    x=int(temp)
    s=0
    while x>0:
        a=x%10
        s=s+a
        x=x//10
    final.append(s*int(temp))
        
print(final)