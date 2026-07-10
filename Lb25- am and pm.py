list=['zero','one','two','three','four','five','six','seven','eight','nine']

n=int(input("enter a number "))

for i in range(len(list)):
    if i==n:
        print(list[i])
        break
    
    