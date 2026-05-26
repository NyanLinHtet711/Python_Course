def bi(key, lst):

    lst.sort()

    dis = len(lst)

    left = 0
    right = dis - 1

    while left <= right:

        middle = (left + right) // 2

        if key == lst[middle]:
            return True

        elif key < lst[middle]:
            right = middle - 1

        else:
            left = middle + 1

    return False


print(bi(4, [2,5,3,4,1]))