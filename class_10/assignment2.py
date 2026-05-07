def Distance(dis):
    kmm=""
    mile=""
    if "km" in dis:
        d=""
        for i in dis:
            if i.isdigit():
                d+=i 
        mil=int(d)*0.621371
        mile+=f'{dis} is equal to {round(mil)} miles'
    if "mi" in dis:
        d=""
        for i in dis:
            if i.isdigit():
                d+=i 
        km=int(d)*1.6
        kmm+=f'{dis} is equal to {round(km)} km'
    return mile,kmm
        

dis=input("Enter distance:")
mile,kmm=Distance(dis)

print(mile)
print(kmm)