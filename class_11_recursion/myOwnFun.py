def SplitType(numlist):
    fl=[]
    il=[]
    for i in numlist:
        if i.isfloat():
            fl.append(i)
        else:
            il.append(i)
    return fl,il 
def oddlist(numlist):
    ol=[]
    if len(numlist)==0:
        return []
    if numlist[0]%2!=0:
        return [numlist[0]]+oddlist(numlist[1:])
    return oddlist[1:]


