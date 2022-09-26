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