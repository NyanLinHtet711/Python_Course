number=int(input("Enter a number:"))
num=[int(input(f"Enter number{i+1}: ")) for i in range(number)]
num=sorted(num)

lowest=num[1]-num[0]
for n in range(len(num)-1):
    dif=num[n+1]-num[n]
    if dif<lowest:
        lowest=dif




print(lowest)