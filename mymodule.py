def greeting(name):
  print("Hello, " + name)

import mymodule

mymodule.greeting("Jonathan")

# mymodule.py

person1 = {
    "Name" : "Masud",
    "age" : 22,
"Location" : "Khulna",

}
import mymodule

# Access the person1 dictionary from the imported module
person = mymodule.person1

# Access and print the dictionary values
print("Name ",person["Name"])
print("Age ",person["age"])
print("Location",person["Location"])

#You can choose to import only parts from a module, by using the from keyword.
def myfunc(name):
    print("hello this is " +name)
person2 ={
    "name":"Mickey",
    "age": 16,
    "location":"Texas",
}
from mymodule import person2
print("The name is", person2["name"])

