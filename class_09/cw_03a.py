list1=[int(x) for x in input("ENter: ").split()] #2 4 10
list2=[int(x) for x in input("Enter: ").split()] # 1 5 10 20
print("Output#1 is")
def Multiplication(list1,list2):
    for n in list2:
        for m in list1:
            t= n*m
            if t<100:
                print(f"{t:<3}",end="  ")
            else:
                print("***", end="  ")
        print()

    print("Output#2 is")
    for n in list1:
        for m in list2:
            t= n*m
            if t<100:
                print(f"{t:<3}",end="  ")
            else:
                print("***", end="  ")
        print()
Multiplication(list1,list2)