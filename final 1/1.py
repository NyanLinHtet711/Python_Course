def f(n):
    temp = [1,3]
            
    for i in range(3,n+1):
        new = 0
        first = temp[i-1-1]
        second = temp[i-2-1]
        new = 3*first + second +4
        temp.append(new)

    for i in range(0,len(temp)):
        print(f"n = {i+1}, f({i+1}) = {temp[i]}")

UInput = int(input("Enter a positive integer: "))
if UInput < 1:
    print("Please enter a positive integer!")
else:
    f(UInput)
