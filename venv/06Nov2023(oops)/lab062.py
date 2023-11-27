class Car:
    def __init__(self,make,model):
        self.make=make #attributes-> make and model
        self.model=model
        #print("I will be called first")

    def start_engine(self):
        print("engine starting of",self.make, self.model)

car1=Car("Toyota","Fortuner")
car2=Car("Tata","Nexon")

car1.start_engine()
car2.start_engine()