def biDirSearch(key, lst):
    left=0
    right=len(lst)-1
    c=0
    while left<= right:
        c+=1
        if lst[left]== key:
            print (f"It takes {c} times to get the {key} from the left.")
            return 
        if lst[right]==key:
            print(f"It takes {c} times to get the {key} from the right.")
            return
        left+=1
        right-=1
    print("There is no {key} in the list.")

key=9 
lst=[1,4,2,5,66,4,9,23,5,55,4] 

biDirSearch(key, lst)