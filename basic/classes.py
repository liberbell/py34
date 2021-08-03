class Person:
    def __init__(self, name, age, nationarity):
        self.name = name
        self.age = age
        self.nationarity = nationarity

    def say_hello(self):
        print("Hello World by class. I am {0}".format(self.name))

eric = Person("eric", 72, "England")
bob = Person("bob", 59, "cuba")
print(eric.age)
print(bob.nationarity)

eric.say_hello()