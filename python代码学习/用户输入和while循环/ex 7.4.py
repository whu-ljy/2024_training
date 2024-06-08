prompt = "输入你想要的批萨配料(输入quit表示你不想要了)"
a = ""
while a != 'quit':
    a = input(prompt)
    print(f"你添加了{a}")