#palindrome normal code

user_input=input("Enter the name\n")

rev_str=user_input[::-1]
print(rev_str)

if user_input==rev_str:
    print("palindrome")
else:
    print("this is't palindrome")