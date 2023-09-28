## Variables
def exa01():
    # Python program to declare variables
    myNumber = 3
    print(myNumber)

    myNumber2 = 4.5
    print(myNumber2)

    myNumber = "helloworld"
    print(myNumber)

    # valid names
    numOfBoxes = 7
    _num_of_boxes = 10  # this is a different variable than numOfBoxes
    _NUM_OF_BOXES = 15  # a different variable as names are case sensitive
    ownerName = "Karthik"
    ownerName2 = "Charan"  # different, valid variable

    # invalid names
    #2ownerName = "David"  # cannot start with number.    Only letter or underscore in the beginning
    #owner - name = "Ram"  # no hypen
    #owner  name = "Krish"  # no space allowed

    # different values assigned to many variables
    length, width, depth = 5, 8, 7
    print(length)
    print(width)
    print(depth)

    # same value assigned to many variables
    length = width = depth = 5
    print(length)
    print(width)
    print(depth)


def fformat_exa01():
    name = "Nick"
    print(f"My name is {name}")

    #
    first_name = "Nick"
    last_name = "Jones"
    profession = "Software Engineer"
    platform = "Codingem.com"
    print(f"Hi! I am {first_name} {last_name}, a {profession}. I'm writing a new article on {platform}.")

    #Multi-Line Formatted
    message = (
        f"Hi! I am {first_name} {last_name}."
        f"I'm a {profession}."
        f"I'm writing a new article on{platform}."
    )
    print(message)

    data = [("x", "y", "sum"), (1, 2, 3), (3, 5, 8)]
    for x, y, sum in data:
        print(f"{x:{1}} {y:{1}} {sum:{2}}")
    #
    f_num = 12.3241233
    print(f"The number is: {f_num:.2f}")

# format specifier
def formatspecifiers_exa01():
    print("%10.3e" % (356.08977))  # 3.561e+02
    print("%10.3E" % (356.08977))  # 3.561E+02
    print("%10o" % (25))  # 31
    print("%10.3o" % (25))  # 031
    print("%10.5o" % (25))  # 00031
    print("%5x" % (47))  # 2f
    print("%5.4x" % (47))  # 002f
    print("%5.4X" % (47))  # 002F


    # print integer and float value
    print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))

    # print integer value
    print("Total students : %3d, Boys : %2d" % (240, 120))

    # print octal value
    print("%7.3o" % (25))

    # print exponential value
    print("%10.3E" % (356.08977))

### str.format ()
def strformate_exa01():
    print(print('{q} {item} cost ${price}'.format(q=6, item='bananas', price=1.74)))
    print('{}{}{}'.format('foo', 'bar', 'baz'))
    print('{}{}'.format('foo', 'bar', 'baz'))
    # print('{}{}{}{}'.format('foo','bar','baz')) # error
    print('{2}.{1}.{0}/{0}{0}.{1}{1}.{2}{2}'.format('foo', 'bar', 'baz'))
    print('{0}/{1}/{2}'.format('foo', 'bar', 'baz'))
    print('{0}/{1}/{2}'.format('foo', 'bar', 'baz'))
    print('{0}/{1}/{2}'.format('bar', 'baz', 'foo'))
    print('{x}/{y}/{z}'.format(x='foo', y='bar', z='baz'))
    print('{x}/{y}/{z}'.format(y='bar', z='baz', x='foo'))


    a, b, c = 1, 2, 3.666667

    first_name = "Nick"
    last_name = "Jones"
    profession = "Software Engineer"
    platform = "Codingem"
    print("Hi! I am {} {}, a {}. I'm writing a new article on{}.".format(
        first_name, last_name, profession, platform))



    print("\nInteger")
    format_test1 = '{}, {:d}, {:3d}, {:03d}'
    print(format_test1)
    print(format_test1.format(a,a,a,a))

    print("\nFloat")
    format_test2 = '{}, {:.0f}, {:.3f}, {:7.3f}, {:07.3f}'
    print(format_test2)
    print(format_test2.format(c,c,c,c,c))

   # order of arguments
    print("\nIn case of input order= {}, {}, {}".format(a,b,c))
    format_test2 = '{1:d}, {2:.2f}, {0:.1f}, {0:d}'
    print('\n'+format_test2+' # We have only 3 inputs!')
    print(format_test2.format(a,b,c))
    format_test3 = '{:d}, {other:.2f}, {:.1f}'
    print('\n'+format_test3)
    print(format_test3.format(a,b,other=c))
    print("Keyword must be at the end")

    print("\nHow about multi-lines? Use tripple quote mark!")
    multi_lines='''
        Hello, my name is {name}.
        I am {age:d} years old.
        My favorite food is {food}
        '''
    print(multi_lines)
    keywords={"name":"Dave", "age":25, "food":"chococake"}  # This is dictionry!
    print(keywords, type(keywords))
    print(multi_lines.format(**keywords))  # two stars: distribute items of "key:value"

    # combining positional and keyword arguments
    print('Number one portal is {0}, {1}, and {other}.'
          .format('Geeks', 'For', other='Geeks'))

    # using format() method with number
    print("Geeks :{0:2d}, Portal :{1:8.2f}".
          format(12, 00.546))

    # Changing positional argument
    print("Second argument: {1:3d}, first one: {0:7.2f}".
          format(47.42, 11))

    print("Geeks: {a:5d},  Portal: {p:8.2f}".
          format(a=453, p=59.058))

    for x in range(1, 11):
        print('{0:2d} {1:3d} {2:4d}'.format(x, x * x, x * x * x))
def input_exa01():
    num = input("Enter number :")
    print(num)
    name1 = input("Enter name : ")
    print(name1)

    value = input("Enter a string value: ")
    num = int(input("Enter an integer value: "))
    float_num = float(input("Enter an float value: "))
    complex_num = complex(input("Enter a complex number: "))
    x, y = input("Enter a two value: ").split()
    x, y, z = input("Enter a three value: ").split()
    a, b = input("Enter a two value: ").split()

def input_exa02():
    # taking two inputs at a time
    x, y = input("Enter two values: ").split()
    print("Number of boys: ", x)
    print("Number of girls: ", y)
    print()

    # taking three inputs at a time
    x, y, z = input("Enter three values: ").split()
    print("Total number of students: ", x)
    print("Number of boys is : ", y)
    print("Number of girls is : ", z)
    print()

    # taking multiple inputs at a time  and type casting using list() function
    x = list(map(int, input("Enter multiple values: ").split()))
    print("List of students: ", x)

    #Using  List  comprehension:
    # taking two input at a time
    x, y = [int(x) for x in input("Enter two values: ").split()]
    print("First Number is: ", x)
    print("Second Number is: ", y)
    print()

    # taking three input at a time
    x, y, z = [int(x) for x in input("Enter three values: ").split()]
    print("First Number is: ", x)
    print("Second Number is: ", y)
    print("Third Number is: ", z)
    print()

    # taking two inputs at a time
    x, y = [int(x) for x in input("Enter two values: ").split()]
    print("First number is {} and second number is {}".format(x, y))
    print()

    # taking multiple inputs at a time
    x = [int(x) for x in input("Enter multiple values: ").split()]
    print("Number of list is: ", x)

