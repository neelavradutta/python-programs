R = []
while True:
    x = input()

    if x.lower() == "q":
        break

    d = float(x)

    if d <= 0 or d > 42.195:
        print("Invalid Input")
        exit()

    R.append(d)

a=[]
for i in range(len(R)):
    if R[i]<42.195:
        a.append(R[i])

print(sorted(a[-3:])[::-1])