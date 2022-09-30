hours = 24
minute = 24 * 60
seconds = 24 * 60 * 60
h = "hours"
m = "minutes"
s = "seconds"


def calculate(num):
    print(f"{num} days has {num * hours} {h}, {num * minute} {m} and {num * seconds} {s}")


user = int(input("Hey user, input any number of days and i will convert to hours, minutes and seconds: \n"))


def validate():
    try:
        if user < 0:
            print("The value is less than zero")
        elif user == 0:
            print("Enter positive value")
        else:
            calculate(user)
    except ValueError:
        print("Nonxense")


validate()

