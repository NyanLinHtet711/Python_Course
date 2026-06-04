#6411271 LYNN THIT NYI NYI

str1 = "Avenger 4 END GAME was released in Year 2019"

def sumOfDigitsFromString(strInput):
    sum_digit = 0
    for i in strInput:
        i = i.lower()
        if i.isdigit():
            sum_digit += int(i)
    print(sum_digit)

sumOfDigitsFromString(str1)
