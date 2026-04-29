for i in range(1,10):
    print(f"Row number {i}:",end=" ")
    for j in range(1,10,):
        if j in [1,5,9] and i in [1,5,9]:
            print(j,end=" ")
        else:
            print(" ",end="")
    print()
