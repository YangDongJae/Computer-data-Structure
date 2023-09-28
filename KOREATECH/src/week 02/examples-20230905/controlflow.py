def mul_table(x, y):
    for line in range(1, y+1):
        for table in range(1, x+1):
            print (line * table, end= "\t")
        print("")

def exa01():
    name = 'Debora'
    if name == 'Debora':
        print('Hi, Debora')
    if name != 'George':
        print('You are not George')
    #
    if name == 'George':
        print('Hi, George.')
    else:
        print('You are not George')
    #
    if name == 'Debora':
        print('Hi Debora!')
    elif name == 'George':
        print('Hi George!')

    #
    if name == 'Debora':
        print('Hi Debora!')
    elif name == 'George':
        print('Hi George!')
    else:
        print('Who are you?')

    age = 15
    # this if statement:
    if age < 18:
        print('kid')
    else:
        print('adult')
    # output: kid
    # is equivalent to this ternary operator:
    print('kid' if age < 18 else 'adult')
    print('kid' if age < 13 else 'teen' if age < 18 else 'adult')
    # is equivalent to this if statement:
    if age < 18:
        if age < 13:
            print('kid')
        else:
            print('teen')
    else:
        print('adult')

def exa02():
    #Matching single values
    response_code = 201
    match response_code:
        case   200: print("OK")
        case   201: print("Created")
        case   300: print("Multiple Choices")
        case   307: print("Temporary Redirect")
        case   404: print("404 Not Found")
        case   500: print("Internal Server Error")
        case   502: print("502 Bad Gateway")
        case _: print("Invalid Case") # default case
    #Matching with the or Pattern
    response_code = 502
    match response_code:
        case 200 | 201:  print("OK")
        case 300 | 307:  print("Redirect")
        case 400 | 401:  print("Bad Request")
        case 500 | 502:  print("Internal Server Error")
        case _: print("Invalid Case") # default case
    # Matching Builtin Classes
    response_code = "300"
    match response_code:
        case    int(): print('Code is a number')
        case    str(): print('Code is a string')
        case    _: print('Code is neither a string nor a number')

    # Matching by the length of an Iterable
    today_responses = [200, 300, 404, 500]
    match today_responses:
        case[a]:    print(f"One response today: {a}")
        case[a, b]: print(f"Two responses today: {a} and {b}")
        case[a, b, *rest]: print(f"All responses: {a}, {b}, {rest}")

    # Guarding Match-Case Statements
    response_code = 300
    match response_code:
        case   int():
                    if response_code > 99 and response_code < 500:
                       print('Code is a valid number')

        case str(): print('Code is a string')
        case _: print('Code is an invalid number')

def exa03():
    for i in range(4):  # Iterating with an index:
        print(i)
    for i in range(5, -1, -1):
        print(i)
    for word in ('cool', 'powerful', 'readable'):  # iterate over values:
        print('Python is %s' % word)
    # continue the next iteration of a loop.:
    a = [1, 0, 2, 4]
    for element in a:
        if element == 0:
            continue
        print(1. / element)
    #
    for i in [1, 2, 3, 4, 5]:
        if i == 3:
            break
        else:
            print("only executed when no item is equal to 3")


    vowels = 'aeiouy'
    # Iterate over  any  sequence
    for i in 'powerful':
        if i in vowels:
            print(i)

    message = "Hello how are you?"
    message.split()  # returns a list
    for word in message.split():
        print(word)

    # Keeping track of enumeration number
    words = ('cool', 'powerful', 'readable')
    for i in range(0, len(words)):
        print((i, words[i]))
    for index, item in enumerate(words):
        print((index, item))

    # Looping over a dictionary
    d = {'a': 1, 'b': 1.2, 'c': 1j}
    for key, val in sorted(d.items()):
        print('Key: %s has value: %s' % (key, val))

    alist = [i ** 2 for i in range(6)]
    print(alist)

def exa04():
    spam = 0
    while spam < 5:
        print('Hello, world.')
        spam = spam + 1

    #break Statements
    while True:
        name = input('Please type your name: ')
        if name == 'your name':
            break

    # continue Statements
    while True:
        name = input('Who are you? ')
        if name != 'Joe':
            continue
        password = input('Password? (It is a fish.): ')
        if password == 'swordfish':
            break

    # Typical C-style while loop
    z = 1 + 1j
    while abs(z) < 100:
        z = z ** 2 + 1
    print(z)

    # break  out of  for / while loop:
    z = 1 + 1j
    while abs(z) < 100:
        if z.imag == 0:
            break
        z = z ** 2 + 1
    print(z)
