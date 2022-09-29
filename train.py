number = 3
number2 = 4

print(number)

#Ternary If Statement
number = 2
message = "positive" if number < 0 else "negative"

print(message)
#######################

numbers = [2,3,5,3,6]
for num in numbers:
    print(num)
numbers.sort()
numbers.remove(2)
numbers.pop()
nums = {"A","C"}
num2 = {"B","C"}
print(numbers)
#Union set
print(nums | num2)

#intersection set
print(nums & num2)

#difference set
print(nums - num2)

#Dictionary
person = {"Name": "Michael", "Age": 60, "Address": "Shonola" }
print(person.values())
for key, value in person.items():
    print(f"{key}: {value}")
#or use this
for key in person:
    print(f"{key}: {person[key]}")

#for loop
numbers = [2,3,4,5,6,7,8]
for num in numbers:
    print(num)
#exercise for loop
total = 0
numbers = [1,2,3,4,5,6,7,8,9,10]
for number in numbers:
    total += number
    print(total)
print(f"Result is {total}")

#while loop
number = 0

while number < 5:
    number += 1
    print(number)
else:
    print("loop ended")'''

#break and continue
'''number = 0
while number < 10:
    if number == 5:
        break
    number+= 1
    print(number)
number = 0
while number < 10:
    number += 1
    if number < 5:
        continue
    print(number)

def adult(age):
    if age < 18 :
        print(f"You are not an adult because you are {age} years")
    else:
        print(f"You are an adult because you are {age} years")
age = int(input("Please enter your age: \n"))
adult(age)

def fib(n): # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
        print()
def fib2(n): # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        return result

fib(20)
class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart


y = Complex(3,5)
print(y.r, y.i)


class Dog:
    kind = 'canine' # class variable shared by all instances
    def __init__(self, name):
        self.name = name # instance variable unique to each instance
        d = Dog('Fido')
        e = Dog('Buddy')
