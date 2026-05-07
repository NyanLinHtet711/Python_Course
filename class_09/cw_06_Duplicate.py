nlist=[[2,5,99,99],[-3,8,1,2,10],[100,34,10]]

def DuplicateNum(nlist):
    seen=[]
    l=[]
    for sub in nlist:
        out=[]
        for i in sub:
            if i not in seen:
                seen.append(i)
                out.append(i)
        l.append(out)
    
    return l
print(DuplicateNum(nlist))


     


