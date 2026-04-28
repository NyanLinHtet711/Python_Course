num=input("Enter a number:")
total=0
for i in num:
    n=int(i)
    even=n%2
    if even ==0:
        total+=n
       
print("The sum of even digit is",total)

