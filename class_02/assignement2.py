num= input("Enter a  3-digit number: ")
total=0
rev_num=""
n1=num[0]
n2=num[1]
n3=num[2]
rev_num=n3+n2+n1
for n in num:
    total+=int(n)
print("New number is ",rev_num)   
print(total)
