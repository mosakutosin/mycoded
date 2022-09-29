from datetime import datetime
junior_staff_names = ["michael", "lekan", "tunde"]
senior_staff_names = ["mary", "chichi", "sandra"]

junior_staff = 50000
junior_allowance = 5000
junior_tax = int(junior_staff * (10 / 100))
junior_total = int(junior_staff + junior_allowance - junior_tax)

time = datetime.today()

senior_staff = 70000
senior_tax = int(senior_staff * (10 / 100))
senior_allowance = 10000
senior_total = int(senior_staff + senior_allowance - senior_tax)

print("JUNIOR STAFFS")
for junior in junior_staff_names:
    print(f"Biabol Travels and Tours\nPAY ADVICE SLIP\n{time.date()}\nStaff Name: {junior} \nSalary: {junior_staff} \nAllowance: {junior_allowance} \nTax: "
          f"{junior_tax} \n__________________\nTotal: #{junior_total} Naira \n********************")
print("\n\n\nSENIOR STAFFS")
for senior in senior_staff_names:
    print(f"Biabol Travels and Tours\nPAY ADVICE SLIP\n{time.date()}\nStaff Name: {senior} \nSalary: {senior_staff} \nAllowance: {senior_allowance} \nTax: "
          f"{senior_tax} \n__________________\nTotal: #{senior_total} Naira \n********************\n********************")

