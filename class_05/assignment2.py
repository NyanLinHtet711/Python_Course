for i in range(31):
    if i in range(10,16) or i in range(20,26):
        print("-",end=" ")
    else:
        if i%3==0:
            print(i,end=" ")
        else:
            print("*",end=" ")