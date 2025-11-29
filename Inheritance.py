#Base class
class Animal:
    def __init__(self, name):
        self.name=name
    def speak(self):
        raise NotImplementedError("Subclasses must implement this method")
#derived class
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow"
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof"
#using polymorphism
pet=Cat("Whiskers")
print(pet.speak())

pet=Dog("Buddy")
print(pet.speak())