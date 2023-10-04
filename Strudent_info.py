class Student:
    def __init__(self, name, age, roll_number):
        self.name = name
        self.age = age
        self.roll_number = roll_number

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll Number: {self.roll_number}")

# Creating instances
student1 = Student("Niragi", 21, 701101)
student2 = Student("Usagi", 22, 701102)

# Display information
print("Student 1:")
student1.display_info()

print("\nStudent 2:")
student2.display_info()

