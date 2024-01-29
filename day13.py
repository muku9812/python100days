# Strings are immutable
a = "yash.... Yash....."
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("."))
print(a.replace("Yash", "Mukesh"))
print(a.split(" "))
heading = "hello Welcome Back !!!"
print(heading.capitalize())
print(len(heading))
print(len(heading.center(50)))
print(a.count("yash"))

str1="Welcome to my class !!"
print(str1.endswith("!!"))
print(str1.endswith("to", 10, 20))

str2 = "He is a good and best man."
print(str2.find("a"))
#if not found it will return -1
print(str2.find('iss'))
# index method return error if the searching string is not found
# print(str2.index('iss'))

str3 = "Welcome back guys"
# check wheather all the string is number or not
print(str3.isalnum())
str3="welcome to the python world number 1"
print(str3.isalpha())

# check whether all the character is lower or not
print(str3.islower())

# istitle return true if staring character of each word is capital
str4 = "Bird Is Flying"
print(str4.istitle())

# startswith check whether the sentences with the given word or not
str5 = "python is a best language"
print(str5.startswith("python"))

# swapcase change lower case into upper and upper into lower
str6 = "Hello programmer, I am learning python"
print(str6.swapcase())

# title change all the starting character of word into capital
str7 = "Hi i am yash and today i am learning python with codewithHarry"
print(str7.title())

