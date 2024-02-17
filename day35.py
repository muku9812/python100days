# for loop with else

# for i in range(1, 5):
#     print(i)
#
# else:
#     print("End of the loop")

for i in range(1, 5):
    if i == 2:
        break
    print(i)
else:
    print("End of the loop")
# Different method of printing the iteration
for i in range(1, 5):
    if i == 2:
        continue
    print(i)
else:
    print("End of the loop")

for i in range(10):
    print("Iteration no {} is for loop".format(i+1))
else:
    print("This is else block")
print("I am out of the loop")
