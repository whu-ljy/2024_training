print("pastrami卖完了！！！")
sandwich_orders = ['pastrami','pastrami','beef','vegetables','pastrami','pork']
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
finished_sandwich = []
while sandwich_orders:
    if sandwich_orders ==  []:
        print("三明治都做完了")
        print(f"finished_sandwich")
    current_sandwich = sandwich_orders.pop()
    print(f"I made you {current_sandwich} sandwich")
    finished_sandwich.append(current_sandwich)
print(finished_sandwich)
    