
############################################################################
##
## In this Program user can input like this 1/3 3/8 and perform operation like they need
## Example:-
## 1/4 4/9
##
###########################################################################


from math import log

def Entropy(X,Y):
	return (-(log(X,2)*X)-(log(Y,2)*Y))


from functools import reduce

inp = list(map(lambda x: reduce(lambda x,y:x/y,list(map(lambda b: float(b),x.split('/')))),list(map(str,input().split()))))

print('Entropy:-',Entropy(inp[0],inp[1]))
