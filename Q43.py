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
