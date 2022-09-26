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
