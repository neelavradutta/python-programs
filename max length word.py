n=int(input("enter the number of words to be entered "))

lst=[]
count=0

for i in range(n):
    lst.append(input("enter the words "))
    
    
for i in range(len(lst)):
    if len(lst[i])>count:
        count=len(lst[i])
        s2=lst[i]
    
    else:
        pass
    
print(s2,count)    

    
    
    
