# doc String
def square(n):
    '''this program take n as a input and give n as a output''' # doc string always written just below tha function name or just above the function body.
    sqr = n * n;
    print(sqr)
    print(square.__doc__)


square(10)