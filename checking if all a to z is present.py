s1 = "The quick brown fox jumps over the lazy dog"
s1=s1.upper()
s2=""

n=int(input("enter number "))

for i in range(len(s1)):
    if i==n:
        s2=s1[:n].lower()+s1[n:]
        
print(s2)