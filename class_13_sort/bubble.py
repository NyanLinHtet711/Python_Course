ls=[3,1,5,2]
n=len(ls)
for i in range(n):
    for j in range(0,n-i-1):
        if ls[j]>ls[j+1]:
            ls[j+1],ls[j]=ls[j],ls[j+1]
