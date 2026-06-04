#6411271 LYNN THIT NYI NYI

def separateChar(myStr):
    str1 = ''
    upper_char = ''
    lower_char = ''
    digit_char = ''

    str1 += myStr
    for each in str1:
        if each.isupper():
            upper_char += each
        elif each.islower():
            lower_char += each
        elif each.isdigit():
            digit_char += each

    print(upper_char)
    print(lower_char)
    print(digit_char)
    
print("**Question 4**")
str1 = "Avenger 4 END GAME was released in Year 2019"
separateChar(str1)
print("= = = = = = = =")
str2 = "I am 109 years old"
separateChar(str2)
print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
