class programmer:
    def __init__(self,name,id,favrt_language):
        self.name = name
        self.id = id
        self.favrt_language = favrt_language
    def display_programmer(self):
        print(f"The programmer name is {self.name} his id {self.id} and his favorite language is {self.favrt_language}")
class parents:
    def __init__(self,fname,mname):
        self.fname = fname
        self.mname = mname
    def display_parents(self):
        print(f"Fsather's name is: {self.fname}")
        print(f"Mother's name is: {self.mname}")
#The Child class is a subclass of both Programmer and Parents. It inherits their attributes and methods
#by calling their constructors using Programmer.__init__ and Parents.__init__ within its own constructor.
class Child(programmer,parents):
    def __init__(self,name,id,favrt_language,fname,mname):
        programmer.__init__(self,name,id,favrt_language)
        parents.__init__(self,fname,mname)
    def display_child(self):
        print("Child Details: ")
        self.display_programmer()
        self.display_parents()
# Create an instance of the Child class
child = Child("Masud Mehrab",11220120733,"Python","Wali Ullah","Farida Farin")
child.display_child()


