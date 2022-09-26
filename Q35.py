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

