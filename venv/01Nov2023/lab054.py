numlist=[1,25,-12,55,23,-89,45]

#print the num greater then 10

def num_greater10(num):
    return num>10

op=list(filter(num_greater10,numlist))
print(op)