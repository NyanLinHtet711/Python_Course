n = int(input("Enter number: "))
c = 0
s = 0
i = 0

while c < n+1:
    if (c%3==0 or c%5==0 or c%6==0) and c != 0:
        s = s + c
        i += 1
        while i < 2:
            i +=1
            print ("The results are ", end="")
        print (str(c), end=", ")
    c+=1

#I dont know how to add full stop at the end instead of comma 

if s == 0:
    print ("No results.")
else:
    print ()
    print ("The sum is " + str(s))
