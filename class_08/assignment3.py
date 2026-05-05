inp=input("Input: ").split()
num=int(input("Enter number: "))
l=len(inp)
for i in inp:
    for j in range(1,num+1):
        print(i.upper()+str(j),end=" ")
    
