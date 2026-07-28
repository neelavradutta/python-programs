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

# Exclude finishers
R = [i for i in R if i != 42.195]

# Sort in descending order
R.sort(reverse=True)

# Print top 3 (or fewer)
print("Highest Distance excluding Finishers:")
print(R[:3])