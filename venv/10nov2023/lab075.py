#
a= int(input("enter the a num"))
b= int(input("enter the b num"))

try:
    c=a/b
    print(c)
except ZeroDivisionError as error:
    print(error)


