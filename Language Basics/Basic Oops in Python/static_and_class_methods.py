class Person(object):
    population = 50

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population

    @staticmethod
    def getAge(self):
        return self.age

person1 = Person("Ashok", 20)
print(person1.getAge())
print(Person.getPopulation())