print("请输入两个数 我来帮你加起来")
print("输入q来退出")

while True:
    first_number = input("第一个数字:")
    if first_number == 'q':
        break

    try:
        first_number = int(first_number)
    except ValueError:
        print("请输入数字！")
        continue
    
        
    second_number = input("第二个数字：")
    if second_number == 'q':
        break

    try:
            second_number = int(second_number)
    except ValueError:
            print("请输入数字！")
            continue
    
    answer = first_number + second_number
    print(f"答案是{answer}")
        