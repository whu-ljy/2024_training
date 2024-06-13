from pathlib import Path

path = Path('guest.txt')
contents = input("请输入你的名字")
path.write_text(contents)
