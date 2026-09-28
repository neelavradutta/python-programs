temp=word.count(word[0])
for i in range(len(w)):
    if temp!=word.count(w[i]):
        od=od+1
    else:
        ev=ev+1