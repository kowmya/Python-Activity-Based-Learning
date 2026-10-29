orders = [
    ("Book", 50, 30, 2),
    ("Pen", 100, 120, 1),
    ("Bag", 20, 10, 3)
]
orders.sort(key=lambda x: x[3])

for product, stock, demand, priority in orders:
    supplied = min(stock, demand)
    pending = demand - supplied

    print("Product:", product)
    print("Supplied:", supplied)
    print("Pending:", pending)

    if pending == 0:
        print("Order Completed")
    else:
        print("Order Partially Completed")
