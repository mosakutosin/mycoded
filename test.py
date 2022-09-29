from datetime import datetime

user_input = input("Please enetr two values\n")
user = user_input.split(":")

goal = user[0]
time = user[1]

deadline = datetime.strptime(time, "%d.%m.%Y")
today = datetime.today()
remain = deadline - today
hours = int(remain.total_seconds() / 60 / 60)

print(f"The remaining date for {goal.upper()} is {remain.days} days {hours} hours")
