from datetime import datetime

user_input = input("Please enter your goal and time separated by a colon\n")
input_list = user_input.split(":")

goal = input_list[0]
deadline = input_list[1]

deadline_date = datetime.strptime(deadline, "%d.%m.%Y")
today_date = datetime.today()
time_remain = deadline_date - today_date
hours = int(time_remain.total_seconds() / 60 / 60)

print(f"Dear user, the time left for your goal {goal.upper()} is {time_remain.days} days {hours} hours")
