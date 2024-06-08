def make_album(singername,albumname,number = None):
    if number == None:
        albumdic = {'歌手名字' : singername , '专辑名' : albumname }
    else:
        albumdic = {'歌手名字' : singername , '专辑名' : albumname ,'歌曲数' : number}
    return albumdic
print(make_album('周杰伦','依然范特西'))
print(make_album('王力宏','火力全开'))
print(make_album('林俊杰','新地球'))

print(make_album('乃万','BUT U','10'))