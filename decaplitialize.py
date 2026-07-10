s1="hello world"

lst=s1.split()
conform=False
for i in lst:
    if lst.count(i)>1:
        conform=True
        
if conform==True:        
    print("True")
else:
    print("False")