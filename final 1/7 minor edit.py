def ProductX(num_list):

    tocount = True
    total = 1
    totalx = 1

    temp = []

    c = 0
    
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

    
print(ProductX([2,0,15,4,2,0,0,5]))
print(ProductX([0,23,5,8,4]))
print(ProductX([2,3,15,0,2,3,0,7,4,0]))
