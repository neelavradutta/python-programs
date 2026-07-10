s="Let's take LeetCode contest"
lst=s.split()
lst1=[]
for i in range(len(lst)):
        lst1.append(lst[i][::-1])

print(" ".join(lst1))