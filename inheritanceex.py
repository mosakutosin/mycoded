class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old")


class Cat(Pet): #The Cat class inheritted the Pet class letting it have access to the Pet functions
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and i am {self.age} years old and i am {self.color}")


class Dog(Pet): #The Dog class inheritted the Pet class letting it have access to the Pet functions
    def speak(self):
        print("Bark")


p = Pet("Tim", 24)
p.show()
c = Cat("Shawn", 4, "brown")
c.speak()
c.show()
d = Dog("Bryan", 38)
d.speak()
