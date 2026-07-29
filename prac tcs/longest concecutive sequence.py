#6
#100 4 200 1 3 2
#4

n=int(input())
arr=list(map(int,input().split()))
l=[]

if len(arr)==0:
    print(0)
    exit()

for i in range(len(arr)):
    a=arr[i]
    c=1
    while a+1 in arr:
        a=a+1
        c=c+1     
    
    l.append(c)

print(max(l))        
        
        
    
        
        