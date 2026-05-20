
def easyencrypt(letter,shift):
    base=ord("a")
    new=""
    low=letter.lower()
    for i in low:
        c=(ord(i)-base+shift)%26
        j=chr(c+base)
        new+=j
    
    return new

letter=input("Enter a message you want to encrypt:")
shift=int(input("Num you want to shift: "))     
print(easyencrypt(letter,shift))
