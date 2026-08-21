s = "10203004"
queries = [[0,7],[1,3],[4,6]]

final = []

for i in range(len(queries)):
    temp = s[queries[i][0]:queries[i][1] + 1]
    temp = temp.replace("0", "")
    
    if temp == "":
        x = 0
    else:
        x = int(temp)

    total = 0

    while x > 0:
        digit = x % 10
        total = total + digit
        x = x // 10

    final.append(total*int(temp)%(10**9+7))

print(final)