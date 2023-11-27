#Class and Object in Python.

#Person
# Attributes -> name, age, gender , height
# Methods Can do -> eat(), run(), think(), dance(), sleep(),fight(), etc

#---Objects--
#Amit
#Durga
# Santosh

class Person:
    name=None # Attributes
    age=None
    height=None
    gender=None

    # Methods
    def run(self):
        print("Run"+self.name)

    def sleep(self):
        print("sleep")

    def eat(self):
        return "I am eating"

amit_obj=Person()
amit_obj.name="Amit"
amit_obj.age="25"
amit_obj.gender="male"
amit_obj.height="5.5"
# print(amit_obj)
amit_obj.run()

durga_obj=Person()
durga_obj.name="Durga"
durga_obj.age="24"
durga_obj.gender="female"
durga_obj.sleep()
durga_obj.run()
# print(durga_obj)