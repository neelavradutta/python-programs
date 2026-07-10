tup=(1,4,9,16,25,36,49,64,81,100)

x=int(input("enter a number:"))
for i in tup:
    if i==x:
        print("found")
        break 
else:
    print("not found")
    