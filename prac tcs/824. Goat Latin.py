sentence=input()
sentence=sentence.split()

for i in range(len(sentence)):
    if sentence[i][0] in "aeiouAEIOU":
        sentence[i]=str(sentence[i])+"ma"+"a"*(i+1)
    else:
        sentence[i]=str(sentence[i][1:])+str(sentence[i][0])+"ma"+"a"*(i+1)

print(" ".join(sentence))
    