#6411271 LYNN THIT NYI NYI

def f(n):
    temp = [1,3]
            
    for i in range(2,n):
        new = 0
        first = temp[i-1]
        second = temp[i-2]
        new = 3*first + second +4
        temp.append(new)

    for i in range(0,len(temp)):
        print(f"n = {i+1}, f({i+1}) = {temp[i]}")

UInput = int(input("Enter a positive integer: "))

if UInput < 1:
    print("Please enter a positive integer!")
else:
    f(UInput)

'''
FUNCTION METHOD 

def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        return 3*f(n-1)+f(n-2)+4

UInput = int(input("Enter a positive integer: "))
             
if UInput < 1:
    print("Please enter a positive integer!")
else:
    for i in range(1,UInput+1):
        print(f"n = {i},f({i}) = {f(i)}")

'''

