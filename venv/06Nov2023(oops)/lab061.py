class Car:
    def __init__(self):
        print("I will be called first")

    def start_engine(self):
        print("engine start")


car1 = Car()
car2 = Car()

print(id(car1))
print(id(car2))
