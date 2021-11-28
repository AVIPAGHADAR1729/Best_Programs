# Print Pascal row with few line of clean code
#__________________________ method 1 _________________________________ # 
from math import comb
def pascalRows(N):
    def helper(N):
        return list(map(lambda x: list(map(lambda y: str(comb(x,y)),range(x+1))),range(N+1)))
    return '\n'.join(list(map(lambda row: ' '.join(row),helper(N))))

print(pascalRows(12))

# OUTPUT
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1
# 1 10 45 120 210 252 210 120 45 10 1
# 1 11 55 165 330 462 462 330 165 55 11 1
# 1 12 66 220 495 792 924 792 495 220 66 12 1


#__________________________ method 2 _________________________________ #


#  This Fastest way get Pascal tringle for any max number of row

def FastPascal(N):
    y = [0]
    row = [1]
    for x in range(N):
        row = [ a+b for a,b in zip(row+y,y+row)]
        yield row
        
 
#__________________________________________________________________________________________________________________________________________________________________________ #


#__________________________ MULTIPLY MATRIX AND TRANSPOSE  WITH ONE LINE OF CODE _________________________________ #

class Matrix:
    def __init__(self,mat):
        self.row = len(mat)
        self.col = len(mat[0])
        self.mat = mat
    def transpose(self):
        return [[self.mat[j][i] for j in range(self.row)] for i in range(self.col)]
    def __repr__(self):
        return f'Matrix:<{self.mat}>'
    def multiply(self,B):
        return [
            [sum(a*b for a,b in zip(row,col)) for col in zip(*B.mat) ] for row in self.mat
        ]

M1 = Matrix([[1,3,40],[10,10,50]])
M2 = Matrix([[1,1,5],[10,8,1]])
print(M1)
print(M2)
# MULTIPLY
print(M1.multiply(M2))
# TRANSPOSE
print(M1.transpose())
print(M2.transpose())
