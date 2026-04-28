n = int(input("Enter n factorial: "))
total = 1
i = 1
text = ""

if n <= 1:
    print(f"{n}! = 1")
else:
    while i <= n:
        total *= i
        text += str(i)
        if i < n:
            text += " x "
        i += 1

    print(f"{n}! = {text} = {total}")