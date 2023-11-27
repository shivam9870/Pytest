#Inheritance
#Grandfather-> Father -> Child

class Animals:

    def  speak(self):
        print("Animal can speak")
        pass

class Dog(Animals):
    def speak(self):
        print("barking ")

dog=Dog()
dog.speak()