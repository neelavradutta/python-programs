word,ch = input().split()
for i in range(len(word)):
    if word[i]==ch:
        print(word[:i+1][::-1]+word[i+1:])
        break
        
if ch not in word:
    print(word)