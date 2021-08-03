class Person:
    def __init__(self, name, age, nationarity):
        self.name = name
        self.age = age
        self.nationarity = nationarity

    def say_hello(self, name):
        print("Mr.{0}.Hello World by class. I am {1}".format(name, self.name))

eric = Person("eric", 72, "England")
bob = Person("bob", 59, "cuba")
print(eric.age)
print(bob.nationarity)

eric.say_hello("mari")
bob.say_hello("mari")