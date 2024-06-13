from pathlib import Path
import json

path = Path('like_numbers.json')

if path.stat().st_size != 0:
    number = path.read_text()
    like_numbers = json.loads(number)
    print(f"I know you like {like_numbers}")
else:
    like_numbers = input("输入你喜欢的数字")
    contents = json.dumps(like_numbers)
    path.write_text(contents)
    print("已成功写入你喜欢的数字")
