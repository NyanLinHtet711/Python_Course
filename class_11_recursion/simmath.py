def fac(n):
    if n<=1:
        return 1
    return n*fac(n-1)

def avgList(lst):
    return sum(lst)/len(lst)
   
def sumodd(numlst):
    if len(numlst)==0:
        return 0
    return numlst[0]+sumodd(numlst[2:])
def sumeven(numlst):
    if len(numlst)<2:
        return 0
    return numlst[0]+sumeven(numlst[2:])

