n=int(input("Enter number of real number:"))
a=n
total=0
p_total=0
n_total=0
c=1
while n>0:
    num=float(input(f"Enter number #{c} : "))
    total+=num
    if num<0:
        n_total+=num
    else:
        p_total+=num

    n-=1
    c+=1

avg=total/a

print("Average is ",avg)
print("Positive total",p_total)
print("Negative Total",n_total)

    
