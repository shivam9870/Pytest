# method OVERLOADING= same name of functions with the different parameters
# Python does not support method overloading in the traditional sense.

class MathUtil():

    def add(self,a,b):
        return a+b

    def add(self,a,b,c):
        return a+b+c

op=MathUtil()
output= op.add(1,2,3)
opt1=op.add(4,5)
print(output)
print(opt1)
# Python does not support method overloading in the traditional sense.
