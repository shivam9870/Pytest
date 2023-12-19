# here we open the 'text.txt' file

with open("cricket.txt", 'r') as File:
    data = File.read()
    print(data)
