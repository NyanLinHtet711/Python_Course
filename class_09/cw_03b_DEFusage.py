list1=[int(x) for x in input("ENter: ").split()] #2 4 10
list2=[int(x) for x in input("Enter: ").split()] # 1 5 10 20

def Multiplication(list1,list2):
    out1=""
    out2=""
    for n in list2:
        for m in list1:
            t= n*m
            if t<100:
                out1+=f"{t:<3} "
            else:
                out1+= "*** "
        out1+="\n"

    print("Output#2 is")
    for n in list1:
        for m in list2:
            t= n*m
            
            if t<100:
                out2+=f"{t:<3} "
            else:
                out2+="*** "
        out2+="\n"
    return out1,out2           
        
out1,out2=Multiplication(list1,list2)
print("Output#1 is")
print(out1)
print("Output#1 is")
print(out2)