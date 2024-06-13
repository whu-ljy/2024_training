from pathlib import Path

path1 = Path('cats.txt')

try :
    path1 = Path('cats.txt')
    contents1 = path1.read_text()
    print(contents1)
except FileNotFoundError:
    print("没找到文件")
    


