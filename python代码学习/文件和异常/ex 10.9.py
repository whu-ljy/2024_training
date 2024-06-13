from pathlib import Path


try :
    path1 = Path('cats.txt')
    contents1 = path1.read_text()
    print(contents1)
except FileNotFoundError:
    pass

try :
    path2 = Path('dogs.txt')
    contents2 = path2.read_text()
    print(contents2)
except FileNotFoundError:
    pass
    