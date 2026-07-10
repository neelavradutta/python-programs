import array
lst=array.array('i',[4,5,3,8,2,3])
a=0
s1=""
for i in range(len(lst)-1):
    for j in range(i+1,len(lst)):
        if lst[i]*lst[j]>a:
            a=lst[i]*lst[j]
            s1=str(lst[i])+","+str(lst[j])
            
print("("+s1+")",a)
print(set(lst))



        
    