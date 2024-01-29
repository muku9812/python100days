# loops in python
name = "Yash"
for i in name:
    print(i)

colors = ["Red", "Yellow", "Blue", "Green"]
for i in colors:
    print(i)
    for j in i:
        print(j)

# range function is used to define maximum number
for i in range(100):
    print(i)

# in range function we can define the range for the loop in example range(0, 10) that means loop start
# from 0 and end at 10-1 = 9
for i in range(0, 10):
    print(i)


#  range(start, stop, step)
for i in range(0, 2*10, 2):
    print(i)