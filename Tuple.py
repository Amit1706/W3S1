# Tuple
thistuple = ("apple",)
print(type(thistuple))

# Not a tuple(only string)  (Because of comma)
thistuple = ("apple")
print(type(thistuple))

mytuple = ("apple", "banana", "cherry",)
print(type(mytuple))

tuple1 = ("Amit", "Neha", "Karan",)
y = list(tuple1)
print(y)
print(type(y))
y[1] = "Saloni"
x = tuple(y)
print(x)
z = ("Saumya",)
tuple1 += z
print(tuple1)

# # Tuple Methods
# count()	Returns the number of times a specified value occurs in a tuple
# index()	Searches the tuple for a specified value and returns the position of where it was found