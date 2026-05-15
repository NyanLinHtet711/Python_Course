# x=1
# def dosmt():
#     global x
#     x=20+5
#     print("value of x inside fun:",x)
# print("valus of x outside fun",x)
# dosmt()
# print("value of x outside fun",x)

def immuetableList(b):
    b+=10
    print("inside",b)
a=100
print("outside",a)
immuetableList(a)
print("outside",a)
