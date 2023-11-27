#sum of digit

num=int(input("Enter the number\t"))
sum=0

while num!=0:
    digit=num%10
    sum=sum+digit
    num //=10

print(sum)