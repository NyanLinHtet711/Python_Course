def biDirSearch(key, lst):

    c = 0

    while c < len(lst):

        if lst[c] == key:
            print(f"It takes {c+1} time to find {key}")
            return True

        c += 1

    print("Sorry Num not found.")
    return False


key = 4
lst = [2,5,3,4,1]

biDirSearch(key, lst)