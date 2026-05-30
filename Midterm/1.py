rate = float(input("Conversion rate(BTH/USD): "))
USD = 0
BHT = 0

UInput = int(input("Enter 1 for US Dollar to Thai Baht, enter 2 otherwise: "))
if UInput == 1:
    USD = float(input("US dollar: "))
    BHT = rate * USD
    BHT = round(BHT, 3)
    print(str(USD) + "$ = " + str(BHT)+ " B.")
elif UInput == 2:
    BHT = float(input("Thai Baht: "))
    USD = (1/rate) * BHT
    USD = round(float(USD),3)
    print(str(BHT) + "B = " + str(USD) + " $.")


    
