# recursion function

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


number = int(input("Enter any number to find factorial: "))
num = factorial(number)
print(f"The factorial of {number} is", num)


#  fibbonanci series

def fibo(n):
    num1 = 0
    num2 = 1
    count = 0
    if n <= 0:
        print("please enter positive or number greater than 0.")
    elif n == 1:
        print(num1)
    else:
        print("The Fibonacci sequence: ")
        while count < n:
            print(num1)
            num3 = num1 + num2
            num1 = num2
            num2 = num3
            count += 1


number = int(input("Enter number the number of term for fibonacci: "))
fibo(number)



