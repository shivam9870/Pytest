#Identity Operators
#is- return TRUE if both variables are the same object
#is- not Returns true if both variables are not the same object
x=[1,2,3]
y=[1,2,3]
print(x is y) #False

a=10
b=10
print(a is b) #True

print("just see the id below :")
print("the id of x",id(x))
print("the id of y",id(y))
print("the id of a",id(a))
print("the id of b",id(b))
print("The ids of a & b are same.")