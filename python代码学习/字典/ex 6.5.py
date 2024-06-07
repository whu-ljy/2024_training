rivers = {
    'nile' : 'egypt',
    'yellowriver' : 'china',
    'xinnongchuan' : 'japan',
    }
for i,j in rivers.items():
    print(f"The{i} run through {j}")

for i in rivers.keys():
    print(f"{i}")

for i in rivers.values():
    print(i)