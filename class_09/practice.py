xlist=[]
xlist.append([1,2,3])
xlist.append([4,5,6])
print(xlist)
for i in range(len(xlist)):
    for j in range(len(xlist[i])):
        print(xlist[i][j],end= " ")
    print()
