while True:
    singername = input("输入歌手的名字(输入quit退出)")
    if singername == 'quit':
        break
    albumname = input("输入专辑名字(输入quit退出)")
    if albumname == 'quit':
        break
    albumdic = {'歌手名字' : singername , '专辑名字' : albumname,}

print(albumdic)