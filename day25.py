# operations in tuple

color1 = ('Red', 'Blue', 'Green', 'Yellow', 'Black')
temp = list(color1)
temp.append('Pink')  # add
temp.pop(3)  # remove
temp[2] = 'White'  # change
color1 = tuple(temp)
print(color1)


# concat tuple
color2 = ('Indigo', 'Purple', 'Black', 'Blue')
colors = color1 + color2
print(colors)
find = colors.index('Purple', 3, 9)
print(find)
print(colors.count('Black'))