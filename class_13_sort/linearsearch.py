def linear(key,lst):
    dis=len(lst)
    i=0
    while i<dis:
        if lst[i]==key:
            return True
        i+=1
    return False
key=4
lst=[2,5,3,4,1]
print(lin