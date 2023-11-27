# exception
a = 10
b = 0

# an exception is an event that occurs during the execution of a program
# that disturb the normal flow of instructions.

try:
    print(a / b)
except ZeroDivisionError as error:
    print(error)
