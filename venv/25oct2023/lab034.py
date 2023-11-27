list1=[1,2,3,45,6,2,22]
list2=[1,True,"Shivam"]
list3=[24,25,26,27,22,21]

print(list2)
print(list2[1])

#changing an element

list2[1]=False
print(list2)

#appending just adding extra element
list2.append(5)
print(list2)

#extending
list2.extend([7,2])
print(list2)

#insert
list2.insert(1,'e')
print(list2)

#remove
list2.remove('e')
print(list2)

#copy
copylist=list1.copy()
print(copylist)

# list1.clear()
# print("Empty list",list1)

list1.sort()
print(list1)

#length
print(len(list1))

print(list1.count(2)) #count how many times 2 occurs in list1

print("list1:",list1)
print("list3:",list3)
list1.extend((list3))
print("merging both list:",list1)