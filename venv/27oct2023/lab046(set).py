#a Set is an unordered collection of data types that is iterable,
# immutable and has no duplicate elements.
#set start with the curly paranthesis

set1={1,2,3,4,4,5,3}
print(type(set))
print(set1)
# set1[1]=12  -> this is not possible coz set is immutable

set2=set("shivam")
print(set2)


for i in set1:
    print(i)