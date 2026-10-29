

data = [[100, 5], [200, 30], [150, 10]]
limit = 10

for i in range(len(data)):
    total = data[i][0]
    defective = data[i][1]
    percent = defective / total * 100

    print("Batch", i + 1)
    print("Defect percentage:", round(percent, 2))

    if percent > limit:
        print("Quality Failed")
    else:
        print("Quality Passed")
