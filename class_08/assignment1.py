st1=list(input("Enter :").split())
c=0
for s in st1:
    if len(s)>=4 and (s[0]==s[-1]):
        c+=1
print(c)