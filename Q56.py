# Q56
# Write a function to compute 5/0 and use try/except to catch the exceptions.
# Hints: Use try/except to catch exceptions.


def q56_compute():
    return 5/0


try:
    q56_compute()
except ZeroDivisionError:
    print("Dividing by zero.")
