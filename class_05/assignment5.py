number1=int(input("Enter a number: "))
number2=int(input("Enter a number: "))

num1=[int(input(f"Enter a number{i+1}: ")) for i in range(number1)]
num2=[int(input(f"Enter a number{i+1}: ")) for i in range(number2)]

listA=num1+num2
listA=sorted(listA)

lowest=listA[1]-listA[0]

for n in range(len(listA)-1):
    dif=listA[n+1]-listA[n]
    if dif<lowest:
        lowest=dif
print(lowest)