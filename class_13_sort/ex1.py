def sum37(lst):
    if len(lst)==0:
        return 0
    if lst[0]%3==0 and lst[0]%7==0:
        return lst[0]+ sum37(lst[1:])
    return sum37(lst[1:])
lst=[1,3,5,7,42,21]
print(sum37(lst))
    
    