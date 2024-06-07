favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'rust',
    'phil' : 'python',
}

people = ['jen' , 'sarah' , 'ljy']
for i in people:
    if i in favorite_languages.keys():
        print(f"{i},thanks!")
    else:
        print(f"{i},please come")