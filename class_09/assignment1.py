list1=[int(x) for x in input("Enter: ").split()]
list2=[int(x) for x in input("Enter: ").split()]

if len(list1)<len(list2) :
    list3=[]
    for i in list1:
        if i in list2:
            list3.append(i)
    if list3==list1:
        print(f"Yes,list1 is a sublist of list2")
    else:
        print("No")
    
else:
    list3=[]
    for i in list2:
        if i in list1:
            list3.append(i)
    if list3==list2:
        print(f"Yes,list 2 is a sublist of list1")
    else:
        print("No")
    

 # SHORTER VERSION

# list1 = [int(x) for x in input("Enter: ").split()]
# list2 = [int(x) for x in input("Enter: ").split()]

# if len(list1) < len(list2):

#     print(
#         "Yes, list1 is a sublist of list2"
#         if all(i in list2 for i in list1)
#         else "No"
#     )

# else:

#     print(
#         "Yes, list2 is a sublist of list1"
#         if all(i in list1 for i in list2)
#         else "No"
#     )