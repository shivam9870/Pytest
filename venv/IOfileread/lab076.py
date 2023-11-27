# File IO in python


# if you want to write in file

# file2=open('shivam.txt','a')
# file2.write("adding this line via append method")
# file2.close()
# if you re-run this writing code then ("adding this line via append method") this line adding every time.

file = open("shivam.txt", 'r')
print(file.read())
file.close()

