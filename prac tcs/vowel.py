word=input().split()
left,right=map(int,input().split())
ref="aeiouAEIOU"
c=0
for i in range(left,right+1):
    if word[i][0] in ref and word[i][-1] in ref:
        c=c+1

print(c)
        
        
    

        