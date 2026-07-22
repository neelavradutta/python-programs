num=input()
arr=[]
for i in range(len(num)-2):
    if len(num[i:i+3])==3 and (num[i]==num[i+1]==num[i+2]):
        arr.append(num[i:i+3])
        
if len(arr)>0:
    print(max(arr))
else:
    print("")
    

