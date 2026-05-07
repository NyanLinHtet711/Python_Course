def MyBio(name,surname,age):
    if age<5 or age>70:
        print(f'Dear{name} {surname}, You shoud stay at home')
    else:
        print(f'Dear{name} {surname}, You shoud stay at home as much as you can')
age=int(input("Enter age;"))
name=input("Enter name")
surname=input("Enter Surname")
MyBio(name,surname,age)
