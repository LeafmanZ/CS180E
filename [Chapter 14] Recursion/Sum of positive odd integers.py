def oddSum(n):
    if n == 0:
        return 0
    elif n%2 == 0:
        return oddSum(n-1)
    else:
        return n + oddSum(n-1)
print(oddSum(3))
