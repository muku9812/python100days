# Function in python
def geomatricMean(num1, num2):
    mean = (num1 * num2) / (num1 + num2)
    print("The geometric mean of given number is ", mean)


def isGreater(num1, num2):
    if num1 > num2:
        print(num1, "is greatest number.")
    elif num2 > num1:
        print(num2, "is greatest number.")
    else:
        print("Both number are equal.")


def isLess(num1, num2):
    pass


a = int(input("please enter the value of a: "))
b = int(input("please enter the value of b: "))
geomatricMean(a, b)
isGreater(a, b)

c = 9
d = 11
geomatricMean(c, d)
isGreater(b, d)

e = 8
f = 9
geomatricMean(e, f)
isGreater(e, f)
