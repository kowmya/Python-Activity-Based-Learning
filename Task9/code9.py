
apartments = ["A", "B", "C"]
units = [80, 150, 250]
fixed_charge = 50

for i in range(len(apartments)):
    u = units[i]

    if u <= 100:
        bill = u * 2
    elif u <= 200:
        bill = 100 * 2 + (u - 100) * 3
    else:
        bill = 100 * 2 + 100 * 3 + (u - 200) * 5

    bill += fixed_charge

    if u < 100:
        bill -= 10

    print(apartments[i], "Units:", u, "Bill:", bill)
