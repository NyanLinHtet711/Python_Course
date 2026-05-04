sen=input("Enter:")# You are my sunshine,you are my everything.
rs=""
rp="were"

i=0
while i<len(sen):
    if sen[i:i+3]=="are":
        rs+="were"
        i+=3
        continue
    else:
        rs+=sen[i]
        i+=1

print(rs)
