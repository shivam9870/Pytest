class Car:
    name=None
    color=None
    engine=None

    def start_engine(self):
        print("starting the engine"+self.name)

    def car_break(self):
        print("breaking"+self.name)

    def car_music(self):
        print("Music listening")

tesla_obj_ref=Car()
tesla_obj_ref.name="Tesla"
tesla_obj_ref.color="Black"
tesla_obj_ref.engine="Electric"

lambo_obj=Car()
lambo_obj.name="Lambo"
lambo_obj.color="Voilet"
lambo_obj.engine="Diesal"

print(tesla_obj_ref)
print(lambo_obj)
tesla_obj_ref.start_engine()
lambo_obj.start_engine()
tesla_obj_ref.car_break()
lambo_obj.car_break()