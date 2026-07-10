s = "is2 sentence4 This1 a3"
lst=s.split()
s2=""
for i in range(len(lst)-1):
    if int(lst[i][-1])>int(lst[i+1][-1]):
        s2=lst[i+1][:len(lst[i+1])-1]+" "+s2

    else:
        s2=s2+lst[i][:len(lst[i])-1]
print(s2)