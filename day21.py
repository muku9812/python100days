# function arguments
def average(a=10, b=20):
    avg = (a + b) / 2
    print("average of", a, "and", b, "is", avg)


average(1, 2)

# tuppol function


def averages(*arguments):
    print(type(arguments))
    sum = 0
    for i in arguments:
        sum = sum + i
    average = sum/len(arguments)
    print("Average is", average)


averages(10, 12, 22, 9)
averages(10, 12, 9)


def names(**name):
    print(name["fname"], name["Mname"], name["lname"])


names(fname="Mukesh", Mname="Kumar", lname="Mandal")

# function to return
def addition(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    return sum

sum = addition(10, 5, 8)
print("Sum of numbers", sum)