n1=int(input("Enter n1:"))
n2=int(input("Enter n2:"))
n3=int(input("Enter n3:"))
n4=int(input("Enter n4:"))

total=n1+n2+n3+n4
if total < 0:
    if total%2==0 :
        print("The sum is ",total)
        print(total,"is nrgative even")

    else:
        print("The sum is ",total)
        print(total,"is negative odd")
elif total> 0:
    if total%2==0 :
        print("The sum is ",total)
        print(total,"is positive even")

    else:
        print("The sum is ",total)
        print(total,"is positive odd")
else:
    print("The sum is 0")
    print("0 is zero")
