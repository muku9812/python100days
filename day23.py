# list methods in python

list = [10, 9, 12, 24, 9, 11, 7, 18, 9]
list.append(21)  # append method add the element in the list
# print(list)
# list.reverse() # It will reverse the list
# print("Reverse", list)
# list.sort()  # sort method sort the element of the list in ascending order
# print(list)
# list.sort(reverse=True)  # this will sort the data of list in descending order
# print(list)

# print(list.index(10))  # index method will find the element is in which index

print(list.count(9))  # count method counts the given element number count in the list
print("Original list", list)
list1 = list.copy()
list1[0] = 0
list1.insert(2, 12)  # insert method help to insert data in the given index. for example on index 2 we insert 12
print("Copy list", list1)



alphabet = ["e", "c", "g", "f", "a", "b"]
vowel = ["a", "e", "i", "o", "u"]
alphabet.append("d")
alphabet.sort()
alphabet.extend(vowel)
print(alphabet)
