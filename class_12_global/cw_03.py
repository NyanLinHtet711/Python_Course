def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def combination(n, r):
    return factorial(n) // (factorial(r) * factorial(n - r))


n = int(input("Enter n: "))
r = int(input("Enter r: "))

print("nCr =", combination(n, r))