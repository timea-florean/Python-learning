class Dog:
    #class attribute 
    species="Canis familiaris"

    #initializer / instance attributes
    def __init__(self,name, age):
        self.name=name
        self.age=age
    #instance method
    def description(self):
        return f"{self.name} is {self.age} years old"
    #another instance method
    def speak(self, sound):
        return f"{self.name} says {sound}"
#creating an object (an instance of the Dog class)
my_dog=Dog("Buddy", 4)

#Accessing the object's attributes
print(f"My dog {my_dog.name} is {my_dog.age} years old and belongs to the species {my_dog.species}.")

print(my_dog.description())
print(my_dog.speak("Woof"))