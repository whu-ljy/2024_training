cities = {
    'wuhan' : {'country' : 'china','population' : 1000000 ,'fact' : 'weather is hot'},
    'shouer' : {'country' : 'korea','population' : 500000 ,'fact' : 'city is nice'},
    'dongjing' : {'country' : 'jopan','population' : 800000 ,'fact' : 'city is fantastic'},
}

for i,j in cities.items():
    print(f"{i}的信息 国家是{j['country']} 人口数是{j['population']} 真相是{j['fact']}")