# Encapsulation -> It describes the idea of wrapping data and the methods that work aon data within one unit.

class Myclass:
    def __init__(self):
        self.public_var=10
        self._protected=12
        self.__private_var=12
        #self._demo_var=89

    def public_method(self):
        print("This is a public method.")
        print(self.public_var)


obj=Myclass()
#print(obj._demo_var)
print(obj.public_var)
print(obj._protected)

