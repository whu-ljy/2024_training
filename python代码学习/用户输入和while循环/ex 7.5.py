age = ''
while True:
    age = input("你的年龄是：(输入0退出)")
    age = int(age)
    if age == 0:
        break
    elif age < 3:
        price = 0
    elif age <12 :
        price = 10
    else:
        price = 15
    print(f"你的票价是{price}")