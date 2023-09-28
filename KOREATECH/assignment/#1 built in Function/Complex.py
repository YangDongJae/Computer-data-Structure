import math

class Complex:
    def __init__(self, x=0, y=0):
        self.re = x  # Real part
        self.im = y  # Imaginary part

    def __str__(self):
        if self.im >= 0:
            return f"{self.re} + {self.im}i"
        else:
            return f"{self.re} - {abs(self.im)}i"

    def __repr__(self):
        return f"Complex({self.re}, {self.im})"

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re + other.re, self.im + other.im)
        else:
            raise TypeError("Unsupported operand type for +")

    def __mul__(self, other):
        if isinstance(other, Complex):
            real = self.re * other.re - self.im * other.im
            imag = self.re * other.im + self.im * other.re
            return Complex(real, imag)
        else:
            raise TypeError("Unsupported operand type for *")

    def __abs__(self):
        return math.sqrt(self.re ** 2 + self.im ** 2)
    
    def __eq__(self, other):
        if isinstance(other, Complex):
            return self.re == other.re and self.im == other.im
        else:
            return False

    def __ne__(self, other):
        if isinstance(other, Complex):
            return not self.__eq__(other)
        else:
            return True

    def __gt__(self, other):
        if isinstance(other, Complex):
            return abs(self) > abs(other)
        else:
            raise TypeError("Unsupported operand type for >")

    def __le__(self, other):
        if isinstance(other, Complex):
            return not self.__gt__(other)
        else:
            raise TypeError("Unsupported operand type for <=")


if __name__ == "__main__":
    z1 = Complex(3, 4)  # Create a complex number 3 + 4i
    z2 = Complex(1, -2)  # Create a complex number 1 - 2i

    # Test addition
    result_add = z1 + z2
    print("Addition:", result_add)

    # Test multiplication
    result_mul = z1 * z2
    print("Multiplication:", result_mul)

    # Test absolute value
    abs_z1 = abs(z1)
    print("Absolute Value of z1:", abs_z1)

    # Test equality
    z3 = Complex(3, 4)  # Create another complex number 3 + 4i
    print("Equality Test (z1 == z3):", z1 == z3)
    print("Equality Test (z1 == z2):", z1 == z2)

    # Test inequality
    print("Inequality Test (z1 != z3):", z1 != z3)
    print("Inequality Test (z1 != z2):", z1 != z2)

    # Test greater than
    z4 = Complex(5, 1)  # Create another complex number 5 + 0i
    print("Greater Than Test (z1 > z4):", z1 > z4)
    print("Greater Than Test (z2 > z1):", z2 > z1)

    # Test less than or equal to
    z5 = Complex(1, 5)  # Create another complex number 0 + 5i
    print("Less Than or Equal To Test (z5 <= z1):", z5 <= z1)
    print("Less Than or Equal To Test (z1 <= z2):", z1 <= z2)

# Result 
# Addition: 4 + 2i
# Multiplication: 11 - 2i
# Absolute Value of z1: 5.0
# Equality Test (z1 == z3): True
# Equality Test (z1 == z2): False
# Inequality Test (z1 != z3): False
# Inequality Test (z1 != z2): True
# Greater Than Test (z1 > z4): False
# Greater Than Test (z2 > z1): False
# Less Than or Equal To Test (z5 <= z1): False
# Less Than or Equal To Test (z1 <= z2): False