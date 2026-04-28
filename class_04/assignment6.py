lst=[int(input(f"Number#{i+1}: "))for i in range(int(input("Enter number of real number:")))]
fh=sh=float("-inf")
if len(lst)==1:
    print (f"Th first Highest number is{lst[0]}")
    print("There is no second number")

else:
    for n in lst:
        if n>fh:
            sh=fh
            fh=n
        elif n!=fh and n > sh:
            sh=n

    print (f"The first Highest number is{fh}")
    print("The second highest number is",sh)
        
