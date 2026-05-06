numList=[1,2.4,"Three",4,5.5,"Six",100,44.5]

def SeparateList(numList):
    strList=[]
    intList=[]
    floatList=[]
    for i in numList:
        if str(i).isalpha():
            strList.append(i)
            
        elif str(i).isdigit():
            intList.append(i)
            
        else:
            floatList.append(i)
    return strList,intList,floatList
          

strList,intList,floatList=SeparateList(numList)
print(strList)
print(intList)
print(floatList)