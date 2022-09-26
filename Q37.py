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
