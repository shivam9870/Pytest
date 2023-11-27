words=["starfruit","apple","strawberry","nuts","starch","lemon"]
min_len=6

def check_len(w):
    return len(w) > min_len

# print(check_len(words[1]))

op=list(filter(check_len,words))
print(op)