# if else condition in python
# a = int(input("Enter any age: "))
# print("your age is :", a)
# if(a > 18):
#     print("you can drive.")
# else:
#     print("You cannot drive.")

num = int(input("Enter the number: "))
if num < 0:
    print(num, "is negative number.")
elif num == 0:
    print("The number you enter zero.")
elif num == 7:
    print("The number is lucky seven.")
else:
    print(num, " is positive number.")
    
# nested if-else
if num < 0:
    if num == -1:
        print("your number is negative and its -1")
    else:
        print("The number is negative expect -1")