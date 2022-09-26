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
