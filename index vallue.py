s1 = "The quick brown fox jumps over the lazy dog"
s1 = s1.lower()


for i in "abcdefghijklmnopqrstuvwxyz":
    if i not in s1:
        print("Not all letters present")
        break
else:
    print("All letters present")