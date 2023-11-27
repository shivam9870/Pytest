class Myhome:

    def __init__(self):
        self.__private_toilet = "Private toilet allowed only Shivam"
        self.__protected_toilet = "Protected toilet allowed only known"
        self.public_toilet = "Public toilet anyone can access."

    def __private_method(self):
        return "This is a private method"


obj = Myhome()
# print(obj.__private_method)
# print(obj.__protected_toilet)
# print(obj.__public_toilet)
allowed = obj.public_toilet
print(allowed)
