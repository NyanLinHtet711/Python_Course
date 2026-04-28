shop=float(input("Enter shopping amount:"))
hour=float(input("Enter hours: "))
minute=float(input("Enter minutes: "))

total_min=(hour*60)+minute
pay_rate=round(total_min/30)
if shop<=500:
    dis=pay_rate-2
    pay=dis*30
    print(f'The parking fee is free for the first hour.You have to pay {pay} for the parking fee')
elif shop>=1500:
    if pay_rate<=4:
        print(f"Parking is free")
    else:
        print(f'Parking fee is 30 Baht')
else:
    dis=pay_rate-4
    pay=dis*30
    print(f'The parking fee is free for the first hour.You have to pay {pay} for the parking fee')
