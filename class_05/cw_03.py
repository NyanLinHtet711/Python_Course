a=int(input("Enter n: "))
b=int(input("Enter x: "))

for i in range(a,b+1):
    y=str(i)
    if y[-1] == "3" or y[-1]=="7":
        print("*",end=" ")
    else:
        print(y,end=" ")