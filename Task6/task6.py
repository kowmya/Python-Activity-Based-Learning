appliances = ["Fan", "Light", "AC"]
before = [100, 60, 200]
after = [70, 30, 120]
savings = []

for i in range(len(appliances)):
    saved = before[i] - after[i]
    percent = saved / before[i] * 100
    savings.append(percent)

    print(appliances[i], "Savings:", round(percent, 2), "%")

best = savings.index(max(savings))
print("Highest savings:", appliances[best])
