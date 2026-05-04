sen=input("Enter:")
ac=0
uc=0
lc=0
nc=0
c=0
for s in sen:
    if s.isalpha():
        ac+=1
        if s.isupper():
            uc+=1
        elif s.islower():
            lc+=1
    elif s.isdigit():
        nc+=1
    else:
        c+=1
print("Alpha",ac)
print("Upper",uc)
print("Lower",lc)
print("Number",nc)
print("-",c)



    
