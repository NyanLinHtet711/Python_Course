list1=[int(x) for x in input("Enter: ").split()]
list2=[int(x) for x in input("Enter: ").split()]
l=[]
if len(list1)< len(list2):
    for i in list1:
        if i in list2:
            l.append(i)
    if l==list1:
        print("Yes")
    else:
        print("No")
else:
    print("list1 must be smaller than list2")
