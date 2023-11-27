#homework
# 1.Write a Python program to find the largest number in a list.
#
# 2.Write a Python program to find the smallest number in a list.
#
# 3.Write a Python program to sum all numbers in a list.
#
# 4.Write a Python program to multiply all numbers in a list.
#
# 5.Write a Python program to count the number of strings in a list
# where the string length is 2 or more and the first and last character are the same.

#1=
list=[2,45,62,85,45,15]
print("The largest number in the list :",max(list))

#2=
print("The smallest number in the list :",min(list))

#3=
print("The sum of numbers in the list :",sum(list))

#4=
list2=[2,4,2,2]
import numpy
result=numpy.prod(list2)
print("The multipication numbers in the list :",result)

#5=
list3=["shivam"]
print(len(list3))