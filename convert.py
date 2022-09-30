minute_cal = 24 * 60
second_cal = 24 * 60 * 60
m = "minutes"
s = "seconds"


def calculate(num):
    if num > 0:
        return f"For {num} days, we have {num * minute_cal} {m} and {num * second_cal} {s}  " \
               f"\n --------------------------------------------"
    elif num == 0:
        return "The value is zero, please input a positive value \n --------------------------------------------"
    else:
        return "Negative value, input positive value \n --------------------------------------------"


def validate():
    try:
        user_num = int(num_of_days)
        ans = calculate(user_num)
        print(ans)

    except ValueError:
        print("Wrong value, dont crash my program joor \n --------------------------------------------")


user = ""
while user != "exit":
    user = input("Hello User, please enter the number of days you want, and i will convert it to minutes "
                 "and seconds : \n")
    for num_of_days in set(user.split(",")):
        validate()
