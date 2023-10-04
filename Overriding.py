#defining a method with the same name in both the parent and child classes,
class animal:
    def speak(self):
        print("Animal speak!")
# child class method overrides the behavior of the parent class method.
class dog(animal):
        def speak(self):
            print("Dog speak Vew")
class cat(animal):
        def speak(self):
            print("Cat speak mew")
#create instance or  object
Cat = cat()
Dog = dog()
# Calling the overridden methods
speak1 = Cat.speak()
speak2 = Dog.speak()

