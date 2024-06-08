def make_car(maker,type,**cardic):
    cardic['制造商'] = maker
    cardic['型号'] = type
    return cardic

car = make_car('华晨' ,'530', color = 'white' ,size = 'Li')
print(f"{car}")
 
              
    