class Myclass:
    name=None
    def print_name(self):
        print("Your name is: "+self.name)
myname_obj=Myclass()
myname_obj.name="shivam"
print(myname_obj)
myname_obj.print_name()