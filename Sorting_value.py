class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

people = [
    Person('Alice', 25),
    Person('Harun', 32),
    Person('Michel', 45)
]

sorted_people = sorted(people, key=lambda x: x.age)
print([person.name for person in sorted_people])
print(sorted_people)


