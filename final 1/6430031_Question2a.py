#6411271 LYNN THIT NYI NYI

def decToNBase(decimal, N):
    if decimal < 0 or N <= 0:
        return "No Output!, invalid parameter(s)"
    
    output = ""

    ### IMPORTANT ###
    while decimal >= 1: #loop
        digit = int(decimal % N) #integer division

        if digit < 10: #if digit is single digit (<10)
            output += str(digit)
        else: #if digit is two digit (>9)
            output += chr(ord('A')+digit-10) 
        decimal = int(decimal / N) #integer division
    ### IMPORTANT ###
        
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



