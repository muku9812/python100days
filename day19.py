# break and continue statement

for i in range(5):
    if i == 3:
        break
    print(i)
# it completely stops the loop
for j in range(1, 100):
    print("10 X ", j, "=", j * 10)
    if j == 10:
        break
# it only ignores the condition from if
for k in range(11):
    if k == 0:
        continue
    print("12 X ", k, "=", k * 12)
