# def carName(*cars):
#     print("Car instock"+ cars[2])
# carName("Toyota","BMW","Marcede","Nissan")


def Oddsum(num):
    count=0
    for i in num:
        if i % 2 ==1 and(5< i < 20):
            count+=i
    return count 
num=[int(x) for x in input("Enter: ").split()]
count=Oddsum(num)
print(count)
            
