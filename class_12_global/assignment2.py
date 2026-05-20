def easyencrypt(letter, shift, dire):

    n = ""

    for i in letter:

        if i.isalpha():

            base = ord("a") if i.islower() else ord("A")

            if dire == "r":
                c = (ord(i) - base + shift) % 26

            elif dire == "l":
                c = (ord(i) - base - shift) % 26

            n += chr(c + base)

        else:
            n += i

    return n


letter = input("Enter: ")
shift = int(input("Enter shift: "))
dire = input("Direction (r/l): ")

en = easyencrypt(letter, shift, dire)

print(en)