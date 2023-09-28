import csv
import random



class PythonDS:
    def string_exa01(self):
        # Creating a String  with single Quotes
        String1 = 'Welcome to the Geeks World'
        print(String1)

        # Creating a String  with double Quotes
        String2 = "I'm a Geek"
        print(String2)

        # Creating a String  with triple Quotes
        String3 = '''I'm a Geek and I live in a world of "Geeks"'''
        print(String3)

        # Creating String with triple Quotes allows multiple lines
        String4 = '''Geeks
                    For
                    Life'''
        print(String4)

        # Access characters of String
        print(String1[0])
        print(String1[-1])

        # String Slicing
        print(String1[3:-2])
        print(String1[3:12])
        print(String1[::-1])

        # reverse  a  string
        gfg = "".join(reversed(String1))
        print(gfg)

        # Deleting/Updating from a String
        list1 = list(String1)
        list1[2] = 'p'
        String2 = ''.join(list1)
        print(String2)
        String3 = String1[0:2] + 'p' + String1[3:]  # Error
        print(String3)
        # Updating a String
        String1 = "Welcome to the Geek World"
        print(String1)

        # Deleting a character  of the String
        String2 = String1[0:2] + String1[3:]
        print(String2)

        # Deleting a String with the use of del
        del String1

    # Escape Sequencing in Strings
    def string_exa02(self):
        # Initial String
        String1 = '''I'm a "Geek"'''
        print(String1)

        # Escaping Single Quote
        String2 = 'I\'m a "Geek"'
        print(String2)

        # Escaping Double Quotes
        String3 = "I'm a \"Geek\""
        print(String3)

        # Printing Paths with the  use of Escape Sequences
        String4 = "C:\\Python\\Geeks\\"
        print(String4)

        # Printing Paths with the  use of Tab
        String5 = "Hi\tGeeks"
        print(String5)

        # Printing Paths with the use of New Line
        String6 = "Python\nGeeks"
        print(String6)

    # Formatting of Strings
    def string_exa03(self):
        # Default order
        String1 = "{} {} {}".format('Geeks', 'For', 'Life')
        print(String1)

        # Positional Formatting
        String1 = "{1} {0} {2}".format('Geeks', 'For', 'Life')
        print(String1)

        # Keyword Formatting
        String1 = "{l} {f} {g}".format(g='Geeks', f='For', l='Life')
        print(String1)

        # Formatting of Integers
        String1 = "{0:b}".format(16)
        print(String1)

        # Formatting of Floats
        String1 = "{0:e}".format(165.6458)
        print(String1)

        # Rounding off Integers
        String1 = "{0:.2f}".format(1 / 6)
        print(String1)

        # String alignment
        String1 = "|{:<10}|{:^10}|{:>10}|".format('Geeks', 'for', 'Geeks')
        print(String1)

        # To demonstrate aligning of spaces
        String1 = "\n{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009)
        print(String1)

    def list_exa01(self):
        # Getting values with indexes
        furniture = ['table', 'chair', 'rack', 'shelf']
        print(furniture[0])
        print(furniture[1])
        print(furniture[2])
        print(furniture[3])

        # Negative indexes
        print(furniture[-1])
        print(furniture[-3])
        print("The {} is bigger than the {}".format(furniture[-1], furniture[-3]))

        # Getting sublists with Slices
        print(furniture[0:4])
        print(furniture[0:-1])
        print(furniture[0:-2])
        print(furniture[1:3])
        print(furniture[:2])
        print(furniture[:])
        furniture2 = furniture[:]
        print(furniture2)

        # Changing values with indexes
        furniture[0] = 'desk'
        furniture[2] = furniture[1]
        furniture[-1] = 'bed'

        # The in and not in operators
        print('rack' in ['table', 'chair', 'rack', 'shelf'])
        print('bed' in ['table', 'chair', 'rack', 'shelf'])
        print('bed' not in furniture)
        print('rack' not in furniture)

        #
        table, chair, rack, shelf = furniture
        print(table, chair, rack, shelf)
        a, b, c, d = furniture
        print(a, b, c, d)
        a, b = 'table', 'chair'
        print(a, b)
        a, b = b, a
        print(a, b)

    def list_exa02(self):
        furniture = ['table', 'chair', 'rack', 'shelf']
        price = [100, 50, 80, 40]
        # Concatenation and Replication
        print([1, 2, 3] + ['A', 'B', 'C'])
        print(['X', 'Y', 'Z'] * 3)
        my_list = [1, 2, 3]
        my_list = [1, 2, 3] + ['A', 'B', 'C']
        print(my_list)

        print(len(my_list))  # Getting a list length with len()
        furniture.append('bed')  # append()
        print(furniture)
        furniture.insert(1, 'bed')  # insert()
        print(furniture)
        del furniture[2]  # del()
        print(furniture)
        furniture.remove('chair')  # remove()
        furniture.insert(0, 'chair')  # insert()
        furniture.pop()  # pop()
        furniture.insert(0, 'chair')  # insert()
        furniture.pop(0)  # pop()
        furniture.insert(0, 'chair')  # insert()

    def list_exa03(self):
        furniture = ['table', 'chair', 'rack', 'shelf']
        price = [100, 50, 80, 40]
        numbers = [2, 5, 3.14, 1, -7]
        letters = ['a', 'z', 'A', 'Z']

        # Sorting values with sort()
        numbers.sort()
        furniture.sort()
        price.sort()
        furniture.sort(reverse=True)
        print(numbers)
        print(furniture)
        print(price)
        letters.sort(key=str.lower)
        print(letters)
        print(sorted(furniture))

        # Getting the index in a loop with enumerate()
        for item in furniture:
            print(item, end=" ")
        print()
        for index, item in enumerate(furniture):
            print('index: {} - item: {}'.format(index, item))

        # Loop in Multiple Lists with zip()
        for item, amount in zip(furniture, price):
            print(f'The {item} costs ${amount}')

    def tuple_exa01(self):
        #Creating tuples
        t0=() # Empty Tuple
        t1=(1,) # Tuple  with a single value
        t2= (1, 2, 3) # Tuple containing  numeric objects
        t3=('hello', 'world') # Tuple containing string  objects
        t4=(True, [1, 2], (3, 4), 'hello') # Tuple containing  multiple objects


        print(t2)
        print(type(t4))

        # Converting     list() and tuple()
        t5 = tuple([1, 2, 3])
        print(tuple(['cat', 'dog', 5]))
        # Tuple from dictionary
        d = dict(a=1, b=2, c=3)
        t6 = tuple(d)


        letters = ('a', 'b', 'c', 'd', 'e')
        for letter in letters:
            print(letter)
        print('d' in letters)
        print(letters[0])
        print(letters[:3])
        print(letters[1:4])

        # Python tuples unpacking
        numbers = (1, 2, 3)
        (a, b, c) = numbers
        # Tuple unpacking using the asterisk
        #review
        numbers = (1, 2, 3, 4, 5)
        (one, two, *more_than_three) = numbers
        (one, *two_to_last, last) = numbers

        z_object = zip(numbers, letters)
        print(tuple(z_object))

        (S, A) = self.sum_and_avg(3, 8, 5)
        print('Sum =', S)
        print('Avg =', A)

    def sum_and_avg(self,x, y, z):
        s = x + y + z
        a = s / 3
        return (s, a)


    def dict_exa01(self):
        my_cat = {
            'size': 'fat',
            'color': 'gray',
            'disposition': 'loud'
        }
        pet = {'color': 'red', 'age': 42}
        for value in pet.values():  # values()
            print(value)
        for key in pet.keys():  # keys()
            print(key)
        for item in pet.items():  # items()
            print(item)
        for key, value in pet.items():
            print(f'Key: {key} Value: {value}')
        print(pet.get('color'))  # get()
        if 'key01' not in pet:
            pet['key01'] = 'value01'
        pet.setdefault('name', 'Tony')  # Adding items with setdefault()
        print(pet.pop('key01'))  # pop
        print(pet.popitem())  # popitem()
        del pet['age']  # del()



    def set_exa01(self):
        # Using lists in a set
        # my_set = {"A", "B", "G", ["Alpha", "Beta", "Gamma"]}
        # print(my_set)    # This will give an error

        # Using tuples in a set
        my_set = {"A", "B", "G", ("Alpha", "Beta", "Gamma")}
        print(my_set)

        # Output
        # {'G', ('Alpha', 'Beta', 'Gamma'), 'A', 'B'}
        # it can be in different order when you print it, because sets are unordered.

        # creating an empty set
        empty_set = set()
        print(type(empty_set))

        s = {1, 2, 3}
        s = set([1, 2, 3])
        print(type(s))
        s = {}  # this will create a dictionary instead of a set
        print(type(s))
        s = {1, 2, 3, 2, 3, 4}
        print(s)

        # Access to Set Element(s)
        movie = {12, "Angry", "Man"}
        for i in movie:
            print(i, end=" ")

        if 10 in movie:
            print("There is only 10 Angry Man")
        else:
            print("It should be 12 man, count it right :)")

    def set_exa02(self):
        s = {1, 2, 3}

        # set add() and update()
        s.add(14)
        print(s)
        s.update([2, 3, 4, 5, 6])
        print(s)

        # set remove() and discard()
        s.remove(3)
        s.discard(3)
        print(s)

        # set union(), intersection(), difference(),  symetric_difference()
        s1 = {1, 2, 3}
        s2 = {3, 4, 5}
        s3 = s1.union(s2)  # or 's1 | s2'
        print(s3)

        s4 = s1.intersection(s2, s3)  # or 's1 & s2 & s3'
        print(s4)
        s5 = s1.difference(s2)  # or 's1 - s2'
        print(s5)

    def vowel_count(self,str):
        count = 0 # Initializing count variable to 0
        vowel = set("aeiouAEIOU") # Creating a set of vowels
        for alphabet in str: # Loop to traverse the alphabet in the given string
            if alphabet in vowel: # If alphabet is present in set vowel
                count = count + 1
        print("No. of vowels :  {} ".format(count))

class files:
    def rfiles_exa01(self,fname):
        with open(fname, 'r') as f:
            print("File name: ", f.name)
            print("File state: ", f.closed)
            print("Opening mode: ", f.mode)
            data = f.read()
            print(data)

    def rfiles_exa02(self,fname):
        with open(fname, 'r') as f:
            print("File name: ", f.name)
            print("File state: ", f.closed)
            print("Opening mode: ", f.mode)
            line = f.readline()
            print(line)
            count = 0

            while True:
                count += 1
                if not line:
                    break
                print("Line{}: {}".format(count, line.strip()))
                line = f.readline()

    def rfiles_exa03(self,fname):
        with open(fname, 'r') as f:
            print("File name: ", f.name)
            print("File state: ", f.closed)
            print("Opening mode: ", f.mode)
            lines = f.readlines()
            count = 0
            for line in lines:
                count += 1
                print("Line{}: {}".format(count, line.strip()))

    def rfiles_exa04(self,fname):
        with open(fname, 'r') as f:
            number_of_lines = 0
            number_of_words = 0
            number_of_chars = 0

            for line in f:
                number_of_lines += 1
                word_list = line.split()
                number_of_words += len(word_list)
                number_of_chars += sum(len(x) for x in word_list)

            print("Lines = {}, Words = {}, Char = {}".format(number_of_lines, number_of_words, number_of_chars))

    #review
    def rfiles_exa05(self,fname):
        with open(fname, 'r') as f:
            text = f.read();
            word_counts = {}
            letter_counts = {}
            # count occurrences of each unique word
            for word in text.split():
                word_counts[word] = word_counts.get(word, 0) + 1
            for letter in text:
                letter_counts[letter] = letter_counts.get(letter, 0) + 1

            print('Frequency of each word')
            for word, count in sorted(word_counts.items()):
                print(word, " = ", count)

            print('\nNumber of unique words:', len(word_counts))
            for letter, count in sorted(letter_counts.items()):
                print(letter, " = ", count)

    def wtxt_exa01(self):
        # using
        lines = ['Readme', 'How to write text files in Python', 'Methods are explained']
        with open('.\data\sample01.txt', 'w') as f:
            for line in lines:
                f.write(line)
                f.write('\n')
        lines2 = ['Readme2', 'How to write text files in Python 2']
        more_lines = ['', 'Append text files', 'The End']
        with open('.\data\sample01.txt', 'a') as f:
            f.write('\n'.join(lines2))
            f.write('\n'.join(more_lines))

    def rcsv_exa01(self):
        with open('.\data\exams.csv', 'r', encoding='utf-8') as csvf:
            data = csv.reader(csvf, delimiter=',')
            for r in data:
                print('{},{},{},{},{},{},{},{}'.format(r[0], r[1], r[2], r[3], r[4], r[5], r[6], r[7]))

    def wcsv_exa01(self):
        with open('.\data\sample01.csv', 'w', newline='', encoding='utf-8') as f:
            data = csv.writer(f)
            for i in range(50):
                data.writerow([i, i * 2, i * 3, i * 4, i * 5])

    def wcsv_exa02(self):
        with open('.\data\sample02.csv', mode='w') as csv_file:
            fieldnames = ['emp_name', 'dept', 'birth_month']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow({'emp_name': 'John Smith', 'dept': 'Accounting', 'birth_month': 'November'})
            writer.writerow({'emp_name': 'Erica Meyers', 'dept': 'IT', 'birth_month': 'March'})