def sum_n(n):
    if n == 0:   # base case
        return 0
    return sum_n(n-1)

n = int(input("Enter a number: "))
print("Sum =", sum_n(n))