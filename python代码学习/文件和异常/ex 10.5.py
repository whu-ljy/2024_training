from pathlib import Path

path = Path('guest2.txt')
contents = ''
while True:
    contents0 = input("请输入你的名字:(输入quit退出)")
    if contents0 != 'quit':
        contents1 = f"{contents0} \n"
        contents += contents1
    else:
        break
path.write_text(contents)
