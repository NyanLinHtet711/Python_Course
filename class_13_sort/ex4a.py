def foursliceSearch(key, numlist):

    size = len(numlist)

    if size % 4 != 0:
        print("List size must be divisible by 4")
        return

    slice_size = size // 4

    slices = [
        numlist[0:slice_size],
        numlist[slice_size:slice_size*2],
        numlist[slice_size*2:slice_size*3],
        numlist[slice_size*3:]
    ]

    loopcount = 0

    for s in slices:
        loopcount += 1

        if key in s:
            print(f"It takes {loopcount} loops to find {key}")
            return

    print("Sorry a number is not found")


# Example
numlist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]

foursliceSearch(9, numlist)