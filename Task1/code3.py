products = ["Book", "Bag", "Pen"]
old = [100, 500, 20]
new = [130, 550, 25]

for i in range(len(products)):
    change = (new[i] - old[i]) / old[i] * 100

    print(products[i], "Change:", round(change, 2), "%")

    if change > 20:
        print("High price increase")
