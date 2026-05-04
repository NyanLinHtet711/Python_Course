s=input("Enter a sentence:")

sen=""
for c in s:
    ch=ord(c)
    if (65<= ch <=90) or (97<= ch <=122) or ch==32:
        sen+= c
print(sen)