from week02 import Point, Person, Circle, Cylinder 

def tstPerson():
    p1 = Person('Yang', 26)
    p2 = Person('Choi', 1995)
    
    print(p1)
    print(p2)
    print(Person.isAdult(25))
    
    print('------')
    Person.fromYear('Choi',1995)
    print(p2)

def tstPoint():
    p1 = Point()
    p2 = Point(5,5)
    p3 = Point(21,3)
    print(p1,"\n",p2,"\n",p3)
    
def tstCC():
    c1 = Circle(1)
    c2 = Cylinder(34,6)
    print(c1)
    print(c2)       

def main():
    tstCC()
    
 

if __name__ == "__main__":
    main()