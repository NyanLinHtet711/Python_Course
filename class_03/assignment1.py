x1=int(input("Enter x1:"))
x2=int(input("Enter x2:"))
x3=int(input("Enter x3:"))

x4=x1%x3
x5=x2%x3

if x4==0 and x5==0:
    print("x3 is a factor of both x1 and x2 ")
elif x4==0 and x5!=0:
    print("x3 is a factor of x1 ")
elif x4!=0 and x5==0:
    print("x3 is a factor of x2")
else:
    print("x3 is a factor of neither x1 nor x2")

