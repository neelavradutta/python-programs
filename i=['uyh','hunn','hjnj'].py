s1="Python Exercises"
count=0
for i in range(len(s1)):
    if s1[i]==" ":
        count=count+1
        
s2=s1.replace(" ","")
print(" "*count+s2)

