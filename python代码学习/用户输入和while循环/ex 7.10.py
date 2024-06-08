places = []
while True:
    place = input("如果你可以去世界上任意一个地方 你想要去哪里？（直接回车表示退出）")
    if place == '':
        break
    places.append(place)
for i in places:
    print(f"{i}")