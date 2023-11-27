# Overriding - Same name in parent and child
# child always override the parent class
# SUPER = call my parent class

class Animal():

    def sound(self):
        print("animal sound")


class Dog(Animal):

    def sound(self):
        super().sound()  # super used when call to parent class ".sound()" use for function
        print("dog sound")


# animal=Animal()
# animal.sound()

dog = Dog()
dog.sound()

# same functions "sound" but when create the object of particular class then corresponding class function is callable
