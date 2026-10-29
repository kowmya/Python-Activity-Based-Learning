students = [
    ("Ravi", 85, 90, 150000),
    ("Raju", 75, 80, 100000),
    ("Sita", 95, 95, 200000),
    ("Kiran", 60, 90, 80000)
]

eligible = []

for name, marks, attendance, income in students:
    if marks >= 70 and attendance >= 75 and income <= 150000:
        eligible.append((name, marks))

eligible.sort(key=lambda x: x[1], reverse=True)

quota = 2

print("Selected Students:")
for student in eligible[:quota]:
    print(student[0], student[1])
