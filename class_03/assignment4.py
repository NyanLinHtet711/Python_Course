num = input("Enter 5-digit Number: ")

if len(num) != 5:
    print("Not 5-digit Number!")
else:
    total = sum(int(num[i]) for i in [0, 1, 3, 4])
    
    if total < int(num[2]):
        result = num[4] + num[1] + num[2] + num[3] + num[0]
    elif total > int(num[2]):
        result = num[0] + num[3] + num[2] + num[1] + num[4]
    else:
        result = num

    print("The output is", result)