names = ["Ravi", "Raju", "Sita"]
marks = [80, 35, 55]
attendance = [90, 60, 80]
lab = [85, 40, 45]

for i in range(len(names)):
    risk = 0

    if marks[i] < 40:
        risk += 1
    if attendance[i] < 75:
        risk += 1
    if lab[i] < 50:
        risk += 1

    print(names[i], end=": ")

    if risk >= 2:
        print("High Risk")
    elif risk == 1:
        print("Medium Risk")
    else:
        print("Low Risk")
