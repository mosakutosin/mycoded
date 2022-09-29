class Item:
    def __init__(self, name: str, price: float, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate(self):
        return self.price * self.quantity


item1 = Item("Phone", 100, 5)
item2 = Item("Laptop", 1000, 3)

print(item1.calculate())


print(item1.name)
print(item2.name)
print(item1.price)
print(item2.price)
print(item1.quantity)
print(item2.quantity)

name = {'name': 'Michael', 'age':30}
num2 = [2,3,4,5,6,5,6,7,8,9]
for num in num2:
    print(f"{num}.{name}")

user = input("Please password : \n")

if user == "michael":
    print(f"Welcome user,{user} let's go")

