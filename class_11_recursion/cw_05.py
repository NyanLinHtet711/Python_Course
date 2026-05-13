def powerx(x,y):
    if y==0:
        return 1
    return x* powerx(x,y-1)
print(powerx(2,3))