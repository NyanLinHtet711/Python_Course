start = int(input("Enter start: "))
end = int(input("Enter end: "))
div = int(input("Enter div: "))

for counter in range(start, end+1):
    if counter % div != 0:
        print(str(counter), end = " ")
    else:
        print ("SKIP", end = "\n")
        
