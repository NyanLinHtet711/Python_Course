list1 = [6,1,8,2,4,0] 
list2 = [0, 0, 0, 0, 0]
list2[0] = list1[0]

for i in range(len(list1)):
    for j in range(1,len(list2)):
        list2[j] = list1[j] + list2[j-1]

    print(f"list2[{i}] = {list2[i]}")

   
