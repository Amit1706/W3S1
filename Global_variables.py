a = "Good"
def myfunc():
    print("I m " + a)
myfunc()   

b = "Elon Musk"
c = "Tesla Motors"
print(c + " is owned by " + b)

d = "Reliance"
e = "Mukesh Ambani"
def cat():
    # print(d + " is owned by " + e)
    d = "Jio"
    print(d + " is owned by " + e)
    print(d)
cat()    
print(d)    

def amit():
    print(c + " is owned by " + b)
amit()

def dog():
    global c 
    c = "SpaceX"
    print(c + " is owned by " + b)
dog()  

print(c)