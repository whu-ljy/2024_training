sandwich_orders = ['a','b','c']
finished_sandwich = []
while sandwich_orders:
    if sandwich_orders ==  []:
        print("三明治都做完了")
        print(f"finished_sandwich")
    current_sandwich = sandwich_orders.pop()
    print(f"I made you {current_sandwich}")
    finished_sandwich.append(current_sandwich)
    