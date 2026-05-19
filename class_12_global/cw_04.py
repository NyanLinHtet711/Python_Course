def removeDu(li):
    newli=[]
    seen=set()
    for i in li:
        if i not in seen:
            newli.append(i)
            seen.add(i)
    print("Inside",li)
    return newli
li=[1,1,2,4,5,4,5,9,6,8]
removeDu(li)
li=removeDu(li)
print("Last",li)