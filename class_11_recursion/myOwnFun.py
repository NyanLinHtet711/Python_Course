def SplitType(numlist):
    fl=[]
    il=[]
    for i in numlist:
        if isinstance(i,int):
            il.append(i)
        else:
            fl.append(i)
    return fl,il 
def oddlist(numlist):
   
    if len(numlist)==0:
        return []
    if numlist[0]%2!=0:
        return [numlist[0]]+oddlist(numlist[1:])
    return oddlist(numlist[1:])

def dul_int(numlist): # [1,2,3,3,4,5,4]
    dlist=[]
    seen1=[]
    seen2=[]
    for i in numlist:
        if i not in seen1:
            seen1.append(i)
            dlist.append(i)
        elif i not in seen2:
            seen2.append(i)
            dlist.append(i)
    return dlist



