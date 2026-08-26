a="1234567891011"
j=0
for i in range(3,len(a)+1,3):
    print(a[j:i])
    j=i
print(a[j:])