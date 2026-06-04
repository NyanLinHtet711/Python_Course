listA = [1, 3, 60, 73, 7, 88, 50, 13, 20, 98, 100, 2, 35, 40, 9]
list1 = []
list2 = []

for each in listA:
    if each <= 50:
        list1.append(each)
    else:
        list2.append(each)

list1.sort()
list2.sort()


print(f"list1 → {list1}")
print(f"list2 → {list2}")
