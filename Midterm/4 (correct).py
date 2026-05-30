num = input("Enter credit card number: ")
cDigit = int(num[15])
total = 0

for i in range (len(num)-1):
    if i%2 == 0:
        temp = 2*int(num[i])
        if temp > 9:
            temp = int(temp/10) + int(temp%10)
            total += int(temp)
        else:
            total += int(temp)
    else:
        total += int(num[i])
        
total += cDigit
if total%10 == 0 :
    print ("Valid credit card number.")
else:
    print("Invalid credit card number.")

