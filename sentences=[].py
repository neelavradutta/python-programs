allowed = "ab"
words = ["ad","bd","aaab","baa","badab"]

count=0
for i in words:
    c=True
    for j in i:
        if j not in allowed:
            c=False
            break
    
        else:
            count=count+1

print(count)