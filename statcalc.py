import math

# print('  _____ _        _   _     _   _               \n /  ___| |      | | (_)   | | (_)              \n \ `--.| |_ __ _| |_ _ ___| |_ _  ___          \n  `--. | __/ _` | __| / __| __| |/ __|         \n /\__/ | || (_| | |_| \__ | |_| | (__          \n \____/ \__\__,_|\__|_|___/\__|_|\___|         \n            _            _       _             \n           | |          | |     | |            \n   ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ \n  / __/ _` | |/ __| | | | |/ _` | __/ _ \| ˙__|\n | (_| (_| | | (__| |_| | | (_| | || (_) | |   \n  \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|   \n')
datagiven = []
adatokszama = 0
adatosszeg = 0
while True:
    adatokszama += 1
    adat1 = input(f'Tárolandó adat {adatokszama}: ')
    if adat1 == 'stop':
        break            
    try:
        adatosszeg = float(adatosszeg) + float(adat1)
        datagiven.append(float(adat1))
    except:
        print('Csak szám adható meg adatnak')
        adatokszama -=1
        if adat1 == 'stop':
            break 
print(f'Az érvényes megadott adatok: {datagiven}')
atlaag = adatosszeg/adatokszama
def atlag():
    print(f'Az átlag: {adatosszeg/adatokszama}')
def median():
    datagiven.sort()
    kindian = datagiven[int(adatokszama/2)-1]
    if (adatokszama-1) % 2 == 0:
        print(f'A medián: {kindian + 0.5}')
    else:
        print(f' A medián: {kindian}')
def terj():
    maxim = 0
    minim = math.inf
    datagiven.sort()
    for i in datagiven:
        if i >= maxim:
            maxim = i
    for j in datagiven:
        if i <= minim:
            minim = j
    print(f'A terjedelem: {maxim-minim}')
def szoras():
    preosszeg = 0
    datagiven.sort(reverse=True)
    for i in datagiven:
        preszoras = (i - atlaag) ** 2
        preosszeg = preosszeg + preszoras
    rootable = preosszeg/adatokszama
    print(f'A szórás: {round(math.sqrt(rootable), 3)}')


print('Érvényes műveletek: *átlag*, *medián*, *terjedelem*, *szórás*, *módusz*, *szumma*, *elemszám*, *szerkeszt*')
muvelet = input('Az elvégzendő művelet: ')
while True:
    if muvelet == 'átlag':
        atlag()
        break
    elif muvelet == 'medián':
        median()
        break
    elif muvelet == 'terjedelem':
        terj()
        break
    elif muvelet == 'szórás':
        szoras()
        break
    else:
        print('Érvénytelen művelet!')