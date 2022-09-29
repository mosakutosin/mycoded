from datetime import datetime
junior_staff_names = ["michael", "lekan", "tunde"]
senior_staff_names = ["mary", "chichi", "sandra"]

time = datetime.today()
junior_staff = 50000
junior_allowance = 5000
junior_tax = int(junior_staff * (10 / 100))
junior_total = int(junior_staff + junior_allowance - junior_tax)

senior_staff = 70000
senior_tax = int(senior_staff * (10 / 100))
senior_allowance = 10000
senior_total = int(senior_staff + senior_allowance - senior_tax)

print(f"Biabol Travels and Tours\nPAY ADVICE SLIP\n{time.date()}\nStaff Name: {junior_staff_names[0]} \nSalary: {junior_staff} \nAllowance: {junior_allowance} \nTax: "
          f"{junior_tax} \n___________\nTotal: #{junior_total} Naira \n********************")