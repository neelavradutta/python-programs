s = "A man, a plan, a cnal: Panama"
s=s.lower()
s2=""
for i in range(len(s)):
    if s[i].isalpha()==True:
        s2=s2+s[i]
        
if s2==s2[::-1]:
    print("True")
else:
    print("False")