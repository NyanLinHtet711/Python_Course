nlist=[[2,5,99],[3,-2,78],[100,34,9]]
def Findmax(nlist):
    l=[]
    nv=0
    for i in nlist:
        l+=i
    mv=l[0]
    nv=l[0]
    for j in l:
        if j>mv:
            mv=j
        if j<nv:
            nv=j
    
    return mv,nv
mv,nv=Findmax(nlist)
print("Max value is ",mv)
print("Min value is ",nv)

