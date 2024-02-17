# Dictionary in python

dict = {
    "name": "Mukesh",
    "SurName": "Mandal",
    "place": "Nepal",
    "age": 24
}
roll = {
    1: "Aman",
    2: "Anish",
    3: "Bhuwan",
    4: "Chandan",
    5: "Darshan",
    6: "Elish",
    7: "Ganesh"
}
print(f"Hello, I am {dict['name']} {dict['SurName']}. I am from {dict['place']} and I am {dict['age']} years old.", )

num = int(input("Please enter roll number of the student to find name: "))
# print(f"Roll number {num} is of {roll[num]}")  # first ways of accessing the value of dictionary, if key not found it will throw error
print(f"Roll number {num} is of {roll.get(num)}")  # Second and best way to accessing the value of dictionary, if data not found this will return none


# Accessing everything from dictionary
print(dict.keys())  # we can access all key of the list.
print(dict.values()) # we can access all the values of the list.
for key in dict.keys():  # we can access all the values of the dictionary
    print(dict[key])

# next method

for key, value in dict.items():
    print(f"The value in {key} is {value}")