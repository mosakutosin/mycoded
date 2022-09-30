class Person:
    def __init__(self, name, age, position):
        self.name = name
        self.age = age
        self.position = position

    def walk(self):
        print(f"i am {self.name} and i am walking...")


staff1 = Person("Peter", 30, "Senior")
staff2 = Person("Michael", 20, "Junior")

print(staff1.name)
print(staff2.__dict__)
print(staff2.walk())
