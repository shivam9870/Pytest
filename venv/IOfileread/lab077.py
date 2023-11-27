# if there is no such file name then you can
# handle this error via the try and exception handling -> #only when reading the file
try:
    data = open('demo.txt', 'r')
    print(data.read())
    file.close()
except FileNotFoundError as e:
    print("File not found ",e)
