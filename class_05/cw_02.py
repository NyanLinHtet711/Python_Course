# Using for loop instead of while Loop
mul=12
print("        ",end="")
z=1
for z in range(1,mul+1):
    print(f"x*{z:<2}",end="  ")
print()
y=1
for y in range(1,mul+1):
    print(f"x = {y:<2}",end="  ")
    x=1

    for x in range(1,mul+1):
        result=x*y
        print(f"{result:<3}",end="   ")
    print()