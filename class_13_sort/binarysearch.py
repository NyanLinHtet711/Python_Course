def bisearch(key, lst):

    lst.sort()

    dis = len(lst)

    left = 0
    right = dis - 1
    c=0

    while left <= right:
        c+=1

        middle = (left + right) // 2

        if key == lst[middle]:
            print(f"It takes {c} to reach.")
            return 

        elif key < lst[middle]:
            right = middle - 1

        else:
            left = middle + 1

    return False


