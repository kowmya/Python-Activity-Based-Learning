students = [
    ("Ravi", 10000, 90, 35),
    ("Raju", 7000, 60, 25),
    ("Sita", 10000, 80, 20)
]

required_fee = 10000

for name, fee, attendance, marks in students:
    problems = []

    if fee < required_fee:
        problems.append("Fee Pending")
    if attendance < 75:
        problems.append("Low Attendance")
    if marks < 20:
        problems.append("Low Marks")

    print(name)

    if len(problems) == 0:
        print("Eligible")
    else:
        print("Not Eligible:", problems)
