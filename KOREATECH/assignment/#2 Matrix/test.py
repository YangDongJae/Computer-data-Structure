import random

class Matrix():
    rng = random.Random()
    def __init__(self,row,col,f):
        self.M =  []

        if f == 'r':
            self.rMatrix(row,col)
            
        elif f == 'z':
            self.zMatrix(row,col)
            
    def rMatrix(row,col):
        for _ in range (row):
            self.M.append([rng.randint(1,10) for _ in range (col)])
            
    
        