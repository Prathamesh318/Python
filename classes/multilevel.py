# Base class
class Animal:
    def sound(self):
        return "Some generic sound"

# Intermediate class (inherits from Animal)
class Mammal(Animal):
    def feature(self):
        return "I have fur or hair"

# Derived class (inherits from Mammal)
class Dog(Mammal):
    def specific_sound(self):
        return "I bark"

# Create an object of the derived class
dog = Dog()

# Access methods from all levels
print(dog.sound())          # From Animal
print(dog.feature())        # From Mammal
print(dog.specific_sound()) # From Dog
