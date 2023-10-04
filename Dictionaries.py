#create and access dictionary items
student = {"name":"Masud", "age":22,"Major":"Computer Science"}
print(student["name"])
print(student["age"])

#looping through dictionary key and values
for key, value in student.items():
    print(key, ":", value)


fruits = ["apple", "banana", "cherry"]
print("First fruit:", fruits[0])

# Adding an item to the list
fruits.append("grape")

# Iterating through the list
for fruit in fruits:
    print(fruit)



