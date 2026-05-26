def teven(lst):
    if len(lst)==0:
        return 0
    if lst[0]%2==0:
        return 1+ teven(lst[1:])
    return teven(lst[1:])
lst=[1,2,3,4,5,6,7,8]
print(teven(lst))