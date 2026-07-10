s1="Count the lowercase letters in the said list of words:"

lst=s1.split()
for i in range(len(lst)):
    if len(lst[i])>=5:
        lst[i]="#"*len(lst[i])

print(lst)        


