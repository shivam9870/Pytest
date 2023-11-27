class Car:
    color=None
    model=None

    def car_name(self):
        print("Your car details is: ",self.color,self.model)

car_color=input("Enter the color of your car")
car_model=input("Enter the model of your car")

car_details_obj=Car()
car_details_obj.color=car_color
car_details_obj.model=car_model

#through the object reference we can call the function
car_details_obj.car_name()