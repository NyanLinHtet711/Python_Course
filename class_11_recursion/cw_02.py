def list_sum(num):
    if len(num)==0:
        return 0
    return num[0]+list_sum(num[1:])

print(list_sum([1,2,3,4,5]))