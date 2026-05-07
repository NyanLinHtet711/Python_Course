nlist=[[2,5,99,99],[-3,8,1,2,10],[1,7,100,10]]

elist=[]
olist=[]

for sub in nlist:
    odd=[]
    even=[]
    for i in sub:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    elist.append(even)
    olist.append(odd)

print("Output: Evenlist: ",elist)
print("Output: Oddlist: ",olist)
