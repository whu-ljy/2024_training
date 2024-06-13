from pathlib import Path
import json

like_numbers = input("输入你喜欢的数字")
path = Path('like_numbers.json')
contents = json.dumps(like_numbers)
path.write_text(contents)

number = path.read_text()
print(f"I know you like {number}")