#Palindrome program
#which means eg.
# MADAM= reverse -> MADAM = this is a palindrome
#naman , malayalam,121 etc these are the palindrome examples.

#now we have reverse the string and match with given user string

#METHOD 1 [Traditional method]:

def reverse_string(inp):
    rev_str=""
    for c in inp:
        rev_str=c+rev_str
    return rev_str

original_string="madam"
revstr = reverse_string(original_string)
print(revstr)

if original_string==revstr:
    print("This is palindrome")
else:
    print("This is not a palindrome")

