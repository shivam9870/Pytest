# here we open the 'text.txt' file

with open("text.txt", 'r') as File:
    data = File.read()
    print(data)
