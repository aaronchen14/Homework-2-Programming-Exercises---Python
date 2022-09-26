# Q1
# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
# between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.
# Hints: Consider use range(#begin, #end) method
q1_range = range(2000, 3200)
q1_answer = []
for x in q1_range:
    if x % 7 == 0 and x % 5 != 0:
        q1_answer.append(x)

print(str(q1_answer), sep=', ')

# Q2
# Question: Write a program which can compute the factorial of a given numbers.
# The results should be printed in a comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8
# Then, the output should be: 40320
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.


def factorial(x):
    if x == 0:
        return 1
    else:
        return x * factorial(x - 1)


q2_input = int(input("Enter number to compute factorial: "))
print(factorial(q2_input))

# Q3
# With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that
# is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program: 8 Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# Consider use dict()

q3_input = int(input("Give max number for dictionary: "))
q3_dict = {}
for x in range(1, q3_input + 1):
    q3_dict[x] = x*x

print(q3_dict)

# Q4
# Write a program which accepts a sequence of comma-separated numbers from console and generate a list
# and a tuple which contains every number. Suppose the following input is supplied to the program:
# 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# tuple() method can convert list to tuple

q4_input = input("Give sequence: ")
q4_list = q4_input.split(',')
q4_tuple = tuple(q4_list)
print(f'List: {q4_list}')
print(f'Tuples: {q4_tuple}')

# Q5
# Define a class which has at least two methods: getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.
# Hints: Use init method to construct some parameters


class Q5Class(object):
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Give me a string to capitalize: ")

    def printString(self):
        print(self.s.upper())


q5_test = Q5Class()
q5_test.getString()
q5_test.printString()

# Q6
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H: C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example: Let us assume the following comma separated input sequence is given to the program:
# 100,150,180 The output of the program should be: 18,22,24
# Hints: If the output received is in decimal form, it should be rounded off to its nearest value
# (for example, if the output received is 26.0, it should be printed as 26)
# In case of input data being supplied to the question, it should be assumed to be a console input.

import math

C = 50
H = 30
D = input("Enter comma separated input: ")
D = D.split(',')
q6_output = []
for x in D:
    q6_output.append(str(round(math.sqrt((2 * C * int(x)) / H))))

print(', '.join(q6_output))

# Q7
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in
# the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,.., Y-1.
# Example: Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console
# input in a comma-separated form.

q7_input = input('Give 2 digits in a comma-separated form: ')
q7_dim = q7_input.split(',')
row_num = int(q7_dim[0])
col_num = int(q7_dim[1])

q7_mat = [[0 for col in range(col_num)] for row in range(row_num)]

for row in range(row_num):
    for col in range(col_num):
        q7_mat[row][col] = row * col

print(f'Q7 Matrix: {q7_mat}')

# Q8
# Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated
# sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program: without,hello,bag,world
# Then, the output should be: bag,hello,without,world
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

q8_input = input('Input in a comma-separated sequence: ')
words = q8_input.split(',')
words.sort()
print(', '.join(words))

# Q9
# Write a program that accepts sequence of lines as input and prints the lines after making all characters in the
# sentence capitalized. Suppose the following input is supplied to the program:
# Hello world Practice makes perfect
# Then, the output should be: HELLO WORLD PRACTICE MAKES PERFECT
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

q9_words = []
while True:
    q9_input = input()
    if q9_input:
        q9_words.append(q9_input.upper())
    else:
        break;

print(' '.join(q9_words))

# Q10
# Write a program that accepts a sequence of whitespace separated words as input and prints
# the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world
# Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
# We use set container to remove duplicated data automatically and then use sorted() to sort the data.

q10_input = input('Give me words separated by space: ')
q10_words = q10_input.split(' ')
q10_sort = sorted(list(set(q10_words)))
print(" ".join(q10_sort))

# Q25
# Define a class, which have a class parameter and have a same instance parameter.
# Hints: Define a instance parameter, need add it in init method
# You can init a object with construct parameter or set the value later


class Person:
    name = "Person"

    def __init__(self, name=None):
        self.name = name


Aaron = Person("Aaron")
print("%s name is %s" % (Person.name, Aaron.name))

# Q35
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the values only.
# Hints: Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


def q35_func(i):
    q35_output = {}
    for x in i:
        q35_output[x] = x**2
    for y in q35_output.values():
        print(y)
    return q35_output


q35_list = list(range(1, 20 + 1))
q35_dict = q35_func(q35_list)
# print(q36_dict)

# Q36
# Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included)
# and the values are square of keys. The function should just print the keys only.
# Hints: Use dict[key]=value pattern to put entry into a dictionary.
# Use ** operator to get power of a number.
# Use range() for loops.
# Use keys() to iterate keys in the dictionary. Also we can use item() to get key/value pairs.


def q36_func(i):
    q36_output = {}
    for x in i:
        q36_output[x] = x**2
    for y in q36_output.keys():
        print(y)
    return q36_output


q36_list = list(range(1, 20 + 1))
q36_dict = q36_func(q36_list)
# print(q36_dict)

# Q37
# Define a function which can generate and print a list where the values are square of numbers
# between 1 and 20 (both included).
# Hints: Use ** operator to get power of a number.
# Use range() for loops.
# Use list.append() to add values into a list.


def q37_func(i):
    q37_return = []
    for x in i:
        q37_return.append(x**2)

    return q37_return


q37_list = list(range(1, 20 + 1))
q37_output = q37_func(q37_list)
print(q37_output)

# Q43
# Write a program to generate and print another tuple whose values are even
# numbers in the given tuple (1,2,3,4,5,6,7,8,9,10).
# Hints: Use "for" to iterate the tuple Use tuple() to generate a tuple from a list.

q43_ituple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
q43_list = []
for x in q43_ituple:
    if x % 2 == 0:
        q43_list.append(x)

q43_ftuple = tuple(q43_list)
print(f'Final tuple: {q43_ftuple}')

# Q51
# Define a class named American and its subclass NewYorker.
# Hints: Use class Subclass(ParentClass) to define a subclass.


class American(object):
    pass


class NewYorker(American):
    pass


# Q53
# Define a class named Rectangle which can be constructed by a length and width.
# The Rectangle class has a method which can compute the area.
# Hints: Use def methodName(self) to define a method.


class Rectangle(object):
    def __init__(self, x, y):
        self.length = x
        self.width = y

    def area(self):
        return self.length * self.width


test_rect = Rectangle(3, 3)
print(test_rect.area())


# Q54
# Define a class named Shape and its subclass Square. The Square class has an init function which takes a length as
# argument. Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.
# Hints: To override a method in super class, we can define a method with the same name in the super class.


class Shape(object):
    def __init__(self):
        pass

    def area(self):
        return 0


class Square(Shape):
    def __init__(self, x):
        Shape.__init__(self)
        self.length = x

    def area(self):
        return self.length * self.length


test_s = Square(3)
print(test_s.area())

# Q56
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Hints: Use try/except to catch exceptions.


def q56_compute():
    return 5/0


try:
    q56_compute()
except ZeroDivisionError:
    print("Dividing by zero.")

# Q94
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after
# removing all duplicate values with original order reserved.
# Hints: Use set() to store a number of values without duplicate.

q94_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
q94_mod = sorted(set(q94_list), key=q94_list.index)
print(f'Unique List: {q94_mod}')
