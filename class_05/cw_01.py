mul=12
print("      ",end="")
y=1
while y<=mul:
    print(f"x*{y:<4}", end="")
    y+=1
print()
x=1
while x<=mul:
    print(f"x ={x:<2}",end=" ")
    z=1
    while z<=mul:
        result=z*x
        print(f"{result:<3}",end="   ")
        z+=1
    print()
    x+=1