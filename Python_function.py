def myfunction(fname):
    print(fname + " Ali")
myfunction("Moeen")
myfunction("Fazar")

def myFunction(*kids):
    print("The youngest kid "+ kids[2])
myFunction("Nilima","Sruti","Saad")

def function(fname,lname):
    print(fname+" "+lname)
function(fname = "Masud", lname = "Mehrab")

def Function(**boys):
    print("The brilliant boy "+boys["sboy"])
Function(fboy="Karim",sboy="Ashik",lboy="Zoro")

def funcountry(country = "Bangladesh"):
    print("Im from " +country)
funcountry()
funcountry("Sweden")

def foodfunc(food):
    for x in food:
        print(x)
fruit = {"Mango","Banana","Avocado"}
foodfunc(fruit)

def my_function(x):
    return 10*x
print(my_function(2))
print(my_function(3))