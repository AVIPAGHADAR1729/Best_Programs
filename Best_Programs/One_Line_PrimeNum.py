#_____________________________________________________________________ One Line Prime Numbers List in Python _________________________________________________________________#

def getPrimeList_Comp(N1,N2):
    return [ x for x in range(N1,N2) if (all(x%y!=0 for y in range(2,x))) ]

def getPrimeList_Filter(N1,N2):
    return list(filter(lambda x: all(x%y!=0 for y in range(2,x)),range(N1,N2)))
    

print(getPrimeList_Comp(10,10000))
print(getPrimeList_Filter(10,10000))





#_____________________________________________________________________________________________________________________________________________________________________________#
