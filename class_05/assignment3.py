a = int(input("a: "))
b = int(input("b: "))

for i in range(a, b + 1):
    s = str(i)

    if s[-1] in ("3", "7"):
        print("*", end=" ")
    elif len(s) < 2:
        print(i, end=" ")
    else:
        t = sum(int(d) for d in s)   
        if t > 7:
            print("%", end=" ")
        else:
            print(i, end=" ")