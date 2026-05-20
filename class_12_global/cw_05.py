def removeDu(li):
    newli=[]
    seen=set()
    for i in li:
        if i not in seen:
            seen.add(i)
            newli.append(i)
        else:
            if i%2==0:
                j=i*20
                newli.append(j)
            else:
                j=i*10
                newli.append(j)
    print("Inside",li)
    return newli
li=[1,1,3,5,4,5,4,9,4,8,6]

print("Last",removeDu(li))