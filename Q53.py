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

