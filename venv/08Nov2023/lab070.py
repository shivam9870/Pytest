#Polymorphism
# Object -> behave differently on the situation
# Person - Ram and Shyam = talk()
# but Ram can talk in hindi & Shyam can talk in english

class shape():
    def area(self):
        print("area of shape")

class Rectangle(shape):

    def __init__(self,length, width):
        self.lenght= length
        self.width= width

    def area(self):
        return self.lenght * self.width

class Circle(shape):

    def __init__(self, raduis):
        self.raduis= raduis

    def area(self):
        return self.raduis * self.raduis * 3.14

shape1=Rectangle(3,4)
print(shape1.area())
shape2= Circle(10)
print(shape2.area())