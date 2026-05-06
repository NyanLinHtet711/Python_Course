list1=[int(x) for x in input("Enter").split()]
list2=[int(x) for x in input("Enter").split()]

def subList(list1,list2):
    l=[]
    for i in list1:
        if i in list2:
            l.append(i)
    if l==list1:
        print("Yes")
    else:
        print("No")
subList(list1,list2)
                
