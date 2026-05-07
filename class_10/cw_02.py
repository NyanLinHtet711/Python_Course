def DoubleTri(x):
    dx=x**2
    tx=x**3
    return x,dx,tx
x=int(input("x: "))
x,dx,tx=DoubleTri(x)
print("Value of x: ",x)
print("Value of Doublex: ",dx)
print("Value of Triplex: ",tx)