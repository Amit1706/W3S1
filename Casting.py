a = 43
b = 45.7
c = 23
d = str(a)
e = int(b)
f = float(c)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
a = float(a)
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
print(type(f))

mylist = ["apple", "banana", "cherry"]
print(type(mylist))

mylist = ("apple", "banana", "cherry")
print(type(mylist))

mylist = {"apple", "banana", "cherry"}
print(type(mylist))

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
thislist.pop(2)
print(thislist)

list = ["BMW", "Mercedes", "Audi", "Tesla", "Volkaswagon"]
list.append("Rolls Royce")
print(list)
list.insert(1, "Toyota")
print(list)
list.remove("Audi")
print(list)

tlist = ["apple", "banana", "cherry"]
ttuple = ("kiwi", "orange")
tlist.extend(ttuple)
print(tlist)