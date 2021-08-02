class Person:
    def __init__(self, name, age, nationarity):
        self.name = name
        self.age = age
        self.nationarity = nationarity

tom = Person("eric", 72, "England")
print(tom.age)