s1=input("enter the sentence ")
s2=input("enter the character to be removed ")
s3=""
for i in range(len(s1)):
    if s1[i]==s2 or s1[i]==s2.capitalize():
        s3=s3+s1[i]
    
print(s3)     

        


