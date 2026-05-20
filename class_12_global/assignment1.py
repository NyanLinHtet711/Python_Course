s = input("Enter: ")

def bi(s):

    t = 0

    if s[0] == "0" and len(s) > 1:
        return "wrong input!"

    for i in range(len(s)):

        t += int(s[i]) * (2 ** (len(s)-1-i))

    return t


print(bi(s))