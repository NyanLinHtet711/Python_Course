list1 = [int(x) for x in input("Enter: ").split()]
list2 = [int(x) for x in input("Enter: ").split()]
list3 = [int(x) for x in input("Enter: ").split()]

def ReplaceElement(list1, list2, list3):
    return list2 + list1[1:-1] + list3

print(ReplaceElement(list1, list2, list3))