class Person:
    price = 60

    def __init__(self, name, age, salary, department):
        self.name = name
        self.age = age
        self.salary = salary
        self.department = department

    def juniorstaff(self):
        print(f"The staffs for the months are: {self.name} {self.age} {self.salary} {self.department}")

    def cal(self):
        print(f"Amount is: {self.price}")


person1 = Person("Michael", 30, 30000, "Printing")
person1.juniorstaff()
person1.cal()

person2 = Person("Seun", 20, 40000, "Finishing")
person2.juniorstaff()
person1.cal()

