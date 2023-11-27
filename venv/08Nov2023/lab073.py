# Abstraction - Hiding the details and showing the what is required

# example like -> when you drive a car ,you accelarate the pedal but
# you dont know how the accelaration and shaft and other things happens constantly
# you just push the pedal..and go wherever you want

# in hindi -> user ko sirf required chheze show kro baaki functionality nahi show krna.

# ABC -> Abstract Base Class
# Abstract base methods

# Shape -> Rectangle , Circle

from abc import ABC, abstractmethod

# abc= module
# ABC= class & abstract_methods = methods

# Animal -> sound()= dog, cat, tiger

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "bow bow"


class Cat(Animal):
    def sound(self):
        return "meow meow"


class Tiger(Animal):
    def sound(self):
        return "roar roar"


dog = Dog()
print(dog.sound())
tiger = Tiger()
print(tiger.sound())

# animal=Animal() -> we cant init the parent class

