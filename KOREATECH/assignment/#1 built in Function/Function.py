class Functions:
    @staticmethod
    def getFactorial(n):
        if n == 0:
            return 1
        else:
            return n * Functions.getFactorial(n - 1)

    @staticmethod
    def drawTriangles(height):
        if height <= 0:
            print("Height must be a positive integer.")
            return

        for i in range(height, 0, -1):
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
            
        print("")

        for i in range(1, height + 1):
            spaces = " " * (height - i)
            stars = "*" * (2 * i - 1)
            print(spaces + stars)
            
    @staticmethod
    def getTriples(limit):
        triples = []
        for side1 in range(1, limit + 1):
            for side2 in range(side1, limit + 1):
                hypotenuse = (side1 ** 2 + side2 ** 2) ** 0.5
                if hypotenuse.is_integer() and hypotenuse <= limit:
                    triples.append((side1, side2, int(hypotenuse)))
        return triples
    
# Result
# 5! = 120
# *********
#  *******
#   *****
#    ***
#     *

#     *
#    ***
#   *****
#  *******
# *********
# (3, 4, 5)
# (5, 12, 13)
# (6, 8, 10)
# (7, 24, 25)
# (8, 15, 17)
# (9, 12, 15)
# (9, 40, 41)
# (10, 24, 26)
# (12, 16, 20)
# (12, 35, 37)
# (14, 48, 50)
# (15, 20, 25)
# (15, 36, 39)
# ...
# (21, 28, 35)
# (24, 32, 40)
# (27, 36, 45)
# (30, 40, 50)    