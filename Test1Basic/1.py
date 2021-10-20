def Strom(Speed):
    if 0<= Speed <=51.99:
        return ('Breeze.')
    elif 52.00<= Speed <=55.99:
        return ('Depression.')
    elif 56.00<= Speed <=101.99:
        return ('Tropical Storm.')
    elif 102.00<= Speed <=208.99:
        return ('Typhoon.')
    elif Speed >=209:
        return ('Super Typhoon.')
    



print(' *** Wind classification ***')
Speed =float(input('Enter wind speed (km/h) : '))
if Speed>=0:
    print('Wind classification is',Strom(Speed))
else:
    print('!!!Wrong value can\'t classify.')