class Person:
    name="Ashok"
    designation="Full Stack Developer"

    def info(self):
        
        print(f"{self.name} is a {self.designation} in our company.")

a = Person()
print(a.name)
a.info()

a.name="Aman"
a.designation="Web Developer"
a.info()

class Animal:

    def __init__(self,food,name):
        print("This is an animal.")
        self.f=food
        self.n=name

    def info(self):
        print(f"The diet of {self.n} is {self.f}.")

Zebra=Animal("grass","Zebra")
Lion=Animal("meat","Lion")
Lion.info()