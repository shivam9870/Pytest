#Map and Filter in the list

#Map function

#traditona way to square the list

num=[1,2,3,4,5]

def triple(a):
    return a*3

sq= lambda x: x*x
#print(sq(5))
sq_list=[]
for i in num:
    sq_list.append(sq(i))
print(sq_list)

#This is a way from for loop
#using MAP FUNCTION

sq2= list(map(lambda x:x * x,num)) #map(function,list/where to apply this functionality)
#here lambda function applies to num
print(sq2)

sq3=list(map(triple,num)) #here we use the triple function
print(sq3)