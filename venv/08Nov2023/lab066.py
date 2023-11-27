# __ =private
# _ = protected
# no underscore (default) = public

class Person:

    #1
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    #3
    def get_name(self):
        return self.__name

    #4
    def set_name(self,name):
        #6
        if name == "john":
            print("dont set the name")
        else:
            self.__name=name

    #2
    def print_details(self):
        print("Your details",self.__name,self.__age)


person=Person("amit","35")
person.print_details()

#i want to change the value of private
# how to change it Get and Set?
# Fetch - Get
#Set the value via here -> Constructor

#5
person.set_name("shivam")
person.set_name("john")
name=person.get_name()
print(name)
person.print_details()

