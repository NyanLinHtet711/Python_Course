letter = input("Enter message: ")
shift = int(input("Shift: "))


def caesar(text, shift):
    new = ""

    for i in text:

        if i.isalpha():

            base = ord("a") if i.islower() else ord("A")

            c = (ord(i) - base + shift) % 26

            new += chr(c + base)

        else:
            new += i

    return new


en_str = caesar(letter, shift)
print(en_str)

de_str = caesar(en_str, -shift)
print(de_str)