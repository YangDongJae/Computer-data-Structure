from datetime import date

class Point:
    def __init__(self,x = 0, y = 0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '({},{})'.format(self.x, self.y)
    
    def __repr__(self):
        return '({},{})'.format(self.x, self.y)  
    
    def __add__(self, other):
        return Point(self.x + other.x ,self.y + other.y)
    
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    
    def length(self, other):
        return Point((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
        # what's meaning of the legnth? 
    
    def distance(self, p):
        return Point((self.x - p.x)**2 + (self.y - p.y)**2)**0.5    
        
    
    def translate(self, a, b):
        return Point(self.x - a, self.y - b)
        
class Person:
    def __init__(self, name =' ', age =0):
        self.name = name
        self.age = age
        
    def __str__(self):
        return '({},{})'.format(self.name, self.age)
        
    @staticmethod
    def isAdult(age):
        return age > 18
    
    @classmethod
    def fromYear(cls, name, p_year):
        return cls(name, date.today().year - p_year)
    
class Circle:
    def __init__(self, r = 1):
        self.r = r
        
    def __str__(self):
        return 'Circle({})'.format(self.r)
    
    def getArea(self):
        pass
    
class Cylinder(Circle):
    def __init__(self, r = 1, h = 1):
        super().__init__(r)
        self.h = h
        
    def __str__(self):
        return 'Cylinder({},{})'.format(self.r, self.h)
    
    def getVolume():
        pass
        
    