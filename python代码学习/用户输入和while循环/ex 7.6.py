prompt = "输入你想要的批萨配料(输入quit表示你不想要了)"
active = ""
while True:
    active = input(prompt)
    if active != 'quit':
        print(f"你添加了{active}")
    else:
        break

