inStr = input("Enter a string: ")
cDigit = input("Enter a digit: ")
check = 0

for digit in inStr:
    if digit != cDigit:
        print("This string DOES NOT contain " + cDigit + " in every adjacent digit in input string.")
        check = -1
        break
    elif digit == cDigit:
       continue

if check == 0:
    print("This string DOES NOT contain " + cDigit + " in every adjacent digit in input string.")

