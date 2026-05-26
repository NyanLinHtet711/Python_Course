def bidir(key, lst):

    l = 0
    r = len(lst) - 1

    while l <= r:

        if key == lst[l]:
            return True

        if key == lst[r]:
            return True

        l += 1
        r -= 1

    return False


def slice4(key, lst):

    dis = len(lst)

    if dis < 4:
        print("List must be larger than 4")
        return

    size = dis // 4

    slices = [
        lst[0:size],
        lst[size:size*2],
        lst[size*2:size*3],
        lst[size*3:]
    ]

    cot = 0

    for j in slices:

        cot += 1

        if bidir(key, j):
            print(f"It takes {cot} times to find {key}.")
            return

    print("Not Found.")


key = 9

lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

slice4(key, lst)