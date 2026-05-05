n=int(input("Enter a number: "))
num=[int(input(f"Enter:{i+1}")) for i in range(n)]
maxnum=1
a=0
for j in num:
    if num[a]>maxnum:
        maxnum=num[a]
        a+=1
print(maxnum)

