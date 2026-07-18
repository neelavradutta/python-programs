words=input().split()
pref=input()
c=0
for i in range(len(words)):
    if words[i][:len(pref)]==pref:
        c=c+1

print(c)