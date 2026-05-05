inp=input("Input: ").split()
num=int(input("Enter number: "))
l=len(inp)
for i in inp:
    for j in range(1,num+1):
        if j%2==1:
            print(i.lower()+str(j),end=" ")
        else:
            print(i.upper()+str(j),end=" ")
            

