list1=[12,15,12,13,1,51,15,13]
print(list1)

#print unique items
set1=set(list1)
print(set1)

set1={1,2,3,4}
set2={5,6,7,8}
myset=set1.union(set2)
print("union:->",myset)

num1={1,2,3,4,5}
num2={4,5,6,7,8}
num3={2,3,4}
mynum=num1.intersection(num2)
print("intersection:->",mynum)
mydiff=num1.difference(num2)
print("difference:->",mydiff)
mysub=num3.issubset(num1) #checking the num3 is the subset in num1
print("subset:->",mysub)

