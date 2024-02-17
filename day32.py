# set method in python

a = {1, 3, 5, 7, 9, 2, 8}
b = {2, 4, 6, 8, 10}
print(a.union(b))
print(a.intersection(b))

# symmetric difference gives the value by ignoring the common
print(a.symmetric_difference(b))


# difference gives the result of a - b
print(a.difference(b))

a.update(b)   # this will update the value of a
print(a)