# Q25
# Define a class, which have a class parameter and have a same instance parameter.
# Hints: Define a instance parameter, need add it in init method
# You can init a object with construct parameter or set the value later


class Person:
    name = "Person"

    def __init__(self, name=None):
        self.name = name


Aaron = Person("Aaron")
print("%s name is %s" % (Person.name, Aaron.name))

