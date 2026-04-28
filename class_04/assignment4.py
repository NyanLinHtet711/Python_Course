fst_int=int(input("Enter first int:"))
sec_int=int(input("Enter second int:"))
text=""
if sec_int > fst_int:
    for i in range(fst_int,sec_int+1):
        text += str(i)
        text+=" "
    print(text)
else:
    for i in range(fst_int,sec_int-1,-1):
        text += str(i)+" "
    print(text)

