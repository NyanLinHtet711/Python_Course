UInput = input("Enter a number: ")
num = int(UInput)
outstr = "The result(s) are/is "
outstr2 = "No results."

if num == 3:
    outstr += "3."
    print(outstr)
elif num >= 3:
    outstr += "3"
    for each_num in range (4, num+1):
        if each_num%3==0 or each_num%5==0 or each_num%6==0:
            outstr += ", " + str(each_num)
        if each_num == num:
            outstr += "."
    print(outstr)
else:
    print(outstr2)

        
