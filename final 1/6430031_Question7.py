#6411271 LYNN THIT NYI NYI

def ProductX(num_list):

    tocount = True
    total = 1

    temp = []

    ### IF ONLY ONE ZERO ###
    c = 0
    for i in range(len(num_list)):
        if num_list[i] == 0:
            c += 1
    if c == 1:
        num_list.remove(0)
        totalx = 1
        for each in num_list:
            if each > 0 and each < 9:
                totalx = totalx * each
        return totalx
    ### ###
    
    
    for i in range(len(num_list)):
        
        if num_list[i] != 0 and num_list[i] > 0 and num_list[i] < 9 and tocount == True:
            total *= num_list[i]
        elif num_list[i] != 0 and num_list[i] > 0 and num_list[i] < 9 and tocount == False:
            if num_list[i]%2 != 0:
                total *= num_list[i]
    
        elif num_list[i] == 0 and tocount == True:
            tocount = False
            
        elif num_list[i] == 0 and tocount == False:
            for j in range (i+1, len(num_list)):
                tocount = True
                if num_list[j] == 0:
                    tocount = False
                    break
    return total

print(ProductX([2,3,15,0,2,3,0,7,4,0]))    
print(ProductX([0,23,5,8,4]))
print(ProductX([2,0,15,4,2,0,0,5]))

