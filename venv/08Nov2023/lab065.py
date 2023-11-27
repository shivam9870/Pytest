# __ =private
# _ = protected
# no underscore (default) = public

class Person:

    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def print_details(self):
        print("Your details",self.__name,self.__age)


person=Person("amit","35")
person.print_details()
