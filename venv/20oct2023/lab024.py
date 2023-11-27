#Factorial Program
# if n=3 then factorial like this:
#3!= 3*2*1= 6

#loop

num=int(input("Enter the number"))
if num <0:
    print("Factorial is not possible for 0 and -ve")
else:
    fact=1
    for i in range(1,num+1):
        fact=fact*i
print("Factorial is -> ",fact)