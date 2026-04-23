gas=int(input("Enter remaining gas:"))
rate=int(input("Enter comsumption rate:"))
distance=int(input("Enter a traveling distance:"))

n_gas= distance/rate
if n_gas<gas:
    r_gas= gas-n_gas
    print("Still have",r_gas,"litre in the tank")
else:
    r_gas= n_gas-gas
    print("You need",r_gas,"more litre to reach the distination")

