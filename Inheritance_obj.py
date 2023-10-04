class employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showDetails(self):
        print(f"He is {self.name} & the id is {self.id}")
#inherite employee class in programmer
class programmer(employee):
    def showLanguage(self):
        print("The dafault language is python.")
e1 = employee("Musa Samsher",1000233)
e1.showDetails()
e2 = programmer("Masud Mehrab", 11220120733)
e2.showDetails()
e2.showLanguage()


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # Placeholder method

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating instances
dog = Dog("Tommy")
cat = Cat("Tyson")

# Calling methods
print(dog.speak())
print(cat.speak())


