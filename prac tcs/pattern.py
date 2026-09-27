caption = "Leetcode daily streak achieved"
s=caption.split(" ")
ch="#"
for i in range(len(s)):
    temp=s[i].capitalize()
    ch=ch+temp

a=caption[0].lower()
ch=ch[:1]+a+ch[2:]
print(ch)