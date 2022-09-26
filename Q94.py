# Q94
# With a given list [12,24,35,24,88,120,155,88,120,155], write a program to print this list after
# removing all duplicate values with original order reserved.
# Hints: Use set() to store a number of values without duplicate.

q94_list = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]
q94_mod = sorted(set(q94_list), key=q94_list.index)
print(f'Unique List: {q94_mod}')
