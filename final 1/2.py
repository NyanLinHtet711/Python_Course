def decToNBase(decimal, N):
    if decimal < 0:
        return "No Output!, invalid parameter(s)"
    
    output = ""
    
    while decimal >= 1:
        digit = int(decimal % N)

        ###
        if digit < 10:
            output += str(digit)
        else:
            output += chr(ord('A')+digit-10)
        decimal = int(decimal / N)
        ###
        
    output = output[::-1] #reverse the string
    
    return output

print("**Question 2**")
number = 131
for i in range(2, 17):
    value = decToNBase(number, i)
    print(f"The base {i} of the base 10, {number} is {value}")
print()
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

number = -56
print(decToNBase(number, 5))



