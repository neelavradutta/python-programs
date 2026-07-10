s1="PythonExercises"

s3=s1[0]
for i in range(1,len(s1)):
    if s1[i].isupper()==True:
        s3=s3+" "+s1[i]
        
    else:
        s3=s3+s1[i]
        
print(s3)