str1=list(input("Enter;").split()) #Tom Peter 100 400 Tom 300 100
lst=[]
for w in str1:
    if w in lst:
        continue
    print(w,end=" ")
    lst.append(w)


            