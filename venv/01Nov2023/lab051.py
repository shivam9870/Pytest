numers=[1,2,3,4,5,6,7,13]

even_num=filter(lambda x:x%2==0,numers)
print(list(even_num))

#odd
odd_num=filter(lambda x:x%2!=0,numers)
print(list(odd_num))

