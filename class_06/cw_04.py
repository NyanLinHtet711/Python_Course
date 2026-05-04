s=input("Enter a sentence:")
rs=""
l=len(s)
j=1
for i in range(l):
    rs+=s[l-j]
    j+=1
print(rs)
