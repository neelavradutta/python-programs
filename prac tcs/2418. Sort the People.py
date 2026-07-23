n=int(input())
names=list(map(str,input().split()))
heights=list(map(int,input().split()))

ab=[]
while ab!=heights:
    ab=heights.copy()
    for i in range(len(heights)-1):
        if heights[i+1]>heights[i]:
            a=heights[i]
            b=names[i]
            heights[i]=heights[i+1]
            names[i]=names[i+1]
            heights[i+1]=a
            names[i+1]=b

print(*heights,*names)
