s1="Write a Java program to sort an array of given integers using Quick sort Algorithm."
lst=s1.split()
small=lst[0]
large=lst[0]


for i in range(len(lst)):
    if len(small)>len(lst[i]):
        small=lst[i]
        
    elif len(lst[i])>len(large):
        large=lst[i]
            
    else:
        pass
        
print(small,large)