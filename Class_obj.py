'''
All classes have a function called __init__(), which is always executed when the class is being initiated.

Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:
'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
p1 = person("John",35)
print(p1.name)
print(p1.age)

class person1:
    def __init__(self,name,age): #The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
        self.name = name
        self.age = age
    def __str__(self):
       return f"{self.name}({self.age})" #Karim(25)
p2 = person1("Karim",25)
print(p2)

class person2:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " +self.name)
p2 = person2("Daud Khan", 48)
p2.myfunc()

class Myclass:
    def __init__(self,value):
        self.value = value
    def value_check(self):
        if self.value > 0:
            return "The value is positive"
        elif self.value < 0:
            return "The value is negative"
        else:
            return "The value is zero"
obj = Myclass(42)
result = obj.value_check()
print(result)


