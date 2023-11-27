#Match
#it is similiar to Switch in JAVA

num= int(input("Enter the number\t"))

match num:
    case 1:
        print("You are entered in case 1")
    case 2:
        print("You are entered in case 2")
    case _: #nothing will matching I shall run
        print("No idea")
