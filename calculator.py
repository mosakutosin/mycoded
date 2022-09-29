import re

print("My Calculator Program")
print("Type 'quit' to exit \n")
previous = 0
run = True


def cal():
    global run
    global previous
    equation = ""

    if previous == 0:
        equation = input("Enter value: ")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        print("Good bye human")
        run = False
        print('End of calculation!')
    else:
        equation = re.sub('[a-zA-Z,./()""]', "", equation)

        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous) + equation)


while run:
    cal()