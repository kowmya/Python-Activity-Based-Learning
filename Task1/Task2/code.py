areas = ["Area A", "Area B", "Area C"]
demand = [100, 150, 200]
supply = [80, 100, 120]

shortages = []

for i in range(len(areas)):
    shortage = demand[i] - supply[i]
    shortages.append(shortage)
    print(areas[i], "Shortage:", shortage)

index = shortages.index(max(shortages))
print("Most underserved:", areas[index])
