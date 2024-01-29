x = int(input("Enter the value of X :"))
match x:
    case 0:
        print("you enter 0")
    case 1:
        print("you enter 1")
    case _:
        print(x, "is the number you entered.")
    