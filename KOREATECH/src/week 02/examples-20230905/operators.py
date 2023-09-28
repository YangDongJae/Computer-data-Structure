# Examples of Arithmetic Operator
def exa01():
    a = 9
    b = 4
    add = a + b # Addition of numbers
    sub = a - b # Subtraction of numbers
    mul = a * b # Multiplication of numbers
    div1 = a / b # Division(float) of numbers
    div2 = a // b # Division(floor) of number
    mod = a % b # Modulo of both number
    # print results
    print(add)
    print(sub)
    print(mul)
    print(div1)
    print(div2)
    print(mod)

# Examples of Relational Operators
def exa02():
    a = 13
    b = 33
    print(a > b)  # a > b is False
    print(a < b) # a < b is True
    print(a == b) # a == b is False
    print(a != b) # a != b is True
    print(a >= b) # a >= b is False
    print(a <= b) # a <= b is True

# Examples of Logical Operator
def exa03():
    a = True
    b = False
    print(a and b) # Print a and b is False
    print(a or b) # Print a or b is True
    print(not a) # Print not a is False

# Examples of Bitwise operators
def exa04():
    a = 10
    b = 4
    print(a & b) # Print bitwise AND operation
    print(a | b) # Print bitwise OR operation
    print(~a) # Print bitwise NOT operation
    print(a ^ b) # print bitwise XOR operation
    print(a >> 2) # print bitwise right shift operation
    print(a << 2) # print bitwise left shift operation

    # Examples of Identity and  Membership operator
def exa05():
    a1 = 'Mahmood'
    b1 = 'MAhmood'

    # Identity operator
    print(a1 is not b1)
    print(a1 is b1)

    # Membership operator
    print("G" in a1)
    print("N" not in b1)