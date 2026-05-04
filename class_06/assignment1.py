num = input("Enter sentence with CAP: ")

new = ""

for i in range(len(num)):

    if num[i].isalpha():

        new_char = ord(num[i]) + 3

        if new_char > ord("Z"):
            new_char -= 26

        new += chr(new_char)

    else:
        new += num[i]

print(new)