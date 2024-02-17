# string formatting

sentences = "Hey I am {0} and I am from {1}."
name = "Mukesh"
address = "Nepal"
# first method
print(sentences.format(name, address))

print(f"Hey I am {name} and I am from {address}.")


price = 12.29021211
print(f"The price of apple is {price:.2f} per kg.")


# we can do this like this.
print(f"Hello My name is {{Name}} and I am from {{address}}")