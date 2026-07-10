

s1=input("Enter words ")
n=int(input("Enter the numer of char to be removed "))
s2=""
for i in range(n):
    ch=input("Enter characters ")
    s2=s2+ch
    

s3=""
for i in range(len(s1)):
    if s1[i] not in s2 :
        s3=s3+s1[i]
        
print(s3)
    