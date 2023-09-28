def exa01():
    x = 3  # a whole number
    f = 3.1415926  # a floating point number
    name = "Python"  # a string
    print(x)
    print(f)
    print(name)
    combination = name + " " + name
    print(combination)
    sum = f + f
    print(sum)

def intType():
    print("\n1. Integer and float numbers\n")
    a=17
    b=7
    print("a = {}:\t type = {}".format(a,type(a)))
    print("b = {}:\t type = {} \n".format(b,type(b)))
    print("c = a+b")
    c=a+b
    print("c = {}:\t type = {} \n".format(c,type(c)))
    print("c = a/b")
    c=a/b
    print("c = {}:\t type = {}  # Basically 8-Byte (64bit) \n".format(c,type(c)))

    print("Cf. floor divider, //")
    print("d = a//b; d2= float(a)//b \n")
    d=a//b; d2= float(a)//b
    print("d = {}:\ttype = {}".format(d,type(d)))
    print("d2 = {}:\ttype = {} \n".format(d2,type(d2)))

    print("Ref. Arithmetic Operators: +, -, *, /, %, **, // ")

### String
def stringType():
    print("\n2. String examples\n")
    print("str1, str2= 'abc1#', \"abc!2\"")
    str1,str2= 'abc1#', "abc!2"
    print(str1,str2,"\n")
    print("d = str(c)  # Change type from float to string; c.f., int(), float()")
    c=100
    d=str(c)
    print("d = {}:\ttype = {}\n".format(d,type(d)))
    print("len(d), d[0:4], d[-3:]  # Python index starts at 0; start to end(not including)")
    print("{}, {}, {}\n".format(len(d),d[0:4],d[-3:]))
    print("c+c vs. d+d[:5] vs. d*2")
    print("{} vs. {} vs. {}\n".format(c+c,d+d[:5],d*2))
    print("len(d*3)")
    print(len(d*3))

### Printing unicode
def ucType():
    print("\n3. Unicode example\n")
    print("El Ni\u00F1o and La Ni\u00F1a \n")
    print("Delta: {}, epsilon: {}, degree: {} \n".format('\u0394','\u03B5','\u00B0'))
    print("Subscript: x{}, x{}, x{} \n".format('\u2081','\u2082','\u2090'))
    print("Superscript: x{}, x{}, x{} \n".format('\u00B9','\u00B2','\u1D43'))

 ### Boolean
def booleanType():
    print("\n4. Boolean type\n")
    print("boo1, boo2 = True, False")
    boo1, boo2 = True, False
    print("boo1 = {}:\ttype = {} \n".format(boo1,type(boo1)))
    print("Value of {} and {}:".format(boo1,boo2))
    print(int(boo1),int(boo2),'\n')
    print("{}+{} = {}".format(boo1,boo2,boo1+boo2))
    print("{}+{} = {}".format(boo1,boo1,boo1+boo1))
    print("{}-{} = {} \n".format(boo2,boo2,boo2-boo2))
    print("{} 'and' {} = {}".format(boo1,boo2,boo1 and boo2))
    print("{} 'or' {} = {}".format(boo1,boo2,boo1 or boo2))
    print("'not' {} = {} \n".format(boo1, not boo1))

    print("bool(-1) = {}, bool(0) = {}, bool(1) = {}, bool(2) = {}".format(bool(-1),bool(0),bool(1),bool(2)))
    print("bool(-0.1) = {}, bool(0.) = {}, bool(0.1) = {}".format(bool(-0.1),bool(0.),bool(0.1)))
    print("---> Value zero(0) is False, and all others are True \n")

    print("""a = 2
    a = bool(a)
    a = int(a)
    print(a)""")
    a = 2; a = bool(a); a = int(a); print(a)
