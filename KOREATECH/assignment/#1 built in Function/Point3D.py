import math

class Point3D:
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

    def __repr__(self):
        return f"Point3D({self.x}, {self.y}, {self.z})"

    def setCord(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def length(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    @staticmethod
    def distance(p1, p2):
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        dz = p2.z - p1.z
        return math.sqrt(dx**2 + dy**2 + dz**2)

    def translate(self, a, b, c):
        self.x += a
        self.y += b
        self.z += c
        
    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)
        else:
            raise TypeError("Unsupported operand type for -")

    def __eq__(self, other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Point3D):
            return self.length() > other.length()
        else:
            raise TypeError("Unsupported operand type for >")

    def __le__(self, other):
        if isinstance(other, Point3D):
            return not self.__gt__(other)
        else:
            raise TypeError("Unsupported operand type for <=")


if __name__ == "__main__":
    p1 = Point3D(1.0, 2.0, 3.0)
    print("Point p1:", p1)

    p2 = Point3D(4.0, 5.0, 6.0)
    print("Point p2:", p2)

    p1.setCord(7.0, 8.0, 9.0)
    print("Updated Point p1:", p1)

    length_p1 = p1.length()
    print("Length of p1:", length_p1)

    distance_p1_p2 = Point3D.distance(p1, p2)
    print("Distance between p1 and p2:", distance_p1_p2)

    p1.translate(1.0, -1.0, 2.0)
    print("Translated Point p1:", p1)

    # Test addition
    result_add = p1 + p2
    print("Addition:", result_add)

    # Test subtraction
    result_sub = p1 - p2
    print("Subtraction:", result_sub)

    # Test equality
    p3 = Point3D(7.0, 8.0, 9.0)  # Create another point with the same coordinates as p1
    print("Equality Test (p1 == p3):", p1 == p3)
    print("Equality Test (p1 == p2):", p1 == p2)

    # Test greater than
    p4 = Point3D(5.0, 0.0, 0.0)  # Create another point
    print("Greater Than Test (p1 > p4):", p1 > p4)
    print("Greater Than Test (p2 > p1):", p2 > p1)

    # Test less than or equal to
    p5 = Point3D(10.0, 10.0, 10.0)  # Create another point
    print("Less Than or Equal To Test (p5 <= p1):", p5 <= p1)
    print("Less Than or Equal To Test (p1 <= p2):", p1 <= p2)
    
    
# Result
# Point p1: (1.0, 2.0, 3.0)
# Point p2: (4.0, 5.0, 6.0)
# Updated Point p1: (7.0, 8.0, 9.0)
# Length of p1: 13.92838827718412
# Distance between p1 and p2: 5.196152422706632
# Translated Point p1: (8.0, 7.0, 11.0)
# Addition: (12.0, 12.0, 17.0)
# Subtraction: (4.0, 2.0, 5.0)
# Equality Test (p1 == p3): False
# Equality Test (p1 == p2): False
# Greater Than Test (p1 > p4): True
# Greater Than Test (p2 > p1): False
# Less Than or Equal To Test (p5 <= p1): False
# Less Than or Equal To Test (p1 <= p2): False

