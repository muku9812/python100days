# tuple in python
# tuples are immutable
# simple tuple
tup = (1,)
print(type(tup), tup)

tups = (1)  # when their is only one element, if you don't give coma after that it will show element datatype, in this case it will show int
print(type(tups), tups)

tupps = (1, 2, 3, 5, 7, 'numbers', 'tuple', True, False)
# tupps[0] = 2  # tuple doesn't allow to modification of data.
print(type(tupps), tupps)
if 4 in tupps:
    print("yes their is 4 in the tuple")
else:
    print("sorry their is no any result.")


# slicing of tuple
tupps2 = tupps[4:7]
print(tupps2)