minute_cal = 24 * 60
second_cal = 24 * 60 * 60
m = "minutes"
s = "seconds"


def calculate(num):
    if num > 0:
        return f"For {num} days, we have {num * minute_cal} {m} and {num * second_cal} {s}"
    elif num == 0:
        return "The value is zero, please input a positive value"
    else:
        return "Negative value, input positive value"


user = input("Hello User, please enter the days you want to convert : \n")


def validate():
    if user.isdigit():
        user_num = int(user)
        ans = calculate(user_num)
        print(ans)
    else:
        print("Wrong value, dont crash my program joor")


validate()

