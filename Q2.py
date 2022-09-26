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