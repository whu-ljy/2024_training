def sand(*food):
    print("你的三明治里面有: ")
    for i in food:       
        print(f"{i}  ")

sand('beef','vegetable')
sand('tomato')
sand('potato','vegetable','pork')