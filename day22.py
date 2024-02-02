# List in python

numbers = [2, 4, 6]
print(len(numbers))
print(type(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])

lists = [1, 2, 3, "Hello", 'buddy', 'pizza']
# doing this two things are same.
print(lists)  # this
print(lists[:])  # this
print(lists[1:4])
print(lists[-3])  # len(list)-3 = 5-3 = 2nd value expected result 3
print(lists[0:6:2])


# simple List comprehension
lst = [i for i in range(10)]
print(lst)

# little complex list comprehension

lsts = [i*2 for i in range(100) if i % 2 == 0]
print(lsts)