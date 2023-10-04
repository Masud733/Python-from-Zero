# Checking if an object is an instance of a specific class
class Dog:
    pass

dog_instance = Dog()
if isinstance(dog_instance,Dog):
    print("It's a Dog!")
else:
    print("It's a not Dog!")
# Checking if an object is an instance of one of multiple classes
class Cow:
    pass
class Goat:
    pass
animal_instance = Cow()
if isinstance(animal_instance,(Cow,Goat)):
    print("It's either a cow or a goat")
else:
    print("It's neither a cow or a goat.")


