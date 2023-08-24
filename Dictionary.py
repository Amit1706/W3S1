car = {
    "Company" : "BMW",
    "Series" : 7,
    "Model" : "740i"
}
print(car)
print(len(car))
a = car["Model"]
print(a)
b = car.keys()
print(b)
car["Color"] = "Black"
print(b)
c = car.items
print(c)
d = car.pop("Model")
print(car)

# Dictionary that contain 3 dictionaries
Family = {
    "Amit" : {
        "Age" : 21,
        "Gender" : "Male",
        "Ed" : "B.Tech"
    },
    "Bharti" : {
        "Age" : 51,
        "Gender" : "Female",
        "Ed" : "B.Com"
    },
    "Manoj" : {
        "Age" : 51,
        "Gender" : "Male",
        "Ed" : "B.Pharma"
    }
}
print(Family)

# Dictionary Methods
# clear()	Removes all the elements from the dictionary
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# get()	Returns the value of the specified key
# items()	Returns a list containing a tuple for each key value pair
# keys()	Returns a list containing the dictionary's keys
# pop()	Removes the element with the specified key
# popitem()	Removes the last inserted key-value pair
# setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	Updates the dictionary with the specified key-value pairs
# values()	Returns a list of all the values in the dictionary