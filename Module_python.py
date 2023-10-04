# mymodule.py

person1 = {
    "name": "John",
    "age": 30,
    "city": "New York"
}
import mymodule  # Import the mymodule module

# Access the person1 dictionary from the imported module
person = mymodule.person1

# Access and print the dictionary values
print("Name:", person["name"])
print("Age:", person["age"])
print("City:", person["city"])
