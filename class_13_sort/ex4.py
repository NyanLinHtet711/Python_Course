import binarysearch

def foursliceSearch(key,lst):
    dis=len(lst)
    c=0
    if dis%4==0:
        for i in range(4,dis-1,4):
            s=0
            c+=1
            for j in range(s,i):
                s+=4
                if lst[j]==key:
                    print(f"It takes {c} times to reach {key}")
                    return
    print("The list is not divided by 4")
key=9
lst=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
foursliceSearch(key,lst)
binarysearch.bisearch(key,lst)
